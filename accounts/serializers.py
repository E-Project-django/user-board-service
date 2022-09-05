from django.contrib.auth.models import update_last_login
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        required=True,
        validators=[validate_password],
    )
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'confirm_password', 'age', 'gender', 'phone_number']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다."})

        return data

    def create(self, validated_data):
        """
        유저를 생성하고 토큰을 생성
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            age=validated_data['age'],
            gender=validated_data['gender'],
            phone_number=validated_data['phone_number'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)

        return user


class LoginSerializer(serializers.Serializer):
    """
    로그인
    로그인과 함께 토큰 생성
    """
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password', None)
        user = authenticate(username=username, password=password)

        if user:
            token = Token.objects.get(user=user)
            update_last_login(None, user)
            return token

        raise serializers.ValidationError(
            {'error': '로그인 할 수 없습니다'}
        )


class UsersSerializer(serializers.ModelSerializer):
    """
    유저 목록 조회
    """
    class Meta:
        model = User
        fields= ['id', 'username', 'age', 'gender', 'phone_number', 'is_active', 'is_staff']


class UserSerializer(serializers.ModelSerializer):
    """
    단일 유저 조회와 수정
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'age', 'gender', 'phone_number']


class MakeStaffSerializer(serializers.ModelSerializer):
    """
    is_staff 변경
    """
    class Meta:
        model = User
        fields = ['is_staff']


class SoftDeleteSerializer(serializers.ModelSerializer):
    """
    is_active 변경
    """
    class Meta:
        model = User
        fields = ['is_active']

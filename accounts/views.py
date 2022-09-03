from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer, UserSerializer, MakeStaffSerializer, SoftDeleteSerializer, LoginSerializer


class RegisterAPI(generics.CreateAPIView):
    """
    회원가입 API
    회원 생성과 토큰 생성
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginAPI(generics.GenericAPIView):
    """
    로그인 API
    username, password, token으로 유효성 판단
    token을 리턴함
    """
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class AccountAPI(generics.RetrieveUpdateAPIView):
    """
    회원 조회, 회원 정보 수정 API
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class MakeStaffAPI(generics.UpdateAPIView):
    """
    관리자 임명 API
    is_staff를 변경
    """
    queryset = User.objects.all()
    serializer_class = MakeStaffSerializer
    lookup_field = 'username'


class SoftDeleteAPI(generics.UpdateAPIView):
    """
    sof-delete를 위한 API
    is_active를 변경
    """
    queryset = User.objects.all()
    serializer_class = SoftDeleteSerializer
    lookup_field = 'username'

from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .permission import IsOwner, IsOwnerOrStaff
from .models import User
from .serializers import RegisterSerializer, UsersSerializer, UserSerializer, \
    MakeStaffSerializer, SoftDeleteSerializer, LoginSerializer


class RegisterAPI(generics.CreateAPIView):
    """
    회원가입 API
    누구나 접근 가능
    회원 생성과 토큰 생성
    """
    permission_classes = [AllowAny]

    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginAPI(generics.GenericAPIView):
    """
    로그인 API
    누구나 접근 가능
    username, password, token으로 유효성 판단
    token을 리턴함
    """
    permission_classes = [AllowAny]

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class AccountListAPI(generics.ListAPIView):
    """
    회원 목록 조회
    관리자만 접근 가능(is_staff==True)
    """
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = UsersSerializer


class AccountDetailAPI(generics.RetrieveUpdateAPIView):
    """
    단일 회원 조회, 회원 정보 수정 API
    본인만 접근 가능
    """
    permission_classes = [IsOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class MakeStaffAPI(generics.UpdateAPIView):
    """
    관리자 임명 API
    관리자만 접근 가능(is_staff==True)
    is_staff를 변경
    """
    permission_classes = [IsAdminUser]

    queryset = User.objects.all()
    serializer_class = MakeStaffSerializer
    lookup_field = 'username'


class SoftDeleteAPI(generics.UpdateAPIView):
    """
    sof-delete를 위한 API
    관리자와 본인 접근 가능
    is_active를 변경
    """
    permission_classes = [IsOwnerOrStaff]

    queryset = User.objects.all()
    serializer_class = SoftDeleteSerializer
    lookup_field = 'username'

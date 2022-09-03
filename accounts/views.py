from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer, UserSerializer, MakeStaffSerializer, SoftDeleteSerializer, LoginSerializer


class RegisterAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({'token': token.key}, status=status.HTTP_200_OK)


class AccountAPI(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'username'


class MakeStaffAPI(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = MakeStaffSerializer
    lookup_field = 'username'


class SoftDeleteAPI(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = SoftDeleteSerializer
    lookup_field = 'username'

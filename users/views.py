from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from users import serializers


class UsersRegister(APIView):
    def post(self, request):
        """
        회원가입
        POST /api/v1/users/register/
        """
        serializer = serializers.UsersRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"message": "Fail Register"}, status=status.HTTP_400_BAD_REQUEST
        )


class Login(APIView):
    """
    로그인
    POST /api/v1/users/login/
    """

    def post(self, request):
        user = authenticate(
            username=request.data.get("username"), password=request.data.get("password")
        )
        if user is not None:
            serializer = serializers.UsersSerializer(user)
            token = TokenObtainPairSerializer.get_token(user)
            access_token = str(token.access_token)
            refresh_token = str(token)
            response = Response(
                {
                    "message": "login success",
                    "user": serializer.data,
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            response.set_cookie(key="access", value=access_token, httponly=True)
            response.set_cookie(key="refresh", value=refresh_token, httponly=True)
            return response
        else:
            return Response(
                {"message": "Fail Login"}, status=status.HTTP_400_BAD_REQUEST
            )


class Logout(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        로그아웃
        POST /api/v1/users/logout/
        """
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            response = Response(
                {"message": "Logout Success"}, status=status.HTTP_200_OK
            )

            response.delete_cookie("access")
            response.delete_cookie("refresh")

            return response
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

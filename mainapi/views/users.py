from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from ..serializers.users import RegisterSerializer
from ..utils import execution_time_logger

class RegisterView(APIView):
    """
    POST /api/register/
    Registers a new user with unique email and username.
    """
    permission_classes = [AllowAny]

    @execution_time_logger
    def post(self, request, version):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    """
    POST /api/login/
    Authenticates a user and returns a JWT token if valid.
    """
    permission_classes = [AllowAny]

    @execution_time_logger
    def post(self, request, version):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    """
    POST /api/logout/
    Logs out the user by blacklisting the provided token.
    """
    permission_classes = [IsAuthenticated]

    @execution_time_logger
    def post(self, request, version):
        try:
            print(request.user.is_authenticated)
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Logout failed"}, status=status.HTTP_400_BAD_REQUEST)

# myapp/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

from .models import CustomUser
from .serializers import CustomUserSerializer, LoginSerializer

# View to handle user creation
class CreateUserView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (AllowAny,)

# View to handle user login
class LoginView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        # Validate login data using LoginSerializer
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        # Authenticate user using email and password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Generate or retrieve a token for the authenticated user
            token, created = Token.objects.get_or_create(user=user)
            # Return token, user_id, and email in the response
            return Response({'token': token.key, 'user_id': user.id, 'email': user.email}, status=status.HTTP_200_OK)
        else:
            # Return error response for invalid credentials
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# View to retrieve, update, and delete user details
class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        # Retrieve the user making the request
        return self.request.user

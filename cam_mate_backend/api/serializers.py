from rest_framework import serializers
from api.models import User, UserManager
from rest_framework.authentication import authenticate
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'is_active', 'is_staff']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()  # Email field for login
    password = serializers.CharField(write_only=True)  # Password field (write-only)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(email=email, password=password)

        # Check if authentication was successful
        if not user:
            raise serializers.ValidationError("Invalid email or password.")

        # Check if user account is active
        if not user.is_active:
            raise serializers.ValidationError("User account is inactive.")
        
        # Add user object to validated data
        data['user'] = user
        return data
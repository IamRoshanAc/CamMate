from django.contrib.auth.backends import BaseBackend
from api.models import User
from django.contrib.auth.hashers import check_password

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        """
        Authenticate the user based on email and password.

        Args:
            request: HTTP request object
            email: User's email address
            password: User's password
            **kwargs: Additional optional arguments (like for other backends)

        Returns:
            user (User object) if authentication is successful, else None
        """
        # Ensure that email and password are provided
        if not email or not password:
            return None  # Missing email or password, authentication fails

        try:
            # Retrieve user by email
            user = User.objects.get(email=email)

            # Validate the password using the user's check_password method
            if user.check_password(password) and user.is_active:
                return user  # Authentication successful if password matches and user is active
            else:
                return None  # Either password doesn't match or user is inactive
        except User.DoesNotExist:
            return None  # User does not exist with the provided email

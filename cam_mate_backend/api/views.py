from rest_framework import status
from django.http import StreamingHttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from api.models import BlacklistedToken
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
import cv2


RTSP_URL = "rtsp://admin:Dead_6533@192.168.1.64:554/Streaming/Channels/101"

def generate_frames():
    cap = cv2.VideoCapture(RTSP_URL)
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' +frame_bytes + b'\r\n' )
            

class VideoStreamAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return StreamingHttpResponse(generate_frames(), content_type = 'multipart/x-mixed-replace; boundary = frame')


@api_view(['GET'])
def video_feed(request):
    return StreamingHttpResponse(generate_frames(), content_type = 'multipart/x-mixed-replace; boundary = frame')

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid credentials'
            }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"detail": "Logout failed. Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user  
        return Response({
            'username': user.username, 
            'email': user.email
        })
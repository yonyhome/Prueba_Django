from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.view import APIview
from rest_framework import status

class UserAPI(APIview):
    def post(self, request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, statu = status.HTTP_400_BAD_REQUEST)

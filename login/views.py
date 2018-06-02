from django.contrib.auth.models import User
from rest_framework import viewsets
from . serializers import UserSerializer, LoginUserSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer



class UserLoginApiView(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginUserSerializer

    def post(self , request, *args, **kwargs):
        data = request.data
        serializer = LoginUserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.error, status=HTTP_400_BAD_REQUEST)

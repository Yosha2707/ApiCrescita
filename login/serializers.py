from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.serializers import CharField, EmailField
from django.db.models import Q
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.response import Response

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password':{'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        print(token.key)
        return user

class LoginUserSerializer(serializers.HyperlinkedModelSerializer):
    username = CharField(required=False, allow_blank=True)
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password':{'write_only':True}}

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data["password"]
        if not username:
            raise serializers.ValidationError('UserName or Password Incorrect..!')
        user = User.objects.filter(
                Q(username=username)

            ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError('UserName or Password Incorrect..!')
        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError('UserName or Password Incorrect..!')

        
        return data

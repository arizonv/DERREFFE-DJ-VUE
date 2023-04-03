from rest_framework import serializers
from django.contrib.auth import authenticate
from api.models import User
from rest_framework.validators import UniqueValidator


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class listSerializer (serializers.ModelSerializer):
     class Meta:
         model = User
         fields = ("id","email","username","is_staff","is_active","date_joined")



class createUserSerializer (serializers.ModelSerializer):
    username = serializers.CharField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = User
        fields = ("name","username","email","password")


    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


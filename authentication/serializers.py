# Django and DRF imports
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# waning_moon_design imports
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']


class RegistrationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128,
        min_length=3,
        write_only=True
    )

    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    def get_token(self, obj):
        user = obj['user']

        if user and user.active:
            refresh = RefreshToken.for_user(user)
            return str(refresh.access_token)
        else:
            raise serializers.ValidationError('Invalid credentials')

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)

        if user and user.active:
            return {
                'user': user,
                'token': self.get_token({'user': user})
            }
        else:
            raise serializers.ValidationError('Invalid credentials')

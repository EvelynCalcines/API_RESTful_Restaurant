# Django and DRF imports
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

# waning_moon_design imports
from .models import User, Comment
from phone_case.models import ColorType, PhoneCase


class ListPhoneCaseSerializer(serializers.ModelSerializer):

    color = serializers.ChoiceField(choices=ColorType.choices, source='get_color_display')
    is_favorite = serializers.SerializerMethodField()
    favorites = serializers.SerializerMethodField()

    class Meta:
        model = PhoneCase
        exclude = ["created_at", "updated_at", "deleted_at", "active", "user"]

    def get_is_favorite(self, obj):
        return obj.is_favorite(self.context["request"].user)

    def get_favorites(self, obj):
        return obj.favorites()


class UserSerializer(serializers.ModelSerializer):

    favorites = ListPhoneCaseSerializer(many=True)

    class Meta:
        model = User
        exclude = ['password']


class UserLoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ["password"]


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "phone", "address"]


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
    user = UserLoginSerializer(read_only=True)

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


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"


class UpdateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("text",)

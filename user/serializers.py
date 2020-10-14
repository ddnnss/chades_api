from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from django.db import IntegrityError, transaction
from rest_framework import exceptions, serializers
from djoser.conf import settings
from .models import *


User = get_user_model()

class EarnedAchivesSerializer(serializers.ModelSerializer):
    # achives = serializers.SlugRelatedField(slug_field='id',read_only=True)
    class Meta:
        model = EarnedAchive
        fields = '__all__'

class AchivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achive
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    # avatar = serializers.CharField(source='get_avatar',read_only=True,required=False)
    avatar = serializers.SerializerMethodField()
    # bg_image = serializers.SerializerMethodField()
    earned_achives = EarnedAchivesSerializer(many=True,read_only=True,required=False)

    class Meta:
        model = User
        fields = [
            'id',
            'last_login',
            'date_joined',
            'avatar',
            'nickname',
            'name',
            'email',
            'score',
            'is_vip',
            'title',
            'expiry_time',
            'bg_image',
            'earned_achives',
            'avaiable_courses',
            'finished_courses',
            'progress_courses',



                  ]

    def get_avatar(self, obj):
        print(obj)
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.avatar.url)
        else:
            return '/avatar.png'
    def get_bg_image(self, obj):
        print(obj)
        if obj.avatar:
            return self.context['request'].build_absolute_uri(obj.bg_image.url)
        else:
            return ''



class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={"input_type": "password"}, write_only=True)

    default_error_messages = {
        "cannot_create_user": settings.CONSTANTS.messages.CANNOT_CREATE_USER_ERROR
    }

    class Meta:
        model = User
        fields = tuple(User.REQUIRED_FIELDS) + (
            settings.LOGIN_FIELD,
            User._meta.pk.name,
            "password",
            "name",
            "nickname",
            "promo",
        )

    def validate(self, attrs):
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs

    def create(self, validated_data):
        print(validated_data)
        try:
            user = self.perform_create(validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user

    def perform_create(self, validated_data):
        print('validated_data',validated_data)
        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            user.is_active = False
            user.save(update_fields=["is_active"])
            if settings.SEND_ACTIVATION_EMAIL:
                user.is_active = False
                user.save(update_fields=["is_active"])
        return user


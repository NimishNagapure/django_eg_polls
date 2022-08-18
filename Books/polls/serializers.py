from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Information, Poll, Choice, Vote

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         Token.objects.create(user=user)
#         return user


# class VoteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Vote
#         fields = '__all__'


# class ChoiceSerializer(serializers.ModelSerializer):
#     votes = VoteSerializer(many=True, read_only=True)

#     class Meta:
#         model = Choice
#         fields = '__all__'


# class PollSerializer(serializers.ModelSerializer):
#     choices = ChoiceSerializer(many=True, read_only=True, required=False)

#     class Meta:
#         model = Poll
#         fields = '__all__'

# class InformationSerializer(serializers.Serializer):

#     class Meta:
#         model = Information
#         fields = '__all__'

#     def create(self, validated_data):
#         return Information.objects.create(**validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ("first_name", "last_name", "adhar")
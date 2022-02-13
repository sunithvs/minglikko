from django.contrib.auth.models import User, Group

from rest_framework import serializers
from .models import Tokens

# first we define the serializers
ques = ['intelligence', 'strength',
        'beauty', 'charisma', 'wealth', 'will_help_poor',
        'religiousity', 'liberal']


class GetTokensSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    # priority_list = serializers.SerializerMethodField()

    class Meta:
        model = Tokens
        fields = [
            'id', 'user', 'intelligence', 'strength',
            'beauty', 'charisma', 'wealth', 'will_help_poor',
            'religiousity', 'liberal', 'total', 'priority_list'
        ]
        extra_kwargs = {
            'user': {'read_only': True},
            'total': {'read_only': True},
        }

    def get_total(self, obj):
        return obj.total


class GetTokensToOthersSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = Tokens
        fields = [
            'private_token', 'intelligence', 'strength',
            'beauty', 'charisma', 'wealth', 'will_help_poor',
            'religiousity', 'liberal', 'total'
        ]

        extra_kwargs = {
            'user': {'read_only': True},
            'total': {'read_only': True},
        }

    def get_total(self, obj):
        return obj.total


class UserSerializer(serializers.ModelSerializer):
    tokens = GetTokensSerializer(many=False, read_only=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', "first_name", "last_name", 'tokens',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)

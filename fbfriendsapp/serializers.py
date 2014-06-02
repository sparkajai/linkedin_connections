from django.contrib.auth.models import User, Group
from fbfriendsapp.models import LinkedinUserFriendsData
from rest_framework import serializers


class LinkedinSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkedinUserFriendsData
        fields = ('full_name', 'photo_url')
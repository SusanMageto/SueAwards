from rest_framework import serializers
from .models import *
from projects.models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

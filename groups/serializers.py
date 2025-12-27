from rest_framework import serializers
from .models import Group, Memberships

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class MembershipsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memberships
        fields = "__all__"
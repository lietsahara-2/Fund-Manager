from django.shortcuts import render
from .models import Memberships, Group
from .serializers import GroupSerializer, MembershipsSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import generics, viewsets

# Admin
class GroupModelViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser]

class MembershipsModelViewSet(viewsets.ModelViewSet):
    queryset = Memberships.objects.all()
    serializer_class = MembershipsSerializer
    permission_classes = [IsAdminUser]

#Users can only view
class GroupListAPIView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class MembershipsListAPIView(generics.ListAPIView):
    queryset = Memberships.objects.all()
    serializer_class = MembershipsSerializer
    permission_classes = [IsAuthenticated]
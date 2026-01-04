from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import User
from .serializers import UserSerializer, AdminUserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser 

# Create your views here.
class AdminUserModelViewSet(viewsets.ModelViewSet):#all CRUD operations
    queryset = User.objects.all()
    serializer_class = AdminUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  #only admin users can access

#normal users can only view and update their own details
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserPartialUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user #user can only update their own details
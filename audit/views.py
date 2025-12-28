from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
#now importing from the necessary files
from .models import Audit
from .serializers import AuditSerializer


# Create your views here.
class AuditModelViewSet(viewsets.ModelViewSet):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class AuditListAPIView(generics.ListAPIView):
    queryset = Audit.objects.all()
    serializer_class = AuditSerializer
    permission_classes = [IsAuthenticated]

from django.urls import path
from .views import AuditModelViewSet, AuditListAPIView
from rest_framework.routers import DefaultRouter

urlpatterns=[

    path('audit/', AuditListAPIView.as_view(), name='audit-list'),
]
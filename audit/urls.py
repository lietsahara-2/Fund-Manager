from django.urls import path
from .views import AuditModelViewSet, AuditListAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'auditadmin', AuditModelViewSet, basename='auditadmin')

urlpatterns=[

    path('listaudit/', AuditListAPIView.as_view(), name='audit-list'),
]

urlpatterns += router.urls
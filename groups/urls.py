from django.urls import path
from .views import GroupModelViewSet, MembershipsModelViewSet, GroupListAPIView, MembershipsListAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'groupadmin', GroupModelViewSet, basename='groupadmin')
router.register(r'membershipadmin', MembershipsModelViewSet, basename='membershipadmin') #basename optional if queryset is present and required otherwise

urlpatterns=[
    path('listgroups/', GroupListAPIView.as_view(), name='group-list'),
    path('listmemberships/', MembershipsListAPIView.as_view(), name='membership-list'),
]

urlpatterns += router.urls
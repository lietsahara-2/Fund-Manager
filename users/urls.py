from django.urls import path
from .views import AdminUserModelViewSet, UserListAPIView, UserPartialUpdateAPIView
from rest_framework.routers import DefaultRouter #importing router for viewsets

#manual mapping ie. as_views({'get':'list', 'post': 'create'}) not optimal for ViewSet routers are better
router = DefaultRouter()
router.register(r'adminuser', AdminUserModelViewSet, basename='adminuser') #registering the viewset with the router
#adminuser/<int:pk> -not necessary as router handles it

urlpatterns=[
    path('listuser/',  UserListAPIView.as_view(), name='user-list'),
    path('update/', UserPartialUpdateAPIView.as_view(), name='user-update'),
] #defining urlpatterns for the views

urlpatterns += router.urls #adding the router urls to urlpatterns



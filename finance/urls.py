from django.urls import path
from .views import ContributionsModelViewSet, ContributionsListCreateAPIView, LoansModelViewSet, LoansListCreateAPIView, TransactionsListAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contributionsadmin', ContributionsModelViewSet, basename='contributionsadmin')
router.register(r'loansadmin', LoansModelViewSet, basename='loansadmin')

urlpatterns=[
    path('contributions/', ContributionsListCreateAPIView.as_view(), name='contribution-list'),
    path('loans/', LoansListCreateAPIView.as_view(), name='loan-list'),
    path('transactions/', TransactionsListAPIView.as_view(), name='transaction-list'),
]   

urlpatterns += router.urls
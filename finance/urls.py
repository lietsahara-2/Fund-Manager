from django.urls import path
from .views import ContributionsModelViewSet, ContributionsListAPIView, LoansModelViewSet, LoansListAPIView, TransactionsModelViewSet, TransactionsListAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contibutionsadmin', ContributionsModelViewSet, basename='contributionsadmin')
router.register(r'loansadmin', LoansModelViewSet, basename='loansadmin')
router.register(r'transactionsadmin', TransactionsModelViewSet, basename='transactionsadmin')

urlpatterns=[
    path('listcontributions/', ContributionsListAPIView.as_view(), name='contribution-list'),
    path('listloans/', LoansListAPIView.as_view(), name='loan-list'),
    path('listtransactions/', TransactionsListAPIView.as_view(), name='transaction-list'),
]   

urlpatterns += router.urls
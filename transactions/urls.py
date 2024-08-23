from django.urls import path
from .views import TransactionReportView, DepositMoneyView

urlpatterns = [
    path('report/', TransactionReportView.as_view(), name='transaction_report'),
    path('deposit/', DepositMoneyView.as_view(), name='deposit_money'),
]

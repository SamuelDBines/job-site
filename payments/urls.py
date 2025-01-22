from django.urls import path
from . import views

urlpatterns = [
    path("payments/", views.PaymentListView.as_view(), name="payment_list"),
    path("payments/<int:job_id>/", views.ProcessPaymentView.as_view(), name="process_payment"),
]
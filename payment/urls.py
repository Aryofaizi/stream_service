from django.urls import path
from . import views


urlpatterns = [
    path("<int:pk>/", view=views.payment_request, name="payment_request"),
    path("verify/", view=views.payment_verify, name="payment_verify"),
]








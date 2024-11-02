from django.urls import path
from . import views

urlpatterns = [
    path("notification/mark_all_as_read/", views.mark_all_notifications_as_read,name="mark_all_as_read"),
    path("share-link/<int:pk>/", views.GenerateShareableLink.as_view(), name="generate_shareable_link"),
]

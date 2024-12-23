from django.contrib import admin
from django.urls import path, include
from django.urls import path
from .views import MessageReceiverView

urlpatterns = [
    path('receive-message/', MessageReceiverView.as_view(), name='receive-message'),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/messaging/", include("messaging.urls")),  # Include messaging app URLs
]

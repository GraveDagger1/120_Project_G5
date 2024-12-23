from django.urls import path
from .views import SendMessageView, ReceiveMessageView

urlpatterns = [
    path('send/', SendMessageView.as_view(), name='send_message'),
    path('receive/<int:pk>/', ReceiveMessageView.as_view(), name='receive_message'),
]

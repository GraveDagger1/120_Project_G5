from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Message
from .serializers import MessageSerializer
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken

# Replace with your generated key
KEY = b'WkJyLAuU2L9UvVnpWpDAtEthIx_ExhC6GfFiVu01Ruk='
cipher_suite = Fernet(KEY)

class SendMessageView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            # Encrypt the message content before saving
            encrypted_content = cipher_suite.encrypt(serializer.validated_data['content'].encode())
            serializer.save(content=encrypted_content.decode())  # Save encrypted content
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReceiveMessageView(APIView):
    def get(self, request, pk):
        try:
            message = Message.objects.get(pk=pk)
            # Decrypt the message content
            try:
                decrypted_content = cipher_suite.decrypt(message.content.encode()).decode()
                message.content = decrypted_content  # Replace encrypted content with decrypted content
            except InvalidToken:
                return Response(
                    {'error': 'Failed to decrypt the message content. Invalid token.'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            serializer = MessageSerializer(message)
            return Response(serializer.data)
        except Message.DoesNotExist:
            return Response(
                {'error': 'Message not found'},
                status=status.HTTP_404_NOT_FOUND
            )
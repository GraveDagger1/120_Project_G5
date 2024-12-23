from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MessageReceiverView(APIView):
    def post(self, request):
        # Decrypt or process incoming data
        encrypted_message = request.data.get('message')
        # Process decrypted_message here...
        return Response({"status": "Message received"}, status=status.HTTP_200_OK)

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework.permissions import IsAuthenticated

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SellerDashboard(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_seller:
            return Response({"msg": "Seller Dashboard"})
        return Response({"msg": "Not a seller"}, status=403)
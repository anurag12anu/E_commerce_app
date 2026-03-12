from django.test import TestCase

# Create your tests here.
from .models import Order
from .serializers import OrderSerializer


class OrderCreateView(APIView):

    def post(self, request):

        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
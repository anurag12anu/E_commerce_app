from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer


class OrderCreateView(APIView):

    def post(self, request):

        serializer = OrderSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save(user=request.user)

            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)
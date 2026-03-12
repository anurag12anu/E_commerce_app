from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer


class CategoryListCreateView(APIView):

    def get(self, request):
        categories = Category.objects.filter(parent=None)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    class SubCategoryView(APIView):

     def get(self, request, category_id):

        subcategories = Category.objects.filter(parent_id=category_id)

        serializer = CategorySerializer(subcategories, many=True)

        return Response(serializer.data)
    
    
from .models import Product
from .serializers import ProductSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductListView(APIView):

    def get(self, request):
        category_id = request.GET.get('category')

        if category_id:
            products = Product.objects.filter(category_id=category_id)
        else:
            products = Product.objects.all()

        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)
    
class ProductDetailView(APIView):

    def get(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

        serializer = ProductSerializer(product)
        return Response(serializer.data)
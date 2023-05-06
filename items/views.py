from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import pagination
from rest_framework import generics, mixins
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from .models import Category, Product, Order, User
from .permissions import IsAuthorOrAllowAny
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorOrAllowAny]


@api_view(['GET'])
def category_detail(request, name):
    product = Category.objects.get(name=name)
    serializer = CategorySerializer(product)
    return Response(serializer.data)


class TweetPagination(pagination.PageNumberPagination):
    page_size = 2


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorOrAllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', ]
    ordering_fields = ['created', ]


@api_view(['GET'])
def phone_detail(request, name):
    product = Product.objects.get(name=name)
    serializer = ProductSerializer(product)
    if serializer:
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def product_detail(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthorOrAllowAny]


@api_view(['GET'])
def order_detail(request, name):
    product = Order.objects.get(name=name)
    serializer = OrderSerializer(product)
    if serializer:
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

#
# class UserRegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegisterSerializer
#
#
# def create(self, request, *args, **kwargs):
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = serializer.save()
#     token, created = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key})

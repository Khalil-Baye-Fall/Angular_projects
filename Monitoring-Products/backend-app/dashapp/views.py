from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken


from .models import Products
from .serializers import ProductSerializer, UserSerializer, RegisterSerializer
from .user_processing_auth import validate_email, validate_username


# registration process........
@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        data = {}
        email = request.data.get('email', '0').lower()
        if validate_email(email) is not None:
            data['error_message'] = 'That email is already in use.'
            return Response(data)

        username = request.data.get('username', '0')
        if validate_username(username) is not None:
            data['error_message'] = 'That username is already in use.'
            return Response(data)

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'successfully registered new user.'
            data['email'] = account.email
            data['username'] = account.username
            data['pk'] = account.pk
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data['response'])
    
    
# Login process...................
class CustomAuthToken(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            'email': user.email
        })
        

# CRUD process for products.........................
@api_view(['GET'])
def getProducts(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@login_required(login_url='/login')
@api_view(['GET'])
def getOneProduct(request, pk):
    products = Products.objects.get(id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@login_required(login_url='/login')
@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@login_required(login_url='/login')
@api_view(['POST'])
def updateProduct(request, pk):
    product = Products.objects.get(id=pk)
    serializer = ProductSerializer(instance=product, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@login_required(login_url='/login')
@api_view(['DELETE'])
def deletProduct(request, pk):
    product = Products.objects.get(id=pk)
    product.delete()
    
    return Response("Product was delete.", status=status.HTTP_204_NO_CONTENT)
from django.urls import path
from .views import getProducts, getOneProduct, createProduct, updateProduct, deletProduct, CustomAuthToken, registration_view

urlpatterns = [
    path('login/auth/token/', CustomAuthToken.as_view(), name="login"),
    path('register/', registration_view, name='register'),
    path('', getProducts, name="get-products"),
    path('products/', getProducts, name="get-products"),
    path('product/<str:pk>/', getOneProduct, name="single-product"),
    path('create-product/', createProduct, name="createProduct"),
    path('update-product/<str:pk>/', updateProduct, name="updateProduct"),
    path('delete-product/<str:pk>/', deletProduct, name="deleteProduct"),
]

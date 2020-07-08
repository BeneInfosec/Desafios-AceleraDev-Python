from django.urls import path
from api import views

urlpatterns = [
    path('lambda/', views.lambda_function),
]

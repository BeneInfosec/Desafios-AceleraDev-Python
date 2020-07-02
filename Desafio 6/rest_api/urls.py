from django.urls import include, path

from rest_framework import routers

from rest_api import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductApiViewSet) #rota da API de produtos

urlpatterns = [
    path('', include(router.urls)), 
    path('categories/', views.CategoryListOnlyAPIView.as_view())
]

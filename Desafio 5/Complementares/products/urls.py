"""ecomm URL Configuration

    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/2.2/topics/http/urls/
    Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from products import views # pegar os views do proprio app

urlpatterns = [
    path('list', views.list_products, name='list'),
    path('create', views.create_product, name='create'),
    #path('delete/<int:product_id>', views.delete_product, name='delete'),
    #path('update/<int:product_id>', views.update_product, name='update')
]

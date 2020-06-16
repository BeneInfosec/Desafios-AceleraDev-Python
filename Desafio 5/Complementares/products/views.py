from django.shortcuts import render

from products.models import Product
# Create your views here.
def list_products(request): #Sempre vai pegar uma request como argumento
    products =  Product.objects.all()

    context = { #Sempre é um dicionário
        'products' : products,
        'products_empty' : []
    }

    return render(request, 'products/list.html', context = context) # Ele reconhece a pasta template, não precisando especificar
#Como ele vai responder uma requisição.
#Ler o produto do banco de dados, e depois extrair os valoares da leitura e depois montar um template
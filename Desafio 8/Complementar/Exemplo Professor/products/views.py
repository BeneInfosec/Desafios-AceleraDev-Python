from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page
from django.conf import settings

from products.models import Product
from products.forms import ProductModelForm # from pasta import classe

# Create your views here.
@cache_page(25) #settings.CACHE_TTL
def list_products(request): #Sempre vai pegar uma request como argumento
    products =  Product.objects.all()

    context = { #Sempre é um dicionário
        'products' : products,
        'products_empty' : []
    }

    return render(request, 'products/list.html', context = context) # Ele reconhece a pasta template, não precisando especificar
#Como ele vai responder uma requisição.
#Ler o produto do banco de dados, e depois extrair os valoares da leitura e depois montar um template

def create_product(request):
    if request.method == 'POST':
        #Salvar form
        form = ProductModelForm(request.POST)
        if form.is_valid():
            #True -> é valido
            form.save()
            return redirect('products:list') #Retorna para a lista de produtos
    else: #Não valido
        #Get form
        form = ProductModelForm()

    context = { #Sempre é um dicionário
        'form' : form
    }
    return render(request, 'products/create.html', context = context)

def delete_product(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('products:list')

def update_product(request, product_id):
    product = Product.objects.get(pk=product_id)

    if request.method == 'POST':
        form = ProductModelForm(data=request.POST, instance=product)
        if form.is_valid():
            #True -> é valido
            form.save()
            return redirect('products:list')
    else: #Não valido
        #Get form
        form = ProductModelForm(instance=product) #id = instancia

    context = { #Sempre é um dicionário
        'form' : form
    }
    return render(request, 'products/update.html', context = context)

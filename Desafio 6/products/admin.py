from django.contrib import admin
from products.models import Product, Category
from django.utils.html import format_html
from django.urls import reverse
# Register your models here.


class CategoryModelAdmin(admin.ModelAdmin):
    def products(self,obj):
        #admin:APP-NAME_MODEL-NAME_changelist
        #APP-NAME = nome definido no apps.py
        href = reverse('admin:products_product_changelist') + f'?category={obj.pk}'
        return format_html(f'<a href="{href}">{obj.products.count()}</a>')
        #Em models.py foi definido na classe Products uma relação de Category com Products

    products.short_description = 'Produtos da Categoria'

    list_display = ('name', 'description', 'products')

class ProductModelAdmin(admin.ModelAdmin):
    def queryset(self, request, queryset):
        category =  request.GET.get('category')
        if category:
            return queryset.filter(category__pk=category)

        return queryset

    list_display = ('name', 'formatted_price', 'description', 'link_category')

    def formatted_price(self,obj):
        return f'{obj.price} R$'

    formatted_price.short_description = 'Preço'

    def link_category(self,obj):
        href = reverse('admin:products_category_change', args=(obj.category.pk,))
        return format_html(f'<a href="{href}">{obj.category.name}</a>')

    link_category.short_description = 'Categoria'



admin.site.register(Product, ProductModelAdmin)
#Configurar a interface da admin
admin.site.register(Category, CategoryModelAdmin)

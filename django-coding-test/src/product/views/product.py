from typing import Any
from django.db.models.query import QuerySet
from django.views import generic
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from product.models import Product, ProductRow
import json
from django.core.paginator import Paginator

from product.models import Variant






class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
    
class SearchByTitleView(ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        try:
            query = self.request.GET.get('title')  # Get the search query from the request
            if query:
                return Product.objects.filter(title__icontains=query)  # Searching by title (case-insensitive)
            else:
                return Product.objects.all()
        except:
            pass


class ShowItem(TemplateView):
    template_name='products/list.html'
    model = ProductRow

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        with open('django_coding_test.json','r') as product_file:
            json_data_temp = product_file.read()
        data = json.loads(json_data_temp)
        ProductRow.objects.all().delete()
        for item in data:
            model_name = item['model']
            if model_name == 'product.product':
                title_temp=item['fields']['title'],
                title = str(title_temp).replace("('",''),
                sku=item['fields']['sku'],
                description_temp=item['fields']['description'],
                description_temp=str(description_temp).strip("('')"),
                created_at_temp=item['fields']['created_at'],
                created_at_temp=str(created_at_temp).strip("('')"),
                updated_at=item['fields']['updated_at']

                for items in data:
                    model_name = items['model']
                    if model_name =='product.productvariantprice':
                        product_variant_one_temp=items['fields']['product_variant_one']
                        product_varient_two_temp=items['fields']['product_variant_two']
                        price_temp =items['fields']['price']
                        stock_temp=items['fields']['stock']

                for items in data:
                    model_name = items['model']
                    if model_name=='product.productvariant':
                        model_varient_id = items['pk']
                        if model_varient_id==product_variant_one_temp:
                            varient_title1_temp = items['fields']['variant_title']

                for items in data:
                    model_name = items['model']
                    if model_name=='product.productvariant':
                        model_varient_id = items['pk']
                        if model_varient_id==product_varient_two_temp:
                            varient_title2_temp = items['fields']['variant_title']
                productRow = ProductRow(
                    title = str(title_temp).replace("('",'').replace("',)",''),
                    description = str(description_temp).replace("(",'').replace("',",'').replace('"', '').replace(",)",''),
                    created_at = str(created_at_temp).replace('(','').replace('"','').replace(",)",'').replace("',",'').replace('"',''),
                    product_variant_one = str(product_variant_one_temp),
                    product_variant_two = str(product_varient_two_temp),
                    varient_title1 = str(varient_title1_temp),
                    varient_title2 = str(varient_title2_temp),
                    price = str(price_temp),
                    stock = str(stock_temp)
                )
                productRow.save()

                # product = Product(
                #     title=item['fields']['title'],
                #     sku=item['fields']['sku'],
                #     description=item['fields']['description'],
                #     created_at=item['fields']['created_at'],
                #     updated_at=item['fields']['updated_at']
                # )

        
        
        

        
        products = ProductRow.objects.all()
        try:
            title = self.request.GET.get('title')
            if len(title) != 0:
                products = products.objects.filter(title__icontains = title)
            else:
                products = ProductRow.objects.all()
        except:
            pass
        paginator =Paginator(products,2)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj']=page_obj
        return context
    



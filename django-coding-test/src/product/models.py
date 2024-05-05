from typing import Any
from django.db import models
from config.g_model import TimeStampMixin
from django.shortcuts import render


# Create your models here.
class Variant(TimeStampMixin):
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)


class Product(TimeStampMixin):
    title = models.CharField(max_length=255)
    sku = models.SlugField(max_length=255, unique=True)
    description = models.TextField()

    # def __str__(self):
    #     return self.title
    # def Product(self, title, sku, description):
    #     self.title = title
    #     self.sku = sku
    #     self.description = description


class ProductImage(TimeStampMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField()


class ProductVariant(TimeStampMixin):
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductVariantPrice(TimeStampMixin):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                              related_name='product_variant_three')
    price = models.FloatField()
    stock = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class ProductRow(TimeStampMixin):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.CharField(max_length=255)
    product_variant_one = models.CharField(max_length=255)
    product_variant_two = models.CharField(max_length=255)
    varient_title1 = models.CharField(max_length=255)
    varient_title2 = models.CharField(max_length=255)
    price =  models.CharField(max_length=255)
    stock = models.CharField(max_length=255)

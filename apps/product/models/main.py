from django.db import models

from apps.core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(BaseModel):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="products",
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="images",
    )

    image = models.ImageField(upload_to="products/")
    alt_text = models.CharField(max_length=255, blank=True)

    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return f"Image for {self.product}"
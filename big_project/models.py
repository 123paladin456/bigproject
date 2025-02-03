from django.db import models
from django.core.validators import (MaxValueValidator, MinValueValidator)
from django.urls import reverse


# Create your models here.




# class Event_object(models.Model):
#     name = models.TextField(max_length=30)
#     description = models.TextField()
#     image = models.ImageField()
#     price = models.DecimalField(max_digits=7, decimal_places=0)
#
# class Programs(models.Model):
#     name = models.TextField(max_length=30)
#     description = models.TextField()
#     objects = models.ManyToManyField(Event_object)
#     counts = models.PositiveIntegerField(default=1)







class Category(models.Model):
    name = models.CharField("Категория", max_length=250, db_index=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="child", blank=True, null=True)
    slug = models.SlugField("URL", max_length=250, unique=True, null=False, editable=True)
    created_date = models.DateTimeField("Дата создания", auto_now_add=True)






    class Meta:
        unique_together = (["slug", "parent"])
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:category-list", args=[str(self.slug)])




class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    title = models.CharField("Название", max_length=250, db_index=True)
    description = models.TextField("Описание", db_index=True)
    slug = models.SlugField("URL", max_length=250, unique=True, null=False, editable=True)
    image = models.ImageField("Изображение", upload_to="images/products/%Y/%m", default="products/products/default.jpg")
    price = models.DecimalField(max_digits=7, decimal_places=2, default=99.99)
    available = models.BooleanField("Наличие", default=True, db_index=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField("Дата обновления",auto_now_add=True, db_index=True)
    discount = models.IntegerField("Скидка", default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])




    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["-created_at"]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("shop:products-detail", args=[str(self.slug)])




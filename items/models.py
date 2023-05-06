from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()



class Category(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categoryes')
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['user', 'category']

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=20, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='products')
    quantity = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} ({self.quantity} {self.name}"
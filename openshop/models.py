from django.db import models
import uuid

class OpenShop (models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=30)
    sku = models.TextField()
    description = models.TextField()
    shop = models.TextField()
    location = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField()
    category = models.TextField()
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    picture = models.TextField()
    is_delete = models.BooleanField(default=False)
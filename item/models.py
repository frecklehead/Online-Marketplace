from django.db import models

# Create your models here.
#defining a model named Category inherited form models.Model with name field (charfield with max length of 255)
class Category(models.Model):
  name=models.CharField(max_length=255)
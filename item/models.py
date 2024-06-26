from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#defining a model named Category inherited form models.Model with name field (charfield with max length of 255)
class Category(models.Model):
  name=models.CharField(max_length=255)
  class Meta:
    ordering =('name',)
    verbose_name_plural='Categories'
  def __str__(self):
     return self.name
class Item(models.Model):

  category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
  name=models.CharField(max_length=255)
  description=models.TextField(blank=True,null=True)
  price=models.FloatField()
  image=models.ImageField(upload_to='item-images',blank=True,null=True)
  is_sold=models.BooleanField(default=False)
  created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
  created_at=models.DateTimeField(auto_now_add=True)
  # stock_quantity = models.PositiveIntegerField(default=0)

  
  def __str__(self):
    return self.name;
    
  
  
from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.IntegerField(null=True)
    email=models.EmailField(null=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True )
    def __str__(self):
        return self.name
class tag(models.Model):
    name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
class Products(models.Model):
    CATEGORY=(
        ('indoor','indoor'),
        ('outdoor','outdoor'),
    )
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
    description=models.CharField(max_length=200,null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True )
    tags=models.ManyToManyField(tag)
    def __str__(self):
        return self.name

class order(models.Model):
    STATUS=(
        ('pending','pending'),
        ('out for delivery','out for delivery'),
        ('delivered','delivered'),
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(Products,null=True,on_delete=models.SET_NULL)
    date_created=models.DateTimeField(auto_now_add=True,null=True )
    status=models.CharField(max_length=100,choices=STATUS)
    def __str__(self):
        return self.product.name
class expected(models.Model):
    ans1=models.CharField(max_length=100,blank=True)
class testcase(models.Model):
    test_input=models.CharField(max_length=100)
    expected_output=models.ForeignKey(expected,on_delete=models.CASCADE)

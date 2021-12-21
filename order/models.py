from django.db import models

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Menuitem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # category = models.ManyToManyField(category, related_name='item')
    category = models.ForeignKey(category,on_delete=models.PROTECT)

    # category = models.TextField()
    def __str__(self):
        return self.name


class ordernow(models.Model):
    order_creat= models.DateTimeField(True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    item = models.ManyToManyField('Menuitem', related_name='order',blank=True)
    def __str__(self):
        return self.order_creat

# class contactus(models.Model):
#     email = models.EmailField()
#     name = models.CharField(max_length=20)
#     message = models.CharField(max_length=20)

# class contactme(models.Model):
#     email = models.EmailField()
#     name = models.CharField(max_length=20)
#     message = models.CharField(max_length=20)

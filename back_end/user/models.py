from django.db import models

# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField("status", default=True)

    class Meta:
        abstract = True

class Customer(Base):

    name = models.CharField('Customer name', help_text='Customer name', max_length=50)
    email = models.EmailField('Customer email', help_text='Customer email')
    password = models.CharField('Customer password', help_text='Customer pssword', max_length=10)

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return self.name


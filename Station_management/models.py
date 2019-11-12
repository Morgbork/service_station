from django.db import models
from django.shortcuts import reverse
from phonenumber_field.modelfields import PhoneNumberField
from .validators import name_validator, make_validator, year_validator, vin_validator,order_amount_validator, order_date_validator



class ClientManager(models.Manager):
    def addClient(self, first_name, last_name, date_of_birth, address, phone, email):
        client = self.create(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, address=address, phone=phone, email=email)
        return client

class Clients(models.Model): 
    first_name = models.CharField(max_length=25, validators=[name_validator])
    last_name = models.CharField(max_length = 25, validators=[name_validator])
    date_of_birth = models.DateField()
    address = models.CharField(max_length = 150)
    phone = PhoneNumberField(unique=True) 
    email = models.EmailField(unique=True)

    objects = ClientManager()

    class Meta: 
        ordering = ['last_name', 'first_name']
        verbose_name_plural = 'Clients'

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_absolute_url(self):
        from .views import clients_search
        return reverse('Station_management:client_card', args=[self.first_name, self.id])


class Cars(models.Model):
    owner = models.ForeignKey('Clients', related_query_name = 'Cars', on_delete = models.CASCADE) 
    make = models.CharField(max_length = 50, validators=[make_validator])
    car_model = models.CharField(max_length = 70)
    year = models.IntegerField(validators = [year_validator]) 
    vin = models.CharField(max_length = 17, unique=True, validators=[vin_validator]) 

    class Meta: 
        ordering = ['make', 'car_model']
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.vin


class Orders(models.Model): 
    ORDER_STATUSES = [
        ('COMP', 'Completed'),
        ('INPR', 'In Progress'),
        ('CANC', 'Cancelled')
    ]
    car = models.ForeignKey('Cars', related_name = 'Orders', on_delete = models.CASCADE)
    date = models.DateField(validators=[order_date_validator])
    order_amount = models.IntegerField(validators=[order_amount_validator])
    order_status = models.CharField(max_length = 1, choices = ORDER_STATUSES)

    class Meta: 
        ordering = ['-date']
        verbose_name_plural = 'Orders'

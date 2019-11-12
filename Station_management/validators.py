from django.core.validators import RegexValidator, EmailValidator
from django.core.exceptions import ValidationError
from datetime import datetime, date

name_validator = RegexValidator(regex = r'[A-Za-z]', message = "Please use only latin letters.")

make_validator = RegexValidator(regex = r'[A-Za-z]', message = "Please use only latin letters.")

def year_validator(value):
    if value < 1885: 
        raise ValidationError('Invalid date.')
    elif value > datetime.now().year:
        raise ValidationError('Invalid date.')

def vin_validator(value):
    if len(value) != 17: 
        raise ValidationError('VIN must consist of 17 characters.')    

def order_date_validator(value):
    if value > datetime.date(datetime.today()):
        raise ValidationError('Invalid date.')

def order_amount_validator(value):
    if not 0 <= value <= 10000:
        raise ValidationError('Order amount must be not less than 0 USD and not greater than 10,000 USD.')
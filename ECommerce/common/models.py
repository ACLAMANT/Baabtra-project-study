from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=50)
    email_id = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    password = models.CharField(max_length=50)

    class Meta:
        db_table = 'customer_tb'

class Seller(models.Model):
    s_name = models.CharField(max_length = 50)
    s_account_number = models.BigIntegerField()
    s_company_name = models.CharField(max_length=50)
    s_account_holder_name = models.CharField(max_length=50)
    s_ifsc_code = models.CharField(max_length=50)
    s_branch_name = models.CharField(max_length=50)
    s_email_id = models.CharField(max_length=50)
    s_mobile_number = models.BigIntegerField()
    s_address = models.CharField(max_length=200)
    s_user_name = models.CharField(max_length=50)
    s_password = models.IntegerField()
    s_image = models.ImageField(upload_to='seller/')

    class Meta:
        db_table = 'seller_tb'
    





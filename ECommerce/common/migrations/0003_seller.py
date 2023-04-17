# Generated by Django 4.1.7 on 2023-04-08 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_customer_address_alter_customer_email_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=50)),
                ('s_account_number', models.BigIntegerField()),
                ('s_company_name', models.CharField(max_length=50)),
                ('s_account_holder_name', models.CharField(max_length=50)),
                ('s_ifsc_code', models.CharField(max_length=50)),
                ('s_branch_name', models.CharField(max_length=50)),
                ('s_email_id', models.CharField(max_length=50)),
                ('s_mobile_number', models.BigIntegerField()),
                ('s_address', models.CharField(max_length=200)),
                ('s_user_name', models.CharField(max_length=50)),
                ('s_password', models.IntegerField()),
                ('s_image', models.ImageField(upload_to='seller/')),
            ],
        ),
    ]
# Generated by Django 5.0.1 on 2024-02-24 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_email_customer_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Frist_Name',
            new_name='frist_name',
        ),
    ]

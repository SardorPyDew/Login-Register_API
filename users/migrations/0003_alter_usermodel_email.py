# Generated by Django 5.0.6 on 2024-07-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_usermodel_email_alter_usermodel_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]

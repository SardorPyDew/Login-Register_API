# Generated by Django 5.0.6 on 2024-07-03 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_usermodel_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]

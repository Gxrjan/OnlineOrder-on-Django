# Generated by Django 2.0.5 on 2018-06-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_auto_20180614_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='outputOrg',
            field=models.CharField(error_messages={'unique': 'Шаблон с таким названием уже существует'}, max_length=255, unique=True),
        ),
    ]
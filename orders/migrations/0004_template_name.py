# Generated by Django 2.0.5 on 2018-05-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='name',
            field=models.CharField(default='blank', max_length=1000),
        ),
    ]

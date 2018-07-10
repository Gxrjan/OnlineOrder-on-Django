# Generated by Django 2.0.5 on 2018-06-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20180605_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cargoDescripton',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='comments',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='template',
            name='name',
            field=models.CharField(max_length=1000),
        ),
    ]
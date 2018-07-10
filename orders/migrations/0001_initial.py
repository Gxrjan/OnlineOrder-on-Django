# Generated by Django 2.0.5 on 2018-05-21 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(verbose_name='date')),
                ('outputOrg', models.CharField(max_length=1000)),
                ('outputContact', models.CharField(max_length=1000)),
                ('outputNumber', models.CharField(max_length=1000)),
                ('outputAdress', models.CharField(max_length=1000)),
                ('inputOrg', models.CharField(max_length=1000)),
                ('inputContact', models.CharField(max_length=1000)),
                ('inputNumber', models.CharField(max_length=1000)),
                ('inputAdress', models.CharField(max_length=1000)),
                ('cargoDescripton', models.CharField(max_length=1000)),
                ('comments', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('inside_number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('uid', models.CharField(max_length=255)),
                ('pwd', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.User'),
        ),
    ]

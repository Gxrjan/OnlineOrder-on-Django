from django.db import models
try:
	from django.contrib.auth import get_user_model
except ImportError:
	from django.contrib.auth.models import User
else:
	User=get_user_model()
import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


# class User(models.Model):
# 	first_name=models.CharField(max_length=255)
# 	last_name=models.CharField(max_length=255)
# 	father_name=models.CharField(max_length=255)
# 	phone_number=models.CharField(max_length=255)
# 	inside_number=models.CharField(max_length=255)
# 	email=models.EmailField(max_length=254)
# 	uid=models.CharField(max_length=255)
# 	pwd=models.CharField(max_length=255)
# 	def __str__(self):
# 		return self.last_name+" "+self.first_name+" "+self.father_name

class Order(models.Model):
	time=models.DateTimeField('date')
	user=models.ForeignKey(User, on_delete=models.CASCADE)
	outputOrg=models.CharField(max_length=1000)
	outputContact=models.CharField(max_length=1000)
	outputNumber=models.CharField(max_length=1000)
	outputAdress=models.CharField(max_length=1000)
	inputOrg=models.CharField(max_length=1000)
	inputContact=models.CharField(max_length=1000)
	inputNumber=models.CharField(max_length=1000)
	inputAdress=models.CharField(max_length=1000)
	cargoDescripton=models.CharField(max_length=1000,null=True,blank=True)
	weight=models.IntegerField(null=True,blank=True)
	comments=models.CharField(max_length=2000,null=True,blank=True)
	attach1=models.FileField(null=True, blank=True);
	attach2=models.FileField(null=True, blank=True);
	attach3=models.FileField(null=True, blank=True);
	attach4=models.FileField(null=True, blank=True);
	def __str__(self):
		return "Order from "+self.outputAdress+" to "+self.inputAdress

class Template(models.Model):
	name=models.CharField(max_length=255,unique=True,error_messages={'unique': 'Шаблон с таким названием уже существует'})
	organization=models.CharField(max_length=1000)
	contact=models.CharField(max_length=1000)
	number=models.CharField(max_length=1000)
	adress=models.CharField(max_length=1000)
	def __str__(self):
		return self.name

class Notification(models.Model):
	order=models.ForeignKey(Order, on_delete=models.CASCADE)
	# def __str__(self):
	# 	return self.id

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=500)
	last_name = models.CharField(max_length=500)
	family_name = models.CharField(max_length=500)
	phone_number = models.CharField(max_length=500)
	inside_number = models.CharField(max_length=500)
	email = models.EmailField(max_length=500)

	def __str__(self):
		return self.user.username+ "'s profile"		

	# @receiver(post_save, sender=User)
	# def create_user_profile(sender, instance, created, **kwargs):
	# 	if created:
	# 		Profile.objects.create(user=instance)

	# @receiver(post_save, sender=User)
	# def save_user_profile(sender, instance, **kwargs):
	# 	instance.profile.save()

	# def update_profile(request, user_id):
	# 	user = User.objects.get(pk=user_id)
	# 	user.profile.first_name='what'
	# 	user.save()





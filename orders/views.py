from django.shortcuts import get_object_or_404, render, redirect
from django.http import Http404
# Create your views here.
from django.core import serializers
from .models import Order, Template, Notification
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PlaceOrderForm,OrderForm,TemplateForm, RegistrationForm, ProfileForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.db import transaction
try:
	from django.contrib.auth import get_user_model
except ImportError:
	from django.contrib.auth.models import User
else:
	User=get_user_model()

# Create your views here.
def index(request):
	notifications=Notification.objects.all()
	return render(request,'orders/index.html', context={'notifications': notifications})

class PlaceOrderView(LoginRequiredMixin, generic.ListView):
	login_url='../accounts/login/'
	redirect_field_name='redirect_to'
	template_name='orders/placeOrder.html'
	context_object_name='templates'

	def get_queryset(self):
		return Template.objects.all()

@login_required
def makeOrder(request):
	templates=Template.objects.all()
	order=OrderForm(request.POST, request.FILES)
	if request.method=='POST':
		form=OrderForm(request.POST, request.FILES)
		if form.is_valid():
			order=form.save(commit=False)
			order.user=request.user
			order.time=timezone.now()
			order.save()
			notification=Notification(order_id=order.id)
			notification.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form=OrderForm()
	return render(request, 'orders/placeOrder.html', context={'form': form, 'templates': templates},)	

@login_required
def showOrders(request):
	orders=Order.objects.all()
	users=User.objects.all()
	for i in range(len(orders)):
		user_last_name = users.get(pk=orders[i].user_id).last_name
		orders[i].user_id=user_last_name
	# for order in orders:
	# 	user_second_name = User.objects.get(pk=order.user_id)

	return render(request, 'orders/showOrders.html', context={'orders':orders},)

@login_required
def showOrder(request, order_id):
	order=Order.objects.get(pk=order_id)
	images=[]
	if order.attach1!="":
		images.append(order.attach1)
	if order.attach2!="":
		images.append(order.attach2)
	if order.attach3!="":
		images.append(order.attach3)
	if order.attach4!="":
		images.append(order.attach4)
	user=User.objects.get(pk=order.user_id)
	return render(request, 'orders/showOrder.html', context={'order':order, 'user':user,'images':images},)

@login_required
def showTemplates(request):
	templates=Template.objects.all()
	template=TemplateForm(request.POST)
	if request.method=='POST':
		form=TemplateForm(request.POST)
		if form.is_valid():
			template=form.save()
			return HttpResponseRedirect(reverse('showTemplates'))
	else:
		form=TemplateForm()
	return render(request, 'orders/showTemplates.html', context={'form': form,'templates': templates},)

@login_required
def showTemplate(request, template_id):
	template=Template.objects.get(pk=template_id)
	if request.method=='POST':
		if 'submit' in request.POST:
			form=TemplateForm(request.POST, instance=template)
			if form.is_valid():
				template=form.save()
				return HttpResponseRedirect(reverse('showTemplates'))
		elif 'delete' in request.POST:
			template.delete()
			return HttpResponseRedirect(reverse('showTemplates'))
	else:
		form=TemplateForm(instance=template)
	return render(request, 'orders/showTemplate.html', context={'form':form,'template': template})
	# template=Template.objects.get(pk=template_id)
	# if request.method=='POST':
	# 	form=TemplateForm(request.POST)
	# 	if form.is_valid():
	# 		template=form.save()
	# 		return HttpResponseRedirect(reverse('showTemplates'))
	# else:
	# 	form=TemplateForm()
	# return render(request, 'orders/showTemplate.html', context={'template': template})

def get_notifications(request):
	if request.GET:
		notifications=Notification.objects.all()
		return HttpResponse(json.dumps(notifications))
	else:
		notifications=Notification.objects.all()
		# data = serializers.serialize('json', notifications)
		# return HttpResponse(data, content_type="application/json")
		result_list = list(notifications.values('id', 'order_id'))
		return HttpResponse(json.dumps(result_list))

def delete_notification(request, notification_id):
	if request.GET:
		notification=Notification.objects.get(pk=notification_id)
		notification.delete()
		return HttpResponse('deleted')

# @login_required
# @transaction.atomic
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		profile_form = ProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user=form.save()
			profile=profile_form.save(commit=False)
			if profile.user_id is None:
				profile.user_id=user.id

			# return HttpResponse(profile_form.user_id)
			profile.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect(reverse('index'))
	else:
		form=UserCreationForm()
		profile_form=ProfileForm()

	return render(request, 'registration/register.html', context={'form': form, 'profile_form': profile_form})
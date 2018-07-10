from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.http import HttpResponse, HttpResponseRedirect

from . import views

urlpatterns = [
	# path('', views.IndexView.as_view(), name='index'),
	path('', lambda r: HttpResponseRedirect('index/')),
	path('index/', views.index, name='index'),
	path('placeOrder/', views.PlaceOrderView.as_view(), name='placeOrder'),
	path('makeOrder/', views.makeOrder, name='makeOrder'),
	path('accounts/', include('django.contrib.auth.urls')),
	path('accounts/login/', auth_views.LoginView.as_view()),
	path('showOrders/', views.showOrders, name='showOrders'),
	path('showOrder/<int:order_id>/', views.showOrder, name='showOrder'),
	path('showTemplates/', views.showTemplates, name='showTemplates'),
	path('showTemplate/<int:template_id>/', views.showTemplate, name='showTemplate'),
	path('get_notifications/', views.get_notifications, name='get_notifications'),
	path('delete_notification/<int:notification_id>/', views.delete_notification, name='delete_notification'),
	path('register/', views.register, name='register'),
]
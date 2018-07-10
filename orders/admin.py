from django.contrib import admin
from .models import Order, Template, Notification, Profile
# Register your models here.


admin.site.register(Order)
admin.site.register(Template)
admin.site.register(Notification)
admin.site.register(Profile)



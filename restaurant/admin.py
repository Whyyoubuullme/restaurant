from django.contrib import admin

from .models import Category,Dish,Reservation,Review 
# Register your models here.

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Reservation)
admin.site.register(Review)


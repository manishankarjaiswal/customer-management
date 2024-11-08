from django.contrib import admin
from .models.customers import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'phone_number', 'user')
    search_fields = ('first_name', 'last_name', 'phone_number')
    list_filter = ('user',)

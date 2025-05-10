"""
Admin configuration for the Customer model.

Registers the Customer model in the Django admin interface with custom display and search settings.
"""

from django.contrib import admin

from .models import Customer


class CustomerAdmin(admin.ModelAdmin):
    """
    Admin interface configuration for the Customer model.

    Attributes:
        list_display (tuple): Fields to display in the list view.
        search_fields (tuple): Fields to be searchable in the admin.
    """

    list_display = ('email', 'first_name', 'last_name', 'created_at', 'updated_at')
    search_fields = ('email', 'first_name', 'last_name')


admin.site.register(Customer, CustomerAdmin)

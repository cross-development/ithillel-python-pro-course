"""
Serializers for the Customer model.

Provides a CustomerSerializer for API representation of customer data.
"""

from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Customer model.
    """

    class Meta:
        model = Customer
        fields = ['id', 'email', 'first_name', 'last_name']

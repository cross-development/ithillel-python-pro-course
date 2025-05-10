"""
ViewSet for handling Customer API endpoints.
"""

from rest_framework import viewsets

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing customers.
    """

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

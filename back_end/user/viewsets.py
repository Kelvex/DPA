from rest_framework import viewsets
from user.models import Customer
from user.serializers import CustomerSerializer
from rest_framework.permissions import IsAuthenticated

class CustomerViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
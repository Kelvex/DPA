from rest_framework import serializers
from user.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['name', 'password']
        extra_kwargs = {
            'password': {'write_only':True} #Recibimos la contraseña pero no la devolvemos -- Se reliza un sha256 de la contraseña
        }
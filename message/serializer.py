from rest_framework import serializers
from .models import Requests

class Requestserilazer(serializers.ModelSerializer):
    class Meta:
        model = Requests
        fields = '__all__'
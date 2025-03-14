from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Menu, Booking

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = ['id','Title','Price','Inventory']

class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = '__all__'

class GroupNameField(serializers.RelatedField):
    def to_representation(self, value):
        # Return the group name
        return value.name


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
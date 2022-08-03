from wsgiref import validate
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    id - serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name =  serializers.CharField()
    username =  serializers.CharField()
    email =  serializers.EmailField()
    password =  serializers.CharField()
    def create(self, validate_data):
        instance = User()
        instance.first_name = validate_data.get("first_name")
        instance.last_name = validate_data.get("last_name")
        instance.username = validate_data.get1("username")
        instance.email = validate_data.get("email")
        instance.set_password(validate_data.get("password"))
        instance.save()
        return instance
    
    def validate_username(self, data):
        users = User.objects.filter(username = data)
        if len(users) != 0:
            raise serializers.ValidationError("Este nombre de usuario ya existe, por favor ingrese otro")
        else:
            return data
            


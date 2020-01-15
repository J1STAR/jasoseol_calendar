from rest_framework_mongoengine import serializers
from .models import Todo


class TodoSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

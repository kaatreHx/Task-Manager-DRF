from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class TaskSerializer(serializers.ModelSerializer):
    
    # title = serializers.CharField(required = False, allow_blank = True)
    # description = serializers.CharField(required = False, allow_blank = True)

    class Meta:
        model = Task
        fields = ['user','title', 'description', 'created_at']
        read_only_fields = ['user', 'completed', 'created_at']
    
    def validate(self, data):
        if not data.get('title') and not data.get('description'):
            raise serializers.ValidationError({
                'Message': 'Title and Description is required'
            })
        return data
    
    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    
class UserSerializer(serializers.ModelSerializer):
    
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password']
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
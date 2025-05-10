from rest_framework import serializers
from .models import Category, Post, Comment
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):

    # category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'category']

class CommentSerializer(serializers.ModelSerializer):
    
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'body', 'author', 'created', 'post']
        read_only_fields = ['author', 'created', 'post']

class PostDetailSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        mode = Post
        fields = ['id', 'title', 'body', 'comments']

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
    
    def validate(self, data):
        if not all([data.get('username'), data.get('password')]):
            raise ValidationError({
                'Message': 'Username and password is required'
            })
        
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
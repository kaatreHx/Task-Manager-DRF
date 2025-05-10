from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify   

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)    
    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)  
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author.username}'
     
    
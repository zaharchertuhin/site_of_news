from django.db import models
from django.contrib.auth import get_user_model

class News(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
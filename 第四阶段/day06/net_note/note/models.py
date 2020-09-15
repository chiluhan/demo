from django.db import models
from user.models import User

# Create your models here.
class Note(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    updata_time=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
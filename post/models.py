from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(max_length=2000,blank=True, null=True)
    created_at = models.DateTimeField(default = timezone.now)
    image = models.ImageField( upload_to='post-img/')
    active =models.BooleanField(default = False)

    def __str__(self):
        return self.title

   

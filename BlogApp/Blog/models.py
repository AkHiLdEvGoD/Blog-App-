from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Blog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_area = models.TextField()
    time_date_posted = models.DateTimeField(default=timezone.now)
    image =  models.ImageField(upload_to='blogPics/',blank=True,null=True)

    def __str__(self):
        return f'{self.user.username} posted on {self.time_date_posted}'

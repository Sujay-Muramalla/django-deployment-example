from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class UserProfileInfo(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user = models.OneToOneField(User)
    user = models.OneToOneField(User,on_delete=models.CASCADE)


    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username
from django.db import models
from django.utils.html import mark_safe

class User_details(models.Model):
    token=models.CharField(max_length=100,null=True,unique=True,verbose_name="Token")
    user_name=models.CharField(max_length=150,null=True,verbose_name="User_name")
    user_email=models.EmailField(max_length=254,null=True)
    google_id=models.CharField(max_length=254,null=True,default=None)
    facebook_id=models.CharField(max_length=254,null=True,default=None)
    apple_id=models.CharField(max_length=254,null=True,default=None)
    user_profile_pic=models.URLField(max_length=254,null=True)
    user_phone_no=models.CharField(max_length=15,null=True)
    is_deleted=models.BooleanField(default=False)
    is_guest=models.BooleanField(default=True)
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="Register at")
    def profile_preview(self):
        if self.user_profile_pic:
            return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.user_profile_pic))
        else:
            return '(No image)'

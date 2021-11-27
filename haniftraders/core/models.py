import os
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images/')

class status_lookup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,null=True)
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField(blank=True,default=None,null=True)

    def __unicode__(self):
        return '%s' % (self.name)

    def __str__(self):
       return self.name

class product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    img_url = models.CharField(max_length=255,blank=True)
    status_id = models.ForeignKey(status_lookup, related_name='status', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,null=True)
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField(blank=True,default=None,null=True)

    def __str__(self):
       return self.name



class item(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(product, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,null=True)
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField(blank=True,default=None,null=True)

    def __str__(self):
       return self.name

class item_image(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(item, related_name="images", on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,null=True)
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField(blank=True,default=None,null=True)

    def __str__(self):
        return self.url

class user_type_lookup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,null=True)
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField(blank=True,default=None,null=True)

    def __str__(self):
       return self.name

class core_user(models.Model):
    id = models.AutoField(primary_key=True)
    core_user_type_id = models.ForeignKey(
        user_type_lookup, related_name="user_types", on_delete=models.CASCADE)
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=10)
    address = models.TextField()
    img_url = models.CharField(max_length=255,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,default=None,null=True)
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField(blank=True,default=None,null=True)

    def __str__(self):
       return self.user_id.get_full_name()

class order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(core_user, related_name="users", on_delete=models.CASCADE)
    item_id = models.ForeignKey(item, related_name="items", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True,null=True)
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField(blank=True,default=None,null=True)
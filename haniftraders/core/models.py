from django.db import models


class product(models.Model):
    id = models.AutoField(primary_key=True)
    product_name = models.DateTimeField()
    img_url = models.DateTimeField()
    status_id = models.ForeignKey('status_lookup', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField()


class status_lookup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField()


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey('product', on_delete=models.CASCADE)
    description = models.DateTimeField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField()


class Item_image(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey('item', on_delete=models.CASCADE)
    url = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField()


class order(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    item_id = models.ForeignKey('item', on_delete=models.CASCADE)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField()


class user(models.Model):
    id = models.AutoField(primary_key=True)
    user_type_id = models.ForeignKey(
        'user_type_lookup', on_delete=models.CASCADE)
    fname = models.DateTimeField()
    lname = models.DateTimeField()
    address = models.DateTimeField()
    url = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField()


class user_type_lookup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField()
    activation_date = models.DateTimeField(auto_now_add=True)
    deactivation_date = models.DateTimeField()

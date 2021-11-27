from rest_framework import serializers
from collections import OrderedDict
from .models import product,status_lookup,item,core_user,User

class custom_dynamic_Field(serializers.RelatedField):
                
    def to_representation(self, value):
        return eval(f'value.{self.default}')

class status_lookup_serializer(serializers.ModelSerializer):
    class Meta:
        model = status_lookup
        fields = ('name','id')

class item_image_serializer(serializers.RelatedField):
    def to_representation(self, value):
        return value.url

class item_serializer(serializers.ModelSerializer):
    images = item_image_serializer(read_only=True,many=True)

    class Meta:
        model = item
        fields = ('id','product_id','name','description','address','price','images','created_at')
        extra_kwargs = {"product_id": {"error_messages": {"required": "please give item an product"}}}


class statusField(serializers.RelatedField):
    
    def to_representation(self, value):
        return value.name

class product_serializer(serializers.ModelSerializer):
    status_id = statusField(many=False,read_only=True)
                
    class Meta:
        model = product
        fields = ('id','name','status_id')


class core_user_serializer(serializers.ModelSerializer):
    first_name = custom_dynamic_Field(source="user_id",many=False,read_only=True,default='first_name')
    last_name = custom_dynamic_Field(source="user_id",many=False,read_only=True,default='last_name')
    username = custom_dynamic_Field(source="user_id",many=False,read_only=True,default='username')
    email = custom_dynamic_Field(source="user_id",many=False,read_only=True,default='email')
    is_active = custom_dynamic_Field(source="user_id",many=False,read_only=True,default='is_active')
    user_type = custom_dynamic_Field(source="core_user_type_id",many=False,read_only=True,default='name')
    class Meta:
        model = core_user
        fields =  ("id","phone_no","address","img_url","user_type",'first_name','last_name','username','email','is_active')

from django.contrib import admin
from .models import product,status_lookup,item,item_image,order,core_user,user_type_lookup

# Register your models here.
admin.site.register(product)
admin.site.register(status_lookup)
admin.site.register(item)
admin.site.register(item_image)
admin.site.register(order)
admin.site.register(core_user)
admin.site.register(user_type_lookup)
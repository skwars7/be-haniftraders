from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product',views.product_view)
router.register('status_lookup',views.status_lookup_view)
router.register('item',views.item_view)
router.register('user',views.core_user_view)

urlpatterns = [
    path('',include(router.urls))
]

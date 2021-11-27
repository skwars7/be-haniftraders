from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import product,status_lookup,item,core_user,User
from .serializers import product_serializer,status_lookup_serializer,item_serializer,core_user_serializer

class product_view(viewsets.ModelViewSet):
    queryset = product.objects.all()
    # import pdb;pdb.set_trace()
    serializer_class = product_serializer

class status_lookup_view(viewsets.ModelViewSet):
    queryset = status_lookup.objects.all()
    serializer_class = status_lookup_serializer

class item_view(viewsets.ModelViewSet):
    queryset = item.objects.all()
    serializer_class = item_serializer

class core_user_view(viewsets.ModelViewSet):
    queryset = core_user.objects.all()
    serializer_class = core_user_serializer

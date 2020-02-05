from django.shortcuts import render
from rest_framework import mixins
from .models import Picture

# Create your views here.

class PictureList(mixins.ListModelMixin):
    queryset = Picture.list()
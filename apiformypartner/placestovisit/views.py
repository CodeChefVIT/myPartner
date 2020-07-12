from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from rest_framework import generics
from .models import Add_place
from rest_framework.views import APIView
from .serializers import AddplaceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import Permission

class PlaceViewSet(viewsets.ModelViewSet):
    permission_classes=[
        permissions.IsAdminUser,
    ]
    serializer_class = AddplaceSerializer

    def get_queryset(self):
        queryset = Add_place.objects.all()
        return queryset

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)  

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)  

class PlaceViewList(generics.ListAPIView):
    queryset = Add_place.objects.all()
    serializer_class= AddplaceSerializer
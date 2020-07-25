from django.shortcuts import render
from rest_framework import viewsets,permissions
from rest_framework import generics
from .models import Rent_bike
from rest_framework.views import APIView
from .serializers import RentbikeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import Permission

class BikeViewSet(viewsets.ModelViewSet):
    permission_classes=[
        permissions.IsAdminUser,
    ]
    serializer_class = RentbikeSerializer

    def get_queryset(self):
        queryset = Rent_bike.objects.all()
        return queryset

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)  

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)  

class BikeViewList(generics.ListAPIView):
    queryset = Rent_bike.objects.all()
    serializer_class= RentbikeSerializer

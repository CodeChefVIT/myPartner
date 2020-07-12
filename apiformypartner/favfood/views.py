from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions
from rest_framework import generics
from .models import Rest_favfood
from rest_framework.views import APIView
from .serializers import RestnfoodSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import Permission

class RestFoodViewSet(viewsets.ModelViewSet):
    permission_classes=[
        permissions.IsAdminUser,
    ]
    serializer_class = RestnfoodSerializer

    def get_queryset(self):
        queryset = Rest_favfood.objects.all()
        return queryset

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)  

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)  

class RestFoodViewList(generics.ListAPIView):
    queryset = Add_place.objects.all()
    serializer_class= RestnfoodSerializer

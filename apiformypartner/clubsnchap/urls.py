from django.contrib import admin
from django.urls import path,include
from .import views
from .views import ClubViewSet
from .views import ClubViewList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('clubsnchap',ClubViewSet,basename="clubsnchap")
urlpatterns = router.urls

urlpatterns +=[
    path('changeinfo/',views.ClubViewList.as_view()),
]
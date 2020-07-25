from django.contrib import admin
from django.urls import path,include
from .import views
from .views import BikeViewSet
from .views import BikeViewList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('bikerent',BikeViewSet,basename="bikerent")
urlpatterns = router.urls

urlpatterns +=[
    path('bikechange/',views.BikeViewList.as_view()),
]
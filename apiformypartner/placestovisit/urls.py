from django.contrib import admin
from django.urls import path,include
from .import views
from .views import PlaceViewSet
from .views import PlaceViewList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('placestovisit',PlaceViewSet,basename="placestovisit")
urlpatterns = router.urls

urlpatterns +=[
    path('editinfo/',views.PlaceViewList.as_view()),
]
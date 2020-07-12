from django.contrib import admin
from django.urls import path,include
from .import views
from .views import RestFoodViewSet
from .views import RestFoodViewList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('favfood',RestFoodViewSet,basename="favfood")
urlpatterns = router.urls

urlpatterns +=[
    path('editfavinfo/',views.RestFoodViewList.as_view()),
]
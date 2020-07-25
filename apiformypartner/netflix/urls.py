from django.contrib import admin
from django.urls import path,include
from .import views
from .views import NetflViewSet
from .views import NetflViewList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('netflix',NetflViewSet,basename="netflix")
urlpatterns = router.urls

urlpatterns +=[
    path('deletenetflix/',views.NetflViewList.as_view()),
]
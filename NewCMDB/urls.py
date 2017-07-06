from django.conf.urls import url,include
from django.contrib import admin
from NewCMDB import views
urlpatterns = [
    url(r'^report/', views.asset_report),
]

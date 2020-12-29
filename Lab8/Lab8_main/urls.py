from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="homepage"),
    path('author', views.about, name = "author"),
    path('lab6', views.lab6, name = "lab6"),
    path('lab7', views.lab7, name = "lab7"),
    path('subjects', views.subjects, name = "subjects"),
    path('WAD', views.WAD, name = "WAD"),
    path('CM', views.CM, name = "CM"),
    path('OS', views.OS, name="OS"),
    path('CT', views.CT, name="CT"),
    path('RTDA', views.RTDA, name="RTDA"),
    path('PE', views.PE, name="PE"),
    path('NaT', views.NaT, name="NaT"),
    path('English', views.English, name="English"),
]
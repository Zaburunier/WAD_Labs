from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:questionId>/", views.detail, name="detail"),
    path("<int:questionId>/vote/", views.vote, name="vote"),
    path("<int:questionId>/results/", views.results, name="results"),
]
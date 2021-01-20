from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("auth/", views.auth, name="auth"),
    path("register/", views.register, name="register"),
    path("edit/",views.edit_mode , name="edit"),
    path("tournaments/", views.tournaments, name="tournaments"),
    path("tournaments/search/", views.tournaments_search, name="tournaments_search"),
    path("tournaments/<int:tournament_id>/", views.tournament_detail, name="tournament_detail"),
    path("tournaments/<int:tournament_id>/edit/", views.tournament_edit, name="tournament_edit"),
    path("tournaments/<int:tournament_id>/table/", views.tournament_table, name="tournament_table"),
    path("teams/", views.teams, name="teams"),
    path("teams/search/", views.teams_search, name="teams_search"),
    path("teams/<int:team_id>/", views.team_detail, name="team_detail"),
    path("teams/<int:team_id>/edit/", views.team_edit, name="team_edit"),
    path("matches/", views.matches, name="matches"),
    path("matches/search/", views.matches_search, name="matches_search"),
    path("matches/<int:match_id>/", views.match_detail, name="match_detail"),
]
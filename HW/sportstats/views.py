from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, QueryDict
from .models import Team, Tournament, Match, User
from .forms import TournamentForm, TeamForm
import json, http.client

def index(request):

    return render(request, "sportstats/index.html")


def tournaments(request):

    return render(request, "sportstats/tournaments/tournaments.html")


def tournaments_search(request):
    requested_name = request.GET.get("tournaments_srch_name").capitalize()
    requested_place = request.GET.get("tournaments_srch_host").capitalize()
    requested_year = request.GET.get("tournaments_srch_year")

    tournaments_to_show = Tournament.objects.filter(tournament_name__icontains=requested_name) \
        .filter(country_name__icontains=requested_place)
    # Проверяем корректность ввода года
    if requested_year.isdigit():
        # Если год был введён, то вводим дополнительную фильтрацию
        requested_year = int(requested_year)
        tournaments_to_show = tournaments_to_show.filter(year_held__exact=requested_year)
    else:
        # Иначе пропускаем
        requested_year = 0

    context = {
        "tournaments_to_show": tournaments_to_show,
        "saved_name" : requested_name,
        "saved_place" : requested_place,
        "saved_year" : '' if requested_year == 0 else requested_year,
    }
    return render(request, "sportstats/tournaments/tournaments_search.html", context)


def tournament_detail(request, tournament_id):
    tournament = get_object_or_404(Tournament, pk=tournament_id)
    participants = tournament.teams_participant.all()
    return render(request, "sportstats/tournaments/tournament_detail.html", {"tournament" : tournament,
                                                                             "teams" : participants})


def tournament_edit(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)

    # Совершаем проверку на то, пришёл ли запрос после изменения формы
    if request.method == "POST":
        # Если да, то надо передать информацию в БД
        formData = QueryDict.copy(request.POST)

        tournament.tournament_name = formData.get(key="tournament_name")
        tournament.year_held = formData.get(key="year_held")
        tournament.teams_participant.set(formData.getlist(key="teams_participant"))
        tournament.country_name = formData.get(key="country_name")
        tournament.is_regular = True if formData.get(key="is_regular") == "on" else False

        tournament.save()
        return redirect("tournament_detail", tournament_id)
    else:
        # Если нет, то просто генерируем форму и отправляем для отображения
        # При этом сразу заполним данными, поскольку эта строка точно уже существует
        form = TournamentForm(initial={
            "tournament_name": tournament.tournament_name,
            "year_held": tournament.year_held,
            "teams_participant": tournament.teams_participant.all(),
            "country_name": tournament.country_name,
            "is_regular": tournament.is_regular
        })
        return render(request, "sportstats/tournaments/tournament_edit.html", {"tournament": tournament,
                                                                           "form" : form})


def tournament_table(request, tournament_id):
    tournament = Tournament.objects.get(id=tournament_id)
    table = list()

    for team in tournament.teams_participant.all():
        tournament_matches = Match.objects.filter(tournament_id__exact=tournament_id)
        # Разделим домашние и гостевые матчи, чтобы избежать громоздких if-else
        home_matches = tournament_matches.filter(first_team__team_name__exact = team.team_name)
        guest_matches = tournament_matches.filter(second_team__team_name__exact = team.team_name)
        matches = 0
        points = 0
        wins = 0
        draws = 0
        defeats = 0

        for match in home_matches:
            matches = matches + 1

            if match.first_team_scores > match.second_team_scores:
                points = points + 3
                wins = wins + 1
            elif match.first_team_scores == match.second_team_scores:
                points = points + 1
                draws = draws + 1
            else:
                defeats = defeats + 1

        for match in guest_matches:
            matches = matches + 1
            if match.first_team_scores < match.second_team_scores:
                points = points + 3
                wins = wins + 1
            elif match.first_team_scores == match.second_team_scores:
                points = points + 1
                draws = draws + 1
            else:
                defeats = defeats + 1

        table.append((team, points, matches, wins, draws, defeats))

    # Сортируем по набранным очкам
    table.sort(key= lambda x: x[1], reverse=True)
    return render(request, "sportstats/tournaments/tournament_table.html", {"table" : table,
                                                                            "tournament": tournament})


def matches(request):
    return render(request, "sportstats/matches/matches.html")


def matches_search(request):
    requested_team1 = request.GET.get("matches_srch_team1").capitalize()
    requested_team2 = request.GET.get("matches_srch_team2").capitalize()

    matches_to_show = Match.objects.filter(first_team__team_name__icontains=requested_team1) \
        .filter(second_team__team_name__icontains=requested_team2)

    context = {
        "matches_to_show": matches_to_show,
        "saved_team1": requested_team1,
        "saved_team2": requested_team2,
    }
    return render(request, "sportstats/matches/matches_search.html", context)


def match_detail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return render(request, "sportstats/matches/match_detail.html", {"match" : match,})


def teams(request):
    return render(request, "sportstats/teams/teams.html")


def teams_search(request):
    query_param = request.GET.get("teams_srch_name").capitalize()

    context = {
        "teams_to_show": Team.objects.filter(team_name__icontains=query_param),
        "saved_name": query_param,
    }
    return render(request, "sportstats/teams/teams_search.html", context)


def team_detail(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    tournaments = Tournament.objects.all().prefetch_related('teams_participant').\
        filter(teams_participant__team_name__icontains=team.team_name)
    latest_matches = Match.objects.all().select_related("first_team").\
                         filter(first_team__team_name__icontains=team.team_name) | \
                     Match.objects.filter(second_team__team_name__icontains=team.team_name)

    return render(request, "sportstats/teams/team_detail.html", {"team" : team,
                                                                 "tournaments" : tournaments,
                                                                 "latest_matches" : latest_matches[:5],
                                                                  })


def team_edit(request, team_id):
    team = Team.objects.get(id=team_id)
    if request.method == "POST":
        # Обновляем данные
        formData = QueryDict.copy(request.POST)
        team.team_name = formData.get(key="team_name")
        team.country = formData.get(key="country")
        team.city = formData.get(key="city")

        # Отдельно обрабатываем список с турнирами
        tournaments = formData.getlist(key="tournaments")
        team.tournament_set.set(tournaments)


        # Сохраняем и выходим
        team.save()
        return redirect("team_detail", team_id)
    else:
        form = TeamForm(initial={
            "team_name" : team.team_name,
            "country" : team.country,
            "city" : team.city,
        })
        return render(request, "sportstats/teams/team_edit.html", {"team" : team,
                                                                   "form" : form,
                                                                   "tournaments" : Tournament.objects.all()})


def auth(request):
    got_login = request.POST.get("auth_email")
    got_password = request.POST.get("auth_password")
    # Если это до первой попытки или же ничего не введено, то возвращаем на ту же страницу
    if got_login == "" and got_password == "":
        return render(request, "sportstats/edit_mode/logon.html")

    # Проверяем, найден ли пользователь
    try:
        user = User.objects.get(email=got_login)
    except User.DoesNotExist:
        try:
            user = User.objects.get(username=got_login)
        except User.DoesNotExist:
            return render(request,
                          "sportstats/edit_mode/logon.html",
                          {"error_message": "Пользователь не найден!"})

    # Проверяем, совпадает ли пароль
    if user.password != got_password:
        return render(request,
                      "sportstats/edit_mode/logon.html",
                      {"error_message": "Введён неверный пароль!"})
    else:
        return redirect("/", { "navbar_color": "bg-danger",
                                      "navbar_brand_text" : "Kernel Mode"})



def register(request):
    # Если пришёл POST, то обрабатываем форму, иначе отображаем исходную страницу
    if request.method == "POST":
        got_email = request.POST.get("email")
        got_fname = request.POST.get("first_name")
        got_lname = request.POST.get("last_name")
        got_login = request.POST.get("username")
        got_pword = request.POST.get("password")
        new_user = User(email=got_email, first_name=got_fname, last_name=got_lname,
                        username=got_login, password=got_pword)
        new_user.save()
        return render(request, "sportstats/edit_mode/logon.html")
    else:
        return render(request, "sportstats/edit_mode/new_user.html")


def edit_mode(request):
    return render(request, "sportstats/edit_mode/edit_mode_main.html")

from django.db import models


class Team(models.Model):
    class Meta:
        verbose_name = "клуб"
        verbose_name_plural = "клубы"

    team_name = models.CharField(max_length=30, verbose_name="Название клуба")
    country = models.CharField(max_length=25, verbose_name="Страна")
    city = models.CharField(max_length=25, verbose_name="Город")

    def __str__(self):
        return "\"{0} ({1})\"".format(self.team_name, self.city)


class Tournament(models.Model):
    class Meta:
        verbose_name = "турнир"
        verbose_name_plural = "турниры"

    tournament_name = models.CharField(max_length=40, verbose_name="Название турнира")
    year_held = models.IntegerField(verbose_name="Год проведения")
    teams_participant = models.ManyToManyField(Team, verbose_name="Участники")
    country_name = models.CharField(max_length=25, verbose_name="Место проведения", default="")
    is_regular = models.BooleanField(default=True, verbose_name="Регулярный сезон")

    def __str__(self):
        return "{0} - {1}".format(self.tournament_name, self.year_held)


class Match(models.Model):
    class Meta:
        verbose_name = "матч"
        verbose_name_plural = "матчи"

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, verbose_name="Турнир")
    date_held = models.DateTimeField(verbose_name="Дата и время проведения")
    first_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team1", verbose_name="Хозяева")
    first_team_scores = models.IntegerField("Голы (хозяева)")
    second_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team2", verbose_name="Гости")
    second_team_scores = models.IntegerField("Голы (гости)")

    def __str__(self):
        return "{0} {1} - {2} {3} ({4}, {5})".format(self.first_team, self.first_team_scores,
                                           self.second_team_scores, self.second_team,
                                            self.tournament, self.date_held)


class User(models.Model):
    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    email = models.CharField(max_length=30, verbose_name="Почтовый адрес")
    first_name = models.CharField(max_length=20, verbose_name="Имя")
    last_name = models.CharField(max_length=25, verbose_name="Фамилия")
    username = models.CharField(max_length=20, verbose_name="Никнейм")
    password = models.CharField(max_length=40, verbose_name="Пароль")

    def __str__(self):
        return "{0} ({1} {2}, {3})".format(self.username, self.last_name, self.first_name, self.email)

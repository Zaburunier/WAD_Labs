from django import forms
from .models import Tournament, Team


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ["tournament_name", "year_held", "teams_participant", "country_name", "is_regular"]
        widgets = {
            "tournament_name" : forms.TextInput(attrs= {
                "class" : "form-control",
                "placeholder" : "Название турнира"
            }),
            "year_held" : forms.NumberInput(attrs= {
                "class": "form-control",
                "placeholder": "Год проведения"
            }),
            "teams_participant" : forms.SelectMultiple(attrs= {
                "class": "form-select",
                "size" : "10",
                "placeholder": "Участники"
            }),
            "country_name" : forms.TextInput(attrs= {
                "class": "form-control",
                "placeholder": "Страна проведения"
            }),
            "is_regular" : forms.CheckboxInput(attrs= {
                "class": "form-check",
                "placeholder": "Является регулярным чемпионатом"
            })
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ["team_name", "country", "city"]
        widgets = {
            "team_name": forms.TextInput(attrs={
                "class": "form-control mb-4",
                "placeholder": "Название команды"
            }),
            "country" : forms.TextInput(attrs={
                "class": "form-control mb-4",
                "placeholder": "Страна"
            }),
            "city": forms.TextInput(attrs={
                "class": "form-control mb-4",
                "placeholder": "Город"
            })
        }

    #tournaments = forms.MultipleChoiceField(choices=Tournament.objects.all(),
    #                                       widget=forms.SelectMultiple(attrs={
    #                                          "class": "form-control mb-4",
    #                                            "placeholder": "Турниры"
    #                                        }))
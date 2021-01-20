from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Question, Choice


def index(request):
    latestQuestions = Question.objects.order_by("-publicationDate")[:5]
    context = {
        "latestQuestions": latestQuestions,
    }
    return render(request, "polls/index.html", context)


def detail(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, "polls/detail.html", { "question" : question })


def vote(request, questionId):
    question = get_object_or_404(Question, pk=questionId)
    try:
        selectedChoice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question" : question,
            "error_message" : "You did not selected!"
        })
    else:
        selectedChoice.votesCounter = selectedChoice.votesCounter + 1
        selectedChoice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(questionId,)))


def results(request, questionId):
    return HttpResponse("You are watching results on question #{}".format(questionId))
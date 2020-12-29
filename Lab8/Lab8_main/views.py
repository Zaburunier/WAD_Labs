from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "Lab8_main/index.html")


def about(request):
    return render(request, "Lab8_main/about.html")


def lab6(request):
    return render(request, "Lab8_main/Lab6.html")


def lab7(request):
    return render(request, "Lab8_main/Lab7.html")


def subjects(request):
    return render(request, "Lab8_main/base_subjects.html")


def CM(request):
    return render(request, "Lab8_main/subjects/CM.html")


def English(request):
    return render(request, "Lab8_main/subjects/English.html")


def NaT(request):
    return render(request, "Lab8_main/subjects/NaT.html")

def OS(request):
    return render(request, "Lab8_main/subjects/OS.html")

def CT(request):
    return render(request, "Lab8_main/subjects/CT.html")

def RTDA(request):
    return render(request, "Lab8_main/subjects/RTDA.html")

def PE(request):
    return render(request, "Lab8_main/subjects/PE.html")

def WAD(request):
    return render(request, "Lab8_main/subjects/WAD.html")
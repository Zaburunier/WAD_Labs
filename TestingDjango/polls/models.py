from django.db import models
from django.utils import timezone
import datetime


class Question(models.Model):
    questionText = models.CharField(max_length=200)
    publicationDate = models.DateTimeField('date published')

    def __str__(self):
        return "{0}: {1}".format(str(self.id), self.questionText)

    def publishedRecently(self):
        return self.publicationDate >= (timezone.now() - datetime.timedelta(days=1))


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choiceText = models.CharField(max_length=200)
    votesCounter = models.IntegerField(default=0)

    def __str__(self):
        return "Choice \"{0}\" (for question {1})".format(self.choiceText, self.question.id)
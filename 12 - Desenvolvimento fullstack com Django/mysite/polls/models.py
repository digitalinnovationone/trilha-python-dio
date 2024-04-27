import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField("Texto da questão", max_length=200)
    pub_date = models.DateTimeField("Data da publicação")
    active = models.BooleanField("Ativo", default=True)

    class Meta:
        verbose_name = "Questão"
        verbose_name_plural = "Questões"

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self) -> str:
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Questão")
    choice_text = models.CharField("Descrição", max_length=200)
    votes = models.IntegerField("Votos", default=0)

    class Meta:
        verbose_name = "Opção"
        verbose_name_plural = "Opções"

    def __str__(self) -> str:
        return self.choice_text

import pytest
from django.utils import timezone
from polls.models import Question


@pytest.mark.django_db
def test_question_was_published_recently_success():
    # Given
    question_text = "Qual é sua linguagem de programação favorita?"
    pub_date = timezone.now()
    active = True

    # When
    question = Question.objects.create(question_text=question_text, pub_date=pub_date, active=active)

    # Then
    assert question.was_published_recently() is True

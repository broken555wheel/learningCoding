import datetime

from django.test import TestCase  #  used to define test cases.
from django.utils import timezone  # provides functionality related to timezones.

from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)  
        self.assertIs(future_question.was_published_recently(), False)
        """creates a Question instance with a publication date set in the future using the timezone.now() function and adding a timedelta of 30 days."""
        """It then calls the was_published_recently() method on the future_question object and asserts that it returns False using self.assertIs()"""
        """assertIs(): This method checks whether two objects are the same object, i.e., if they have the same identity. """


    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date is older than one day
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)



    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for questions whose pub_date is within the last day
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)
    


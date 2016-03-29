import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

# Create your tests here.

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertEqual(future_question.was_published_recently(), False)

        # fixing the bug: => polls/model.py

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is older than 1 day.
        """
        time = timezone.now()  - datetime.timedelta(days=30)
        old_question = Question(pub_date=time)
        self.assertEqual(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() should return True for questions whose
        pub_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_question = Question(pub_date=time)
        self.assertEqual(recent_question.was_published_recently(), True)

"""
# test client
>>>python manage.py shell

>>>(all)
from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
client = Client()

response = client.get('/')
response.status_code

from django.core.urlresolvers import reverse
response = client.get(reverse('polls:index'))
response.status_code
response.content


from polls.models import Question
from django.utils import timezone
q = Question(question_text="Who is your favorite Beatle?", pub_date=timezone.now())
q.save()
response = client.get('/polls/')
response.content
response.context['latest_question_list']
"""

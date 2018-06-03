import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import UserInfo

# TODO: TEST NEWUSERFORM INPUTS


########################################
# Helper Functions

def create_user(days, **kwargs):
    # create a user with given text a number of days offset from now
    # can use positive and negative integers
    
    time = timezone.now() + datetime.timedelta(days=days)
    return UserInfo.objects.create(pub_date=time,**kwargs)

########################################


# Create your tests here.

class UserInfoModelTests(TestCase):
    
    def test_was_published_recently_with_future_question(self):
        #was_published_recently() returns False for questions whose pub_date is in the future.
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = UserInfo(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
        
        
    def test_was_published_recently_with_old_user(self):
        # was_published_recently() returns False for questions whose pub_date is older than 1 day
        time = timezone.now() - datetime.timedelta(days=1,seconds=1)
        old_user = UserInfo(pub_date=time)
        self.assertIs(old_user.was_published_recently(), False)
        
    def test_was_published_recently_with_recent_question(self):
        # was_published_recently() returns True for questions whose pub_date is within the last day.
        time = timezone.now() -datetime.timedelta(hours=23,minutes=59,seconds=59)
        recent_user = UserInfo(pub_date=time)
        self.assertIs(recent_user.was_published_recently(), True)
        
        
class UserIndexViewTests(TestCase):
    def test_no_users(self):
        # if no users exist, display an appropriate message
        response = self.client.get(reverse('get_info:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No users found")
        self.assertQuerysetEqual(response.context['object_list'], [])
        
        
    def test_past_user(self):
        # Users with a pub_date in the past are displayed on index page
        create_user(days=-30, first_name='past', last_name='user')
        response = self.client.get(reverse('get_info:index'))
        self.assertQuerysetEqual(response.context['object_list'], ['<UserInfo: past user>'])
        
    
    def test_future_user(self):
        # Users with a pub_date in the future are not displayed oon the index page
        create_user(days=+30, first_name='future', last_name='user')
        response = self.client.get(reverse('get_info:index'))
        self.assertContains(response, "No users found")
        
    
    def test_past_and_future_users(self):
        # Even if there are both past and future users, only users in the past are displayed
        create_user(days=-10, first_name='previous', last_name='user')
        create_user(days=+10, first_name='future', last_name='user')
        response = self.client.get(reverse('get_info:index'))
        self.assertQuerysetEqual(response.context['object_list'], ['<UserInfo: previous user>'])
        
    
    def test_two_past_questions(self):
        # The index page displays multiple users
        create_user(days=-10, first_name='previous', last_name='user')
        create_user(days=-30, first_name='past', last_name='user')
        response = self.client.get(reverse('get_info:index'))
        self.assertQuerysetEqual(response.context['object_list'], ['<UserInfo: previous user>', '<UserInfo: past user>'])

        
class DetailViewTests(TestCase):
    def test_future_user(self):
        # the detail view of a user with a pub_date in the future returns 404 not found
        future_user = create_user(days=+30, first_name='future', last_name='user')
        url = reverse('get_info:detail', args=(future_user.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)
    
    def test_past_user(self):
        past_user = create_user(days=-30, first_name='past', last_name='user')
        url = reverse('get_info:detail', args=(past_user.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        
    
    def test_invalid_user_id(self):
        user = UserInfo(first_name="invalid", last_name="user", id=1)
        url = reverse('get_info:detail', args=(user.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)
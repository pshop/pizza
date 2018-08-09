from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserInfo, PostalAddress

# Create your tests here.

def create_full_user_no_address():

    user = User.objects.create_user('paulshop', 'pc@gmail.com', 'prout')
    user.first_name = 'paul'
    user.last_name = 'choppin'
    user.save()

    info = UserInfo(user=user)
    info.user.phone_number='0609120124'
    info.save()

    return user

class UserInfoTests(TestCase):

    def create_full_user_no_address(self):

        user = create_full_user()

        self.assertIs(user.username, 'paulshop')
        self.assertIs(user.first_name, 'paul')
        self.assertIs(user.last_name, 'choppin')
        self.assertEqual(user.email, 'pc@gmail.com')
        self.assertTrue(user.password)
        self.assertEqual(user.phone_number, '0609120124')
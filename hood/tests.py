from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
# Create your tests here.



class UserTest(TestCase):
    def setUp(self):
        self.user=User(username='ogolla',first_name='ogolla',last_name='okumu',email='ogollaokumu@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.user,User))

    def test_data(self):
        self.assertTrue(self.user.username,"ogolla")
        self.assertTrue(self.user.first_name,"ogolla")
        self.assertTrue(self.user.last_name,'okumu')
        self.assertTrue(self.user.email,'ogollaokumu@gmail.com')

    def test_save(self):
        self.user.save()
        users = User.objects.all()
        self.assertTrue(len(users)>0)

    def test_delete(self):
        user = User.objects.filter(id=1)
        user.delete()
        users = User.objects.all()
        self.assertTrue(len(users)==0)

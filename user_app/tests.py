from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

class RegisterTestCase(APITestCase):

    def test_register(self):
        data = {
            "usrename" : "testcase",
            "email": "testcase@mail.com",
            "password": "Test@123",
            "password2": "Test@123"
        }

        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
class LoginLogoutTestCase(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username = "testlogin", password = "test123")

    def test_login(self):
        data = {
            'username': "testlogin",
            'password': "test123"

        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):

        self.token = Token.objects.get(user__username="testlogin")
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key) 
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


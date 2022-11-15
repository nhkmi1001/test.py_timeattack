from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import User

class UserTest(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "username":"test",
            "fullname":"test",
            "email":"test@test.com",
            "password":"123",
        }
        response = self.client.post(url, user_data) 
        print(response.data)
        self.assertEqual(response.data['message'], '가입 완료!!')

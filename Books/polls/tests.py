from django import test
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import request, response

        # # # Create your tests here.
        # from rest_framework.test import APITestCase
        # from rest_framework.test import APIRequestFactory

        # from polls import views


        # class TestPoll(APITestCase):
        #     def setUp(self):
        #         self.factory = APIRequestFactory()
        #         self.view = views.PollViewSet.as_view({'get':'list'})
        #         self.uri ='/polls/'


        #     def test_list(self):
        #         request = self.factory.get(self.uri)
        #         response  = self.view(request)
        #         self.assertEqual(response.status_code,200,
        #                         "Expanded Responce code 200, recived {0} insted ".format(response.status_code))


from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class TestPoll(APITestCase):
    def setUp(self):
        # self.factory = APIRequestFactory()
        # self.uri = '/users/'
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password="test"
        )

    def test_list(self):
        request = self.factory.get(self.uri, HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         "Expanded Responce code 200, recived {0} instead ".format(response.status_code))













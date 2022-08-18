from django.contrib import admin
from django.contrib.auth.models import User
from django.db import router
from rest_framework import routers
# from .views import ChoiceList, CreateVote
# from .views import UserCreate, LoginView
from django.urls import path
from .views import  TestingAPI
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
# from .views import PollViewSet
# 
# router = DefaultRouter()
# router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    # path('polls/', polls_list, name='polls_list'),
    # # get list of polls
    # path('polls/<int:pk>/', polls_detail, name='polls_detail'),
    #  # get specific of poll

    # path("polls/",PollList.as_view(),name="polls_list"),
    # # get list of polls
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # # get specific of poll
    # path("choices/",ChoiceList.as_view(),name="choices_list"),
    # # get list of choices
    # path("vote/",CreateVote.as_view(),name="create_vote"),
    # # create vote

    # Get choices for specific poll and create choices for specific poll
    # path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choices_list"),
    # get list of choices

    # create vote for the  choice identified by choice_pk under the poll identified by pk
    # path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    # # get vote of choice_pk,polls_pk
    # path("user/", UserCreate.as_view(), name='user_create'),
    # path("login/", LoginView.as_view(), name="login"),
    # path("login/", views.obtain_auth_token, name="login"),
    path("testing/", TestingAPI.as_view(), name="testing"),
]

# urlpatterns += router.urls

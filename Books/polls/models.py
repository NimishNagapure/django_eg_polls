from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Poll(models.Model):
    question = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    poll = models.ForeignKey(
        Poll, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice = models.ForeignKey(
        Choice, related_name='votes', on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    voted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class meta:
        unique_together = ("poll", "voted_by")

import time
def user_profile_picture(instance, filename):
    filebase, extension = filename.split(".")
    return "user_profile_picture/%s.%s" % (
        str(int(round(time.time() * 1000))),
        extension,
    )

class Information(models.Model):
    first_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100,null=True)
    adhar = models.ImageField(upload_to=user_profile_picture,null = True)

    # def __str__(self):
    #     return self.first_name



from django.db import models


class Quiz(models.Model):
    name = models.CharField(max_length=10)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class Option(models.Model):
    content = models.TextField()
    is_correct = models.BooleanField()


class Question(models.Model):
    OBJECTIVE = 'OBJ'
    SUBJECTIVE = 'SBJ'
    QUESTION_TYPES = (
        (OBJECTIVE, 'Objective'),
        (SUBJECTIVE, 'Subjective'),
    )
    content = models.TextField()
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPES, default=OBJECTIVE)
    options = models.ManyToManyField(Option, related_name='options')


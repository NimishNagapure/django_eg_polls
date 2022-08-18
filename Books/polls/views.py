from collections import Counter
import json
import os
from django.conf import settings
from django.contrib.auth.models import Permission, User
from django.core.exceptions import PermissionDenied
from django.db.utils import Error
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from polls.models import Information, Question


# from rest_framework import viewsets
from .models import Poll, Choice
from .serializers import UserSerializer
# from django.contrib.auth import authenticate

# # Create your views here.

# class LoginView(APIView):
#     permission_classes = ()
#     def post(self,request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         user = authenticate(username=username, password=password)
#         if user:
#             return Response({"Token":user.auth_token.key})
#         else:
#             return Response({"Error":"Wrong Credentials"},status = status.HTTP_400_BAD_REQUEST)


# class PollViewSet(viewsets.ModelViewSet):
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer
    
#     # Authenticated users can delete only polls they have created.
#     def destroy(self, request, *args, **kwargs):
#         poll = Poll.objects.get(pk =self.kwargs["pk"])
#         if not request.user ==  poll.created_by:
#             raise PermissionDenied("You can not delete this poll.")
#         return super().destroy(request, *args, **kwargs)


# class UserCreate(generics.CreateAPIView):
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserSerializer

# class ChoiceList(generics.ListCreateAPIView):
#     def get_queryset(self):
#         queryset = Choice.objects.filter(poll_id= self.kwargs['pk'])     
#         # Get the choices for the specific poll by pk
#         return queryset
#     serializer_class = ChoiceSerializer

#     # Authenticated users can create choices only for polls they have created.
#     def post(self, request, *args, **kwargs):
#         poll = Poll.objects.get(pk = self.kwargs["pk"])
#         if not request.user == poll.created_by:
#             raise PermissionDenied("You cannot create choice for this poll")
#         return super().post(request, *args, **kwargs)


# Generics View

"""

# for ChoiceList we pass pk to checklist  we override get_queryset method to filter on choices with this poll_id
class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(poll_id= self.kwargs['pk'])     
        # Get the choices for the specific poll by pk
        return queryset
    serializer_class = ChoiceSerializer

#  We pass poll_id and choice_id. We subclass this from APIview , rather than a genric view , because we completly customize the behaviour.

class CreateVote(APIView):
    serializer_class = VoteSerializer

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get('voted_by')
        data = {'choice': choice_pk, 'poll': pk, 'voted_by': voted_by}   
        # To vote for the choices idetified by choice_pk
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""


# Generic view
"""
from django.db.models import query
from rest_framework import generics, serializers

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer

class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer

"""

#API Class Base View

"""
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class PollList(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        data = PollSerializer(polls, many=True).data
        return Response(data)

class PollDetail(APIView):
    def get(self, request, pk):
        poll = get_object_or_404(Poll, pk=pk)
        data = PollSerializer(poll).data
        return Response(data)
"""




#  Django views

"""
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Poll


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}  # we get list of dictionaries
    return JsonResponse(data)
    


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "question": poll.question,                      
        "created_by": poll.created_by.username,
        "pub_date": poll.pub_date   
    }}                                                                                      # we get dictionary                   
    return JsonResponse(data)

"""


from django.utils.datastructures import MultiValueDictKeyError



# class PostInformationArray(APIView):

#     def post(self, request):
#         first_name = request.data.get('first_name')
#         last_name = request.data.get('last_name')
#         adhar = request.data.get('adhar')

#         info = Information.objects.create(first_name=first_name, last_name=last_name,adhar=adhar)
#         data = InformationSerializer(info).data
#         return Response(data)
        
            



# class ChangePasswordSerializer(serializers.Serializer):
#     # old_password = serializers.CharField(max_length=255, min_length=6, write_only=True)
#     new_password = serializers.CharField(max_length=255, min_length=6, write_only=True)
#     confirm_password = serializers.CharField(
#         max_length=255, min_length=6, write_only=True
#     )

#     def validate(self, attrs):
#         # old_password = attrs.get("old_password", "")
#         new_password = attrs.get("new_password", "")
#         confirm_password = attrs.get("confirm_password", "")

#         # if not self.context["request"].user.check_password(old_password):
#         #     raise serializers.ValidationError("Old password is incorrect")
#         if new_password != confirm_password:
#             raise serializers.ValidationError("New password and confirm password does not match")
#         return attrs
    
#     def save(self, **kwargs):
#         user = self.context["request"].user
#         user.set_password(self.validated_data["new_password"])
#         user.save()
#         return user


# class ChangePasswordAPIView(APIView):
#     serializers_class = ChangePasswordSerializer
#     def put(self, request):
#         try:
#             user_id = request.auth["user_id"]
#             user = HrmsUsers.objects.filter(id=user_id).first()
#             if user:
#                 serializer = self.serializers_class(user,context={'request': request}, data=request.data)
#                 if serializer.is_valid():
#                     serializer.save()
#                     return Response(
#                         {"Message": "Password is changed successfully"},
#                         status=status.HTTP_200_OK,
#                     )
#                 return Response(
#                     {"Error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
#                 )
#             return Response(
#                 {"Error": "User doesn't exist"}, status=status.HTTP_400_BAD_REQUEST
#             )
#         except HrmsUsers.DoesNotExist:
#             return Response(
#                 {"Error": "User doesn't exist"}, status=status.HTTP_400_BAD_REQUEST
#             )
       


# def handle_uploaded_file(files):
#     photo_urls = []
#     for file in files:
#         with open(os.path.join(settings.MEDIA_ROOT, file.name), "wb+") as destination:
#             for chunk in file.chunks():
#                 destination.write(chunk)
#                 photo_urls.append(file.name)
#             destination.close()
#     return photo_urls



# class OnBoardingAPIView(APIView):
#     def patch(self, request):
#         try:
#             user_id = request.auth["user_id"]
#             personal_email = request.data["personal_email"]
#             user = Employee.objects.filter(user_id=user_id).first()
#             user.middle_name = request.data["middle_name"]
#             user.date_of_birth = request.data["date_of_birth"]
#             user.personal_email = personal_email
#             user.contact_number = request.data["contact_number"]
#             user.emergency_number = request.data["emergency_number"]
#             user.pan_number = request.data["pan_number"].upper()
#             user.job_title = request.data["job_title"]
#             user.employee_status = request.data["employee_status"].upper()
#             user.save()
#             address = Addresses.objects.filter(
#                 employee=(Employee.objects.filter(user_id=user_id)).first()
#             ).first()
#             address.address_data = request.data["address_data"]
#             address.save()
#             # document = DocumentMaster.objects.filter(
#             #     employee=(Employee.objects.filter(user_id=user_id)).first()
#             # ).first()
#             # document.document_data = request.data["document_data"]
#             # document.save()
#             bank_details = BankDetails.objects.filter(
#                 employee=(Employee.objects.filter(user_id=user_id)).first()
#             ).first()
#             bank_details.bank_name = request.data["bank_name"]
#             bank_details.ifsc_code = request.data["ifsc_code"]
#             bank_details.bank_address = request.data["bank_address"]
#             bank_details.account_number = request.data["account_number"]
#             bank_details.save()
#             return Response(
#                 {"Message": "Employee details is updated  successfully"},
#                 status=status.HTTP_201_CREATED,
#             )
#         except Employee.DoesNotExist:
#             return Response(
#                 {"Error": "Employee does not exists"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

"""

from django.db import connection
from django.db import reset_queries


def database_debug(func):
    def inner_func(*args, **kwargs):
        reset_queries()
        results = func()
        query_info = connection.queries
        print('function_name: {}'.format(func.__name__))
        print('query_count: {}'.format(len(query_info)))
        queries = ['{}\n'.format(query['sql']) for query in query_info]
        print('queries: \n{}'.format(''.join(queries)))
        return results
    return inner_func


class TestingAPI(APIView):
    # Normal Get API
    def get_(self,request):
        questions = Question.objects.all()
        # print(questions)
        quize_name = [question.quiz.name for question in questions]
        # print(quize_name)
        query_info = connection.queries
        print('query_count: {}'.format(len(query_info)))
        queries = ['{}\n'.format(query['sql']) for query in query_info]
        print('queries: \n{}'.format(''.join(queries)))
        return Response({"Message":quize_name},status=status.HTTP_200_OK)

    # Select Releated get API
    def get_(self,request):
        questions = Question.objects.select_related('quiz').all()
        # print(questions)
        quize_name = [question.quiz.name for question in questions]
        # print(quize_name)
        query_info = connection.queries
        print('query_count: {}'.format(len(query_info)))
        queries = ['{}\n'.format(query['sql']) for query in query_info]
        print('queries: \n{}'.format(''.join(queries)))
        return Response({"Message":quize_name},status=status.HTTP_200_OK)

    # Prefetch Releated get API
    def get(self,request):
        questions = Question.objects.prefetch_related('quiz').all()
        # print(questions)
        quize_name = [question.quiz.name for question in questions]
        # print(quize_name)
        query_info = connection.queries
        print('query_count: {}'.format(len(query_info)))
        queries = ['{}\n'.format(query['sql']) for query in query_info]
        print('queries: \n{}'.format(''.join(queries)))
        return Response({"Message":quize_name},status=status.HTTP_200_OK)

"""
        

class TestingAPI(APIView):
    # Normal Get API
    def get(self, request):
        polls = Information.objects.all()
        data = UserSerializer(polls, many=True).data
        return Response(data)
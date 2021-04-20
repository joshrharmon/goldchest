from django.shortcuts import render
from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken

import sqlite3
from sqlite3 import Error


# Create your views here.
class LeadListCreate(generics.ListCreateAPIView):
  permission_classes = (permissions.AllowAny,)
  queryset = Lead.objects.all()
  serializer_class = LeadSerializer


@api_view(['GET'])
def current_user(request):
  """
  Determine the current user by their token, and return their data
  """

  serializer = UserSerializer(request.user)
  return Response(serializer.data)


class UserList(APIView):
  """
  Create a new user. It's called 'UserList' because normally we'd have a get
  method here too, for retrieving a list of all User objects.
  """

  permission_classes = (permissions.AllowAny,)

  def get(self, request, format=None):
    """
    Return a list of all users.
    """

    usernames = [user.username for user in User.objects.all()]
    return Response(usernames)

  def post(self, request, format=None):
    serializer = UserSerializerWithToken(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def create_conn(path):
  connection = None
  try:
    connection = sqlite3.connect(path, check_same_thread=False)
    print("DB connection successful.")
  except Error as e:
    print(f"An error '{e}' occurred during db connection")
  return connection

@api_view(['GET'])
def steamID(request):
  username = request.user

  conn = create_conn("db.sqlite3")
  cursor = conn.execute("SELECT id FROM auth_user WHERE username='{}';"
      .format(username))
  userid = cursor.fetchall()[0][0]

  stmt = """SELECT claimed_id FROM django_openid_auth_useropenid WHERE
    id={};""".format(userid)
  cursor = conn.execute(stmt)
  steamid = cursor.fetchall()[0][0]

  conn.close()

  return Response(steamid[37:])

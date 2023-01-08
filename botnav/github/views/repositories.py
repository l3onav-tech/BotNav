from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.http import HttpResponse
import json


class CreateRepositoryView(APIView):

    def post(self, request):
        return Response({})

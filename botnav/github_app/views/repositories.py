from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from botnav.github_app.serializers import (
        CreateRepositorySerializer,
        ReadRepoSerializer
    )
import json


class CreateRepoAPIView(APIView):


    def post(self, request):
        serializer = CreateRepositorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response = serializer.save()
            return Response(response.json(), status=status.HTTP_201_CREATED)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)


class ReadRepoApiView(APIView):

    def post(self, request):
        serializer = ReadRepoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            response =  serializer.save()
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response({}, status=HTTP_400_BAD_REQUEST)

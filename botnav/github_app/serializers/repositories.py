from rest_framework import serializers
from django.conf import settings
import requests


class CreateRepositorySerializer(serializers.Serializer):

    organization = serializers.CharField(
            max_length=250,
            allow_blank=False,
            allow_null=False,
            trim_whitespace=True,
            default=settings.GITHUB_ORG_DEFAULT
        )
    name = serializers.CharField(
            max_length=250,
            allow_blank=False,
            allow_null=False,
            trim_whitespace=True
        )
    description = serializers.CharField(
            max_length=1024,
            allow_blank=True,
            allow_null=True,
            trim_whitespace=True,
            required=False
        )
    team_id = serializers.CharField(
            max_length=250,
            allow_blank=True,
            allow_null=True,
            trim_whitespace=True,
            required=False
       )
    private                = serializers.BooleanField(default=False)
    allow_squash_merge     = serializers.BooleanField(default=True)
    allow_merge_commit     = serializers.BooleanField(default=True)
    allow_rebase_merge     = serializers.BooleanField(default=True)
    allow_auto_merge       = serializers.BooleanField(default=False)
    delete_branch_on_merge = serializers.BooleanField(default=False)
    use_squash_pr_title_as_default = serializers.BooleanField(default=False)

    def create(self, data):
        org = data['organization']
        data.pop('organization')
        access_token = settings.GITHUB_TOKEN_API
        headers = {
            "accept" : "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": access_token
        }
        response = requests.post(
            f'https://api.github.com/orgs/{org}/repos',
            data=data,
            headers=headers
        )
        if response.status_code == 201:
            return response
        else:
            raise serializers.ValidationError(response.json()['message'])


class ReadRepoSerializer(serializers.Serializer):


    def create(self):
        org = settings.GITHUB_ORG_DEFAULT
        access_token = settings.GITHUB_TOKEN_API
        headers = {
            "accept" : "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Authorization": access_token
        }
        response = requests.get(
            f'https://api.github.com/orgs/{org}/repos',
            headers=headers
        )
        if response.status_code == 200:
            return response
        else:
            raise serializers.ValidationError(response.json()['message'])

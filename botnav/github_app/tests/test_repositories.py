from rest_framework.test import APIRequestFactory, APITestCase
from django.conf import settings
import requests

class RepoAPITest(APITestCase):

    def setUp(self):
        self.access_token=settings.GITHUB_TOKEN_API
        self.org_name="l3onav-tech"
        self.repo_name=""
        self.url = f"/api/orgs/{self.org_name}/repos"
        self.data = {
            "name": self.repo_name
        }
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/vnd.github+json"
        }

    def test_github_api_online(self):
        response = requests.get(f"https://api.github.com/user", headers=self.headers)
        self.assertEqual(response.status_code, 200)
    """
    def test_create_repo_success(self):
        response = self.client.post(self.url, data=self.data, headers=self.headers)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {})

    def test_create_repo_failure(self):
        response = self.client.post(self.url, data={'name':'test'}, headers=self.headers)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"message": "Error message"})
    """





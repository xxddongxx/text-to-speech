from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import User

PATH = "/api/v1/tts/"
REQUEST_DATA = {
    "title": "test",
    "text": "안녕하세요. 안녕 테스트입니다. Hi. 안녕 This is test. Wow!  안녕 멋지죠?. 안녕 한 번 만들어 봤어요. 안녕 부자연스럽지만!. 안녕 잘 부탁 드립니다?. 안녕 응원 부탁드려요. 안녕 GO GO GO. 안녕 Bye. 안녕 See Ya. 안녕 부탁 응원 테스트.",
}


def get_user():
    user = User.objects.create(username="test")
    user.set_password("test1234")
    user.save()
    return user


class TestProjectCreate(APITestCase):
    def setUp(self):
        self.user = get_user()

    def test_project_create(self):
        """
        프로젝트 생성 및 오디오 파일 생성 테스트
        """
        token = RefreshToken.for_user(self.user)
        project_url = PATH + "project/"
        header = {"HTTP_AUTHORIZATION": f"Bearer {token.access_token}"}
        response = self.client.post(project_url, REQUEST_DATA, **header)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)

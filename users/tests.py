from rest_framework.test import APITestCase
from rest_framework import status


class TestRegister(APITestCase):
    REGISTER_URL = "/api/v1/users/register/"

    def test_register_fail(self):
        """
        회원가입 실페 테스트
        """
        response = self.client.post(self.REGISTER_URL)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)

        response = self.client.post(self.REGISTER_URL, {"password": "test"})
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIsInstance(response_data, dict)
        self.assertIn("message", response_data)

    def test_register_success(self):
        """
        회원가입 성공 테스트
        """
        request_data = {
            "username": "test",
            "password": "test",
        }
        response = self.client.post(self.REGISTER_URL, request_data)
        response_data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsInstance(response_data, dict)
        self.assertIn("username", response_data)
        self.assertNotIn("password", response_data)

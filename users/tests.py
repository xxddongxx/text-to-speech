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

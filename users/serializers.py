from rest_framework import serializers

from users.models import User


class UsersRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def save(self):
        user = User(username=self.validated_data["username"])
        password = self.validated_data["password"]
        user.set_password(password)
        user.save()
        return user


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "name",
            "email",
            "phone",
        ]

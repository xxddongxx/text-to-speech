from collections import deque

from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from tts import serializers
from tts.models import Audio, Title
from tts.permission import IsOwner
from utils.util import Util


class ProjectView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    def post(self, request):
        """
        프로젝트 생성
        POST /api/v1/tts/project/
        """
        project_page = 0

        title = request.data["title"]
        text = [request.data["text"]]

        if not title:
            raise ParseError("프로젝트 제목이 없습니다.")
        if not text:
            raise ParseError("audio로 생성할 내용이 없습니다.")

        title_serializer = serializers.TitleSerializer(data=request.data)

        if not title_serializer.is_valid():
            return Response(title_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        title_model = title_serializer.save(author=self.request.user)
        title_pk = title_model.pk

        # 전처리
        preprocessing_text = Util().text_preprocessing(text)
        sentence_queue = deque(preprocessing_text)

        while sentence_queue:
            project_page += 1
            # 프로젝트 한 페이지 생성
            project_data = {"page": project_page, "title": title_pk}

            serializer = serializers.ProjectSerializer(data=project_data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            project_serializer = serializer.save()
            audio_text_list = Util().make_audio_data(
                sentence_queue, project_serializer, title_pk
            )

            file_mame = (
                str(project_serializer.title) + "_" + str(project_serializer.page)
            )
            Util().make_audio_file(audio_text_list, file_mame)

        return Response(
            {"message": "Success"},
            status=status.HTTP_201_CREATED,
        )


class ProjectDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    def get(self, request, pk):
        """
        특정 텍스트 조회
        GET /api/v1/tts/project/<pk>/?query=kwy_word
        """
        key_word = request.GET.get("query")
        audios = Audio.objects.filter(project_id=pk, text__contains=key_word)
        page = request.GET.get("page", 1)
        paginator = Paginator(audios, 10)
        serializer = serializers.AudioSerializer(paginator.get_page(page), many=True)

        return Response(
            {
                "message": "Success",
                "status": status.HTTP_200_OK,
                "total_count": paginator.count,
                "total_page": paginator.num_pages,
                "result": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    def delete(self, request, pk):
        """
        프로젝트 삭제
        DELETE /api/v1/tts/project/<pk>/
        프로젝트 대표 model Title 모델
        """
        project = Title.objects.get(pk=pk)
        project.delete()
        return Response({"message": "Success"}, status=status.HTTP_204_NO_CONTENT)


class AudioDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    def put(self, request, audio_pk):
        """
        텍스트 수정
        GET /api/v1/tts/audio/pk/
        """
        audio = Audio.objects.get(pk=audio_pk)
        serializer = serializers.AudioUpdateSerializer(audio, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, audio_pk):
        """
        Delete /api/v1/tts/audio/pk/
        """
        audio = Audio.objects.get(pk=audio_pk)
        audio.delete()
        return Response({"message": "Success"}, status=status.HTTP_204_NO_CONTENT)

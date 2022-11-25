import re

from gtts import gTTS
from gtts.tts import Speed

from tts import serializers


class Util:
    def text_preprocessing(self, text_list):
        """
        전처리
        1. 특수문자 재거
        2. .,!, ? 문장 구분
        3. 빈 문장 재거
        """
        delimiters = r"\. |\! |\? "
        re_sub_text = re.sub(
            r"~|`|@|#|\$|%|^|&|\*|\(|\)|_|\+|-|=|\||\|\{|}|\[|]|:|;|<|,|>|/",
            "",
            text_list[0],
        )
        re_split_text = re.split(delimiters, re_sub_text)
        re_strip_text = [re_text.strip() for re_text in re_split_text]
        remove_empty_text = list(filter(lambda x: len(x) > 0, re_strip_text))

        return remove_empty_text

    def make_audio_file(self, text_list, file_name):
        """
        audio 파일 생성
        """
        tts = gTTS(" ".join(text_list), lang="ko", slow=Speed.NORMAL)
        tts.save("audio\\" + file_name + ".mp3")

    def make_audio_data(self, sentence_queue, project, title_pk):
        """
        audio 데이터 생성
        """
        sequence = 0
        result = []
        while sequence < 10:
            if not sentence_queue:
                break

            sentence = sentence_queue.popleft()
            sequence += 1

            data = {
                "sequence": sequence,
                "text": sentence,
                "project": title_pk,
                "project_page": project.page,
            }

            audio_serializer = serializers.AudioSerializer(data=data)
            if audio_serializer.is_valid():
                audio = audio_serializer.save()
                result.append(audio.text)
        return result

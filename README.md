# :loudspeaker:text-to-speech
tts 딥러닝 모델을 사용한 일부 기능 구현

# :bookmark_tabs: 목차
* [Text to speach](#loudspeakertext-to-speech)
  * [목차](#bookmark_tabs-목차)
  * [프로젝트 요구사항](#clipboard-프로젝트-요구사항)
  * [API Docs](#books-api-docs)
    * [회원 가입](#회원-가입)
    * [로그인](#로그인)
    * [로그아웃](#로그아웃)
    * [프로젝트 생성](#프로젝트-생성오디오-생성)
    * [텍스트 조회](#텍스트-조회)
    * [텍스트 수정](#텍스트-수정)
    * [텍스트(오디오) 생성 / 삭제](#텍스트오디오-생성--삭제)
    * [프로젝트 삭제](#프로젝트-삭제)



# :clipboard: 프로젝트 요구사항
1. Text to Speech(TTS) 딥러닝 모델을 사용하기 위한 일부 기능을 구현하는 과제입니다.
2. 프로젝트 생성(오디오 생성)
  * 텍스트(str)가 담긴 리스트를 받습니다. (length = 1)
  * 이를 전처리하여 오디오를 생성하는 함수의 input으로 같이 넣습니다.
    [['text1', 'text2', 'text3', ....], path]
  * 일정시간 이후 함수에서 (id, text)형태의 원소를 가진 리스트를 리턴합니다.
    [('id1' ,'text1'), ('id2', 'text2'), ('id3', 'text3'), ....]
  * 오디오는 input의 path에 저장됩니다
3. 텍스트 조회
  * 특정 프로젝트의 n번째 페이지를 조회합니다.
  * 한페이지는 10문장으로 이루어져 있습니다.
4. 텍스트 수정
  * 한 문장의 텍스트와 스피드를 수정합니다.
5. 오디오파일 송신
  * 요청받은 오디오파일을 송신합니다.
6. 텍스트(오디오) 생성 / 삭제
  * 삽입위치는 항상 앞, 뒤가 아닌 중간도 가능.
7. 프로젝트 삭제

# :books: API Docs
## 회원 가입

> Method: POST<br>
URL: /api/v1/users/register/<br>
Description: SimpleJWT Token 발행<br>
Request Example
```json
{
    "username": "test@test.com",
    "password": "12341234"
}
```
> Response Example
```json
{
    "username": "test2@test.com"
}
```
##  로그인
> Method: POST<br>
URL: /api/v1/users/login/<br>
Request Example
```json
{
    "username": "test@test.com",
    "password": "12341234"
}
```
> Response Example
```json
{
    "refresh": "token_key1",
    "access": "token_key2"
}
```
##  로그아웃(
> Method: POST<br>
URL: /api/v1/users/logout/<br>
Request Example
```json
{
    "refresh": "token_key1"
}
```
## 프로젝트 생성(오디오 생성)
> Method: POST<br>
URL: /api/v1/tts/project/<br>
Request Example
```json
{
    "title": "project title",
    "text": "안녕하세요. 테스트 데#$%이터 (입니)다. 만나서 반[갑습니]다."
}
```
Response Example
> 전처리 관정<br>
> 1. 특수문자 재거(@#$%^ 등)<br>
> 2. ['.', '!', '?'] 문장 구분<br>
> 3. 빈 문장 재거<br>
> /audio/ 폴더에 파일 생성<br>
> 파일명: "프로젝트이름_프로젝트페이지"
```json
{
    "message": "Success"
}
```
## 텍스트 조회
> Method: GET<br>
URL: /api/v1/tts/project/pk/?query=안녕&page=1<br>
Response Example
```json
[
    {
        "id": 15,
        "sequence": 1,
        "text": "안녕하세요",
        "speed": 1.0,
        "updated_at": "2022-11-15T21:41:28.362041+09:00",
        "project_page": 1,
        "project": 1
    },
    {
        "id": 16,
        "sequence": 2,
        "text": "안녕 테스트입니다",
        "speed": 1.0,
        "updated_at": "2022-11-15T21:41:28.372046+09:00",
        "project_page": 1,
        "project": 1
    },
    . . . 
]
```

## 텍스트 수정
> Method: PUT<br>
URL: /api/v1/tts/audio/pk/<br>
Request Example
```json
{
    "text": "변경하는 텍스트.",
    "speed": 2.0
}
```
Request Example
```json
{
    "text": "변경하는 텍스트.",
    "speed": 2.0
}
```
## 텍스트(오디오) 생성 / 삭제
> Method: DELETE<br>
URL: /api/v1/tts/audio/pk/<br>
Request Example
```json
{
    "message": "Success"
}
```
## 프로젝트 삭제
> Method: DELETE<br>
URL: /api/v1/tts/project/pk/<br>
Request Example
```json
{
    "message": "Success"
}
```
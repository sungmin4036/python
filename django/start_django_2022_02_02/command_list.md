djanog-admin: 장고 사용할수 있는 명령어 나옴

django-admin startproject start_django_2022_02_02
            프로젝트 시작      프로젝트 이름

--

격리되어있는 실행 파일을 원하기 떄문에 가상환경 필요

가상환경 설치 장소는 프로젝트 만든곳 아래에 설치할것


- 파이참의 경우] 

파일-설정-projcet pragmatic-python interpreter-add-ok

- 비주얼 스튜디오 코드] 

python -m venv [가상환경 이름]

가상환경의 부모폴더를 폴더열기를 한후 F1 or Ctrl+Shift+p 를 한후, select interpreter 눌러서 가상환경 클릭. / or 왼쪽 아래 파이썬 인터프리터 선택

가상환경이 설치 되었기에 pip install django 하여 장고 설치하기

python manage.py runserver 명령어 실행하여 서버 실행


--

python manage.py startapp accountapp
                            [앱이름]

accountapp 만들었고, 이것을 사용할거다 라는걸 명시 필요

장고 메인 폴더 - settings.py - INSTALLED_APPS - accountapp(앱이름 추가)

--

장고는 각각 시큐리티 키 가지고 있음. 보안상 다른사람에게 알려주면 안됨.

깃헙에 올려버리는걸 방지하기 위해 장고 문서 이용

python -m pip install django-environ

\# pip install environ 하면 에러가 뜨니 주의할것

settings.py 에 내용 추가 및 가상 폴더에 .env 폴더 생성후 내용 추가.

이렇게하면 setting의 env 변수에 가상폴더 .env 내용이 포함된거여서 settings의 SECRET_KEY 삭제해도 된다.

SECRET_KEY = env('SEVRET_KEY')로 변경

.gitignore 에 .env 추가

---

루트 폴더에 templates 폴더 생성후 base.html 생성

view 에서 만든걸 html에 넣는 형식

settings에서

TEMPLATES = [

'DIRS': [os.path.join(BASE_DIR, 'templates')],
                                    폴더이름

을 수정해줘야한다. 장고가 이 탬플릿트가 어디있는지 알고서, html 파일들을 view 파일을 연결시켜준다.
--

accountapp 폴더에 다시 templates-accountapp 폴더를 만든다.

추후 사용시 가독성 높이기 위해서 하는 사전 작업

--

settings.py 에 STATIC_ROOT 추가

staticfiles 따로 관리 하기 위해서 static 폴더 생성 및 css파일 생성

--

hello_world.html 에서 css attribute 테스트
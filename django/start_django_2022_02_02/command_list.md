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
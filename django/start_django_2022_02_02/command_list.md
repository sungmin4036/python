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

---

settings.py 에 STATIC_ROOT 추가

staticfiles 따로 관리 하기 위해서 static 폴더 생성 및 css파일 생성

---

hello_world.html 에서 css attribute 테스트

---

python manage.py makemigrations

modles.py 에서 쓰는 DB 와 연동시킬 파이썬 파일로 만들어 주는 작업을 해주는 명령어

위의 명령어를 치면, migrations 폴더에서 파일이 생성된것을 확인할수있으며, 

\# 추가로 만들어진 파일을 임의로 지우면 적체적으로 깨질가능성이 매우 높으므로, 함부로 삭제하지 말것.

이것을 실제 서버에 적용하기 위해서 사용 하는 명령어는

python manage.py migrate

---


Exception Value: no such table: accountapp_helloworld 라는 에러 발생

장고 서버 끄고, 마이그레이션 재생성 및 재적용을 한후, 재실행하면 된다.

---


ㅁ 전체적인 흐름

![image](https://user-images.githubusercontent.com/62640332/152668716-52d7b1fa-563e-4f1d-b008-7bdd5237fe3f.png)


From -> hello world에 요청을 보낼시, 가상서버를 빌려서 실제서버를 올린 가정하에,

이 요청을 아무나 할수있는게 아닌 인증시스템필요.

=> 계정이라는 객체 필요.

1. 회원 가입 -----------------> create view
2. 로그인   ------------------> (login view)
3. 회원가입한 계정 보기 -------> read view  ---------> 장고에서는 Detail View 라고 불린다.
4. 회원가입한 계정 정보 변경 --> update view
5. 계정 탈퇴 -----------------> delete view

<br>
<br>

ㅁ 로그인,로그아운 처리순서

![image](https://user-images.githubusercontent.com/62640332/152681472-3448ac73-ba31-43c2-a768-f8e356d02181.png)

next라는 파라미터를 POST or GET을 통해서 next라는 밸류가 존재한다면은 진행되지만,

next값이 없다면, 세팅 안에있는 LOGIN_, REDIRECT_, URL  순으로 처리하고,

이거 마저도 없다면 Default로 처리한다.

---

djagno-bootstap4 이용, 설치후 , settings에 명시 및 html 파일에 명시

---

글꼴 추가

static 폴더에 fonts 라는 폴더 추가 및 그아래에 다운받은 글꼴 추가후, head.html에 style 태그 이용해서 추가

base.html에서 전체적으로 적용을위해서 추가.


---
update는 기본으로 아이디도 변경이 가능하게 설정되어있따.

그래서, forms.py를 생성하여, AccountUpdateForm을 수정하여 만들어 준뒤,  View.py에서 사용중인 form_class 을 UserCreationForm 

-> AccountUpdateForm 으로 변경한다.

---

현제 update, login 이런대를 직적 들어가면 로그인이 안되어있어도 들어가진다.

뭔가 말이 안되는 상황이다.

--> authentication 필요

---

파이썬 데코레이터, 그함수의 앞이나 뒤, 앞뒤에 붙어서 가독성이 좋게 만들어 주는것.

![image](https://user-images.githubusercontent.com/62640332/152809107-c0e6c76b-b277-487d-a496-16b31f241b4a.png)

---

root 계정 생성 

python manage.py createsuperuser

프로필 만들건데, 이미지를 다루기 위해서는  settingspy 에서 media 데이터 추가 

media에 필요한 라이브러리 설치 필요 pip install pillowp

---

account 객체와 Profile 객체는 1:1 로 구현 

Profile Image   
Profile Nickname
Profile Message   

No Delete View    
No Detail View


프로필 app 생성 python manage.py startapp profileapp

settings 에서 installed 에 추가, url 추가

![image](https://user-images.githubusercontent.com/62640332/152816870-e94db4bc-c0ba-42fd-b1c0-b1e7374eb2f7.png)

AccountAPP 의 usercreationForm 은 장고에서 기본 제공해주는것

ProfileAPP 의 경우에는 기본 제공해주지 않는다. => 새로운 폼을 만들어서 사용해야한다. but 수십 수백개가 되면 일일리 치지 어려움

 => Model Form, 기존의 모델을 폼으로 만들어주는 기능

 ![image](https://user-images.githubusercontent.com/62640332/152817199-7465bf96-2e6f-4fa0-93d9-12788a205c5d.png)

 ![image](https://user-images.githubusercontent.com/62640332/152817265-faebf7eb-e74c-4fa2-802e-46c0f5dfe557.png)


 profileapp 폴더에 forms.py 생성


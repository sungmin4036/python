개발 패턴

M odel   
V iew   
C ontroller --> T emplate(장고의 경우)   

==> MTV?MVT?

각 역할이 나눠지게 설계를 하게됨.

ㅁ Model

: 데이터 베이스와 장고 통신하게 해주는 도구

장고에서 객체를 만들면(유저의 계정 생성) 새로운 글을 씀(객체) 이러한 과정을 편리하게 해주는것이 Model, 

장고에서 DB언어 사용하지 않고도 편하게 사용가능하게 해줌. 

Row : Columns = Item : Attribute

- Django] Article(Title, article, Image...)

- Database] Row (Columns)

DB에 대해서 신경쓸 필요가 없게 된다.

ㅁ View

유저가 서버에 요청(request)을 하면, 서버가 응답을 한다.

응답을 하는 과정

1. check if authenticated
2. check request valid
3. Collect data from DB
4. render response
5. ....

이러한 과정을 View 에서 한다.

ㅁ Template

JS, HTML, CSS의 프론트 엔드단과 밀접한 관계, 즉 user Interface 어떻게 구현할것인지 

유저가 개시글을 보고싶으면, 서버에서 응답 과정 거쳐서 유저에게 보내줘야하는데, 이 개시글을 어떻게 구현할것인지를 Template가 한다

![image](https://user-images.githubusercontent.com/62640332/152121465-5ad5e858-ae1e-4959-9b7c-55498cee8a28.png)


---

H pyer   
T ext   
M arkup   
L anguage   

Template 에서 extends / include 자주 사용

- extends는 미리 만들어노는 html 탬플릿 파일을 만들어 노면, 이것을 가지고 와서 html을 만든다. => 바탕을 깔아주는 느낌

- include는 조각을 가지고 와서 탬플릿에 박아 넣는다. => 정의를 가져와서 붙이는 느낌

![image](https://user-images.githubusercontent.com/62640332/152164821-40879868-cdf1-4714-a32b-8a38d711cc45.png)


--

C ascading   
S tyle   
S sheet   

DISPALY Attribute] html 화면을 어떻게 구성하는지, 어떤 원리로 구성하는지

4가지 속성

1. Block
   
   ![image](https://user-images.githubusercontent.com/62640332/152366355-290bcb57-599f-4c23-bc9d-200080b6344f.png)

블럭의 속성은, 태그에는 모두 부모가 있고, 그 부모의 최대한의 너비를 모두 가져가면서, 블록 모양의 형태를 유지한다. 

높이를 따로 설정하지 않는한 가로 크기에 맞춰진다.

2. Inline

![image](https://user-images.githubusercontent.com/62640332/152366618-4f472e2d-c208-49dc-b994-21bcd9619838.png)

그 글씩의 높이만큼만 블록 크기 맞춰준다. 한 줄에 해결

3. Inline-block

![image](https://user-images.githubusercontent.com/62640332/152366811-0812c361-9418-4ee6-996e-fc550febfa2e.png)

블록인데도 불가하고, inline 처럼 한쪽에 쌓이는 형식

4. none

![image](https://user-images.githubusercontent.com/62640332/152366958-4979114a-a33a-4cc7-ab67-a180f3186a2d.png)

html 상에서 있긴 있지만, 시각화되는 거에서 아무것도 없음


\# visibility(시각화) 속성 이 있는데 여기서 Hidden 이라는 속성이 있다.

- Display none의 경우 자식이 논으로 바뀌면, 아예 없는 것처럼 취급한다. 아예 공간을 차지 하지 않음

- visibility의 hidden 의 경우 존재하긴 하지만 보이지만 않을뿐, 그 공간은 차지하고있다.


ㅁ SIZE attribue

1. px - 부모의 크기가 몇이든 상관 없이 무조건 고정 ex) Width: 100px Height: 100px
2. em - 부모가 커지거나 작아지면 자식도 똑같이 커지거나 작아진다. 그러나 부모가 여러개 있을경우 모든 부모의 곱해서 크기가 적용되버린다.
3. rem - 바로 위에 있는 부모가 커지든 작아지든 상관이 없으나, root HTML의 크기가 변경되면 이것을 따라간다.
4. %


![image](https://user-images.githubusercontent.com/62640332/152368448-1eb4ce2e-8ff2-486c-86fa-847feb8ab57e.png)


반응형(Responsive)으로 만들기 중요하다.

---

html 스타일 적용 되는 순서

1. html 파일 내부 태그
2. html 파일 style 구문
3. css파일



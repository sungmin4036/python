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



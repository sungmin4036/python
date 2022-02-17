개발 패턴

M odel   
V iew   
C ontroller ---> T emplate(장고의 경우)   

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


----

H pyer   
T ext   
M arkup   
L anguage   

Template 에서 extends / include 자주 사용

- extends는 미리 만들어노는 html 탬플릿 파일을 만들어 노면, 이것을 가지고 와서 html을 만든다. => 바탕을 깔아주는 느낌

- include는 조각을 가지고 와서 탬플릿에 박아 넣는다. => 정의를 가져와서 붙이는 느낌

![image](https://user-images.githubusercontent.com/62640332/152164821-40879868-cdf1-4714-a32b-8a38d711cc45.png)


---

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

----

html 스타일 적용 되는 순서

1. html 파일 내부 태그
2. html 파일 style 구문
3. css파일


----

HTTP Protocol

1. GET
2. POST

![image](https://user-images.githubusercontent.com/62640332/152633000-e301a21e-cb3e-4817-b6d8-ad8b9b9fbb62.png)

서버에서 무엇을 보내줘야하는지 정보가 정해져있다.

그것에 대한 데이터를 정의 되어 있는것이 GET 과 POST

https://onion.haus/ 로 데이터를 보낼경우


<br>
<br>

- GET 의 경우 대부분 조회(inquiry)를 위해서 사용된다.

https://onion.haus/?param1=value1

<br>
<br>

- POST의 경우 create, update를 위해서 사용된다.

https://oninon.haus/

POST + BODY << BODY에 데이터를 넣어서 보낸다.

---

<br>
<br>
 
 djanog 는 CURD 의 생산성이 좋은걸로 유명하다.

 Create  (view)
 Read    (view)
 Update  (view)
 Delete  (view)

 why?? 각 모든 기능에 대한 view 를 따로 제공해준다. (class) 

 => CBV

 C lass   
 B ased   
 V iew    

 이에 반대되는 말이 FBV(Function Based View)며, 함수 기반의 뷰로, 지금 까지만든 Hello World가 FBV 이다.

 ```
 def hello_world(request):
    
    if request.method == "POST": #GET 인지 POST인지 구별해서 처리하게 해야한다.
        
        temp = request.POST.get('hello_world_input')
        
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        hello_world_list = HelloWorld.objects.all()
      return HttpResponseRedirect(reverse('accountapp:hello_world'))
        
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
 ```

나중에 너무 길어진다.

```
class AccountCreateView(generic.CreateView):
   mdoel = User
   form_class = AccountCreateForm
   success_url = reverse_lazy('app:list')
   template_name = 'accountapp/account_create.html'
```
CBA 형식으로 하면 굉장히 짧아진다.

class base로 만들게 된다면, 대부분 좋아지지만 주로 생산성, 복잡도, 사용하는시간도 굉장히 좋아진다.


---

detail view 의경우 그 개시물의 정보 여서 지금은 single object 지만, 게시물이기떄문에 multi object 필요 ==> List View 필요 + Pagination

```
listview 형태

class ArticleListView(ListView):
   model = Article
   context_object_name = 'article_list'
   template_name = 'articleapp/list.html'
   paginate_by = 25  - 몇개의 객체를 보여줄것인지
```

- pagination? 
: generate page of objects로 ex) 구글에서 검색시 아래에 있는 1, 2, 3 페이지 등과같은것

- infinite Scroll
: ex) Facebook, Instargram, Pinterest...  이것 사용하려면 자바스크립트 필요.

![image](https://user-images.githubusercontent.com/62640332/153892785-c71f58a9-408f-49e1-9e4b-3fccdae2f437.png)

html에서 주로 사용할 객체가 article_list 와 page_obj 사용된다.

  
![image](https://user-images.githubusercontent.com/62640332/153893096-4466476c-bb25-45ea-ab22-1103e4deb568.png)

article_list는 말그대로 개시물의 리스트 이 안에 각 객체들의 정보가 들어가 있음

![image](https://user-images.githubusercontent.com/62640332/153893148-fa000c89-fd55-4e01-bda6-a4432acf2d5b.png)

page_obj 는 각 페이지의 링크 만들어준다.

---

![image](https://user-images.githubusercontent.com/62640332/154092202-01db3510-0319-49ab-9351-0b52fbc20224.png)

create view ] no object
detail view ] no form

detail view 에서는 form을 넣어버리면 안된다 => mixin 사용

![image](https://user-images.githubusercontent.com/62640332/154092543-0d1f778e-368d-485f-bfb7-fef5d9dd74fa.png)

다중 상속을 가능하게 해준다. 이내부에서 form 클래스를 지정해줌으로써, detail 뷰에서도 form 사용 가능하게 해준다.

![image](https://user-images.githubusercontent.com/62640332/154092603-d75ac260-dbc4-475d-91de-df378463b6ae.png)


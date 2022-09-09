### **1. 사전 준비**

우선 시작하기에 앞서 편의를 위한 추가 라이브러리 설치해주자!

```
pip install ipython # 파이썬 기본 쉘보다 더 강력한 파이썬 쉘
pip install django-extensions # Django 확장 프로그램 모음으로 shell_plus, graph model 등 다양한 확장 기능 제공
pip freeze > requirements.txt
```

![](https://blog.kakaocdn.net/dn/IBFYb/btrLiqlRCLn/ClZITfqanJOVvLcgv9uMFK/img.png)

> **Shell**

-   운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램
-   셀(껍데기)은 사용자와 운영 체제의 내부 사이의 인터페이스를 감싸는 층이기 때문에 이러한 이름이 붙었다.
-   "사용자 <-> 셸 <-> 운영체제"

> **Python Shell**

-   파이썬 코드를 실행해주는 인터프리터
    -   인터프리터 : 코드를 한 줄 씩 읽어 내려가며 실행하는 프로그램
-   인터렉티브 혹은 대화형 shell 이라고 부름
-   Python 명령어를 실행하여 그 결과를 바로 제공

![](https://blog.kakaocdn.net/dn/rdITD/btrLhXK22Vn/YH2lfqp1SDO9Q9gm04eFhk/img.png)

> **Django shell**

-   ORM 관련 구문 연습을 위해 파이썬 쉘 환경을 사용
-   다만 일반 파이썬 쉘을 통해서는 장고 프로젝트 환경에 영향을 줄 수 없기 때문에 Django 환경 안에서 진행할 수 있는 Django 쉘을 사용

```
python manage.py shell_plus
```

![](https://blog.kakaocdn.net/dn/d7gS8M/btrLhtDznkH/079b9yjyK9TKurQ8tieSxk/img.png)

![](https://blog.kakaocdn.net/dn/G4VMR/btrLiiOWzdp/kRyK2Cer7bGMpoLrR0Bkrk/img.png)

---

### **2. QuerySet API**

#### **# Database API**

-   Django가 기본적으로 ORM을 제공함에 따른 것으로 DB를 편하게 조작할 수 있도록 도움
-   Model을 만들면 Django는 객체들을 만들고 읽고 수정하고 지울 수 있는 **DB API를 자동으로 만든다**.

![](https://blog.kakaocdn.net/dn/bjvDxj/btrLiBOgLar/7Crl63MORXO0lR4N6LFLyk/img.png)

> **"objects" manager**

-   Django 모델이 데이터베이스 **쿼리 작업을 가능하게 하는 인터페이스**
-   Django는 기본적으로 모든 Django 모델 클래스에 대해 objects라는 Manager 객체를 자동으로 추가
-   이 **Manager(objects)를 통해 특정 데이터를 조작(메서드)**할 수 잇음
-   **"DB를 Python class로 조작할 수 있도록 여러 메서드를 제공하는 manager"**

#### **# Query**

-   데이버베이스에 특정한 데이터를 보여 달라는 요청
-   "쿼리문을 작성한다" = 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성
-   이때, 파이썬으로 작성한 코드가 **ORM에 의해 SQL로 변환되어 데이터베이스에 전달**되며, 데이터베이스의 응답 데이터를 ORM이 **QuerySet**이라는 자료 형태로 변환하여 우리에게 전달

> **QuerySet**

-   **데이터베이스에게서 전달받은 객체 목록(데이터 모음)**
    -   순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있음
-   Django ORM을 통해 만들어진 자료형이며, 필터를 걸거나 정렬 등을 수행할 수 있음
-   **"objects" manager를 사용하여 복수의 데이터를 가져오는 queryset metod를 사용할 때 반환되는 객체**
-   단, 데이터베이스가 단일한 객체를 반환할 때는 **QuerySet**이 아닌 **모델의 인스턴스로 반환됨**
-   즉, querySet과 상호작용하기 위해 사용되는 도구

![](https://blog.kakaocdn.net/dn/bvpXBg/btrLhuJjBYH/FRJUgVjMxjls6DzH7E0b3k/img.png)

---

### 3. CRUD

-   **Create / Read / Update / Delete**
    -   생성 / 조회 / 수정 / 삭제
-   대부분의 컴퓨터 소프트웨어가 가지는 기본적인 데이터 처리 기능 4가지를 묶어서 일컫는 말

> **CREATE**

데이터 객체를 생성하는 방법은 아래 3가지가 있다.

**# 첫 번째 방법**

1. **article = Article()  
**

-   클래스를 통한 인스턴스 생성

![](https://blog.kakaocdn.net/dn/KYkNP/btrLiAPoMRt/zMWtoKswWqx8Om8gh2lkHk/img.png)

2. **article.title**

-   클래스 변수명과 같은 이름의 인스턴스 변수를 생성 후 값 할당
-   인스턴스 생성 시 초기 값을 함께 작성하여 생성한다.

![](https://blog.kakaocdn.net/dn/KctTX/btrLgSw4sJ4/OuM7bJ6PpAdwdCyMBdamBk/img.png)

3. **article.save()**

-   인스턴스로 save 메서드 호출.
-   반드시 save 메서드를 호출하여야 비로소 DB에 데이터가 저장된다. (레코드 생성)
-   여기서 **DB 테이블의 칼럼 이름이 id임에도 pk를 사용할 수 있는 이유는 Django가 제공하는 shortcut 때문**

![](https://blog.kakaocdn.net/dn/de8Qhf/btrLhJM3eSQ/Vvdv3AuumUDafm5xXuUkHK/img.png)

**# 두 번째 방법**

-   인스턴스 생성 시 초기 값을 함께 작성하여 생성한다.

![](https://blog.kakaocdn.net/dn/l4rlF/btrLmyiSSbU/NN6CkQlL2igrCv2xc3rTX1/img.png)

**# 세 번째 방법**

-   QuerySet API 중 **create() 메서드 활용**

![](https://blog.kakaocdn.net/dn/biJb3Q/btrLkabIIkO/NANUtkVOptz9PXUV8IfcI1/img.png)

**# .save()**

-   "Saving object"
-   객체를 데이터베이스에 저장함
-   데이터 생성 시 save를 호출하기 전에는 객체의 id 값은 None
    -   id 값은 Django가 아니라 데이터베이스에서 계산되기 때문
-   단순히 모델 클래스를 통해 인스턴스를 생성하는 것은 DB에 영향을 미치지 않기 때문에 **반드시 save를 호출해야 테이블에 레코드가 생성됨**

> **READ  
> **

-   QuerySet API method를 사용해 데이터를 다양하게 조회하기
-   크게 2가지로 분류된다.
    1.  Methods that **"return new querysets"**
    2.  Methods that **"do not return querysets"**

**# all()**

-   QuerySet return
-   전체 데이터 조회

![](https://blog.kakaocdn.net/dn/pCh67/btrLiVlBpwp/rFojXij2u0Mda63w4wGf9K/img.png)

**# get()**

-   단일 데이터 조회
-   객체를 찾을 수 없으면 DoesNotExist 예외를 발생시키고, 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외를 발생시킴
-   위와 같은 특징을 가지고 있기 때문에 primary key와 같이 **고유성(uniqueness)을 보장하는 조회에서 사용해야 함**

![](https://blog.kakaocdn.net/dn/XJfhx/btrLkav2uIX/fYWzvl7Im0zWOVHdN5lPik/img.png)

**# filter()**

-   지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환

![](https://blog.kakaocdn.net/dn/bghUWw/btrLmx5lWQ4/kL8EHiYPvK0iMCmAPNvuaK/img.png)

**# Field lookups**

-   특정 레코드에 대한 조건을 설정하는 방법
-   QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인자로 지정됨
-   다양한 built-in lookups는 공식문서 참고
    -   https://docs.djanggoproject.com/en/3.2/ref/models/querysets/#field-lookups

![](https://blog.kakaocdn.net/dn/pXNXo/btrLiBneuA8/x4Hyq0sSj9PTuaOafT5e51/img.png)

> **Update  
> **

**# 과정**

1.  수정하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
2.  article 인스턴스 객체의 인스턴스 변수 값을 새로운 값으로 할당
3.  save() 인스턴스 메서드 호출

![](https://blog.kakaocdn.net/dn/XWue9/btrLgScNVOT/H47OUL145mytci77RoInEk/img.png)

> **Delete 과정**

1.  삭제하고자 하는 article 인스턴스 객체를 조회 후 반환 값을 저장
2.  delete() 인스턴스 메서드 호출

![](https://blog.kakaocdn.net/dn/b2jMec/btrLiqMSRHh/FxduSbYJ63O3Dhm6rgKGoK/img.png)

#### # 참고 __str__()

-   표준 파이썬 클래스의 메서드인 **str()을 정의하여** 각각의 object가 사람이 읽을 수 있는 문자열을 **반환(return)**하도록 할 수 있음
-   작성 후 반드시 shell 재시작해야 반영

![](https://blog.kakaocdn.net/dn/vPkuA/btrLhhQLLPq/tbz73Ac2SanCCrVpaGuNW0/img.png)
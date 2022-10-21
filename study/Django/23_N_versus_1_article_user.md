앞에서는 Comment(N)와 Article(1) 모델 간 관계를 설정하였다. 이번엔 Article(N)과 User(1) 간 관계를 알아보자

"0개 이상의 게시글은 1개의 회원에 의해 작성될 수 있음"

#### **목차**

1.  Referencing the User model
2.  CREATE
3.  Delete
4.  Update
5.  Read

---

### **1. Referencing the User model**

> **Django에서 User 모델을 참조하는 방법**

1.  **settings.AUTH_USER_MODEL**
    -   반환 값 : **'accounts.User' (문자열)**
    -   User 모델에 대한 외래 키 또는 M:N 관계를 정의할 때 사용
    -   **models.py의 모델 필드에서 User 모델을 참조할 때 사용**
2.  **get_user_model()**
    -   반환 값 : **User Object (객체)**
    -   현재 활성화(active) 된 User 모델을 반환
    -   커스터마이징한 User 모델이 있을 경우는 Custom User 모델, 그렇지 않으면 User를 반환
    -   **models.py가 아닌 다른 모든 곳에서 유저 모델을 참조할 때 사용**

> **모델 관계 설정**

![](https://blog.kakaocdn.net/dn/OL5FG/btrOqzUAuak/wOnqgMnkPje6VuqNokgYO0/img.png)

-   Article 모델에 User 모델을 참조하는 외래 키 작성

![](https://blog.kakaocdn.net/dn/k3eqH/btrOqLHdbdQ/Ni5KWWjYynptiXzD5aFArK/img.png)

**※ Migration 진행**

-   기존에 존재하던 테이블에 새로운 칼럼이 추가되어야 하는 상황
-   따라서, migrations 파일이 곧바로 만들어지는 것이 아닌 일련의 과정 필요

```
python manage.py makemigrations
```

![](https://blog.kakaocdn.net/dn/V0QLM/btrOqTZjTCY/V8ndcUk41pd0J9XjoBPno1/img.png)

-   첫 번째 화면
    -   기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래 키 필드 **user_id**가 생성되지 않음
    -   그래서 기본값을 어떻게 작성할 것인지 선택해야 함
    -   1을 입력하고 Enter 진행 (다음 화면에서 직접 기본 값 입력)

![](https://blog.kakaocdn.net/dn/ONcdE/btrOscDOttI/rvAwCY8DwtWzc7T5SEKGo1/img.png)

-   두 번째 화면
    -   article의 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야 함
    -   마찬가지고 1 입력하고 Enter 진행
    -   그러면 기존 작성된 게시글이 존재한다면 모두 1번 회원이 작성한 것으로 처리

-   migrations 파일 생성 후 migrate 진행
-   article 테이블 스키마 변경 및 확인

![](https://blog.kakaocdn.net/dn/bpCYfX/btrOqNLMhSi/Fnn2phBGnrl3m7qmfNska1/img.png)

> **Django에서 User 모델을 참조하는 방법 정리**

-   models.py에서는 **settings.AUTH_USER_MODEL**
-   다른 모든 곳에서는 **get_user_model()**

---

### **2. CREATE**

-   인증된 회원의 게시글 작성 구현하기
-   작성하기 전 로그인을 먼저 진행한 상태로 진행

> **ArticleForm**

![](https://blog.kakaocdn.net/dn/49g49/btrOpTsiXAR/xYbsriQzRs1OdPbkRy7Fl0/img.png)

-   ArticleForm 출력을 확인해보면 create 템플릿에서 불필요한 필드(user)가 출력됨
-   이전에 CommentForm에서 외래 키 필드 article이 출력되는 상황과 동일한 상황
-   user 필드에 작성해야 하는 user 객체는 view 함수의 request 객체를 활용해야 함
-   따라서 아래와 같이 수정

![](https://blog.kakaocdn.net/dn/cSEA5c/btrOpR2iRL2/G9iMsFY8ZkFesq5wpgMqv1/img.png)

> **외래 키 데이터 누락**

-   게시글 작성 시 **NOT NULL constraint failed: articles_article.user_id 에러** 발생

![](https://blog.kakaocdn.net/dn/cG8OnC/btrOqM7cgte/LnRTEaNrvU7mPkgJEUK6z0/img.png)

-   "NOT NULL 제약 조건이 실패했다. articles_article 테이블의 user_id 컬럼에서"
-   게시글 작성 시 외래 키에 저장되어야 할 작성자 정보가 누락되었기 때문

-   게시글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션을 활용

![](https://blog.kakaocdn.net/dn/pDxPc/btrOnLIdKt4/TVbEtCeAt5tdelwKkzb51K/img.png)

---

### **3. DELETE**

> **게시글 삭제 시 작성자 확인**

-   이제 게시글에는 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 삭제할 수 있도록 함

![](https://blog.kakaocdn.net/dn/dtcLSq/btrOqUYgZcE/1SXmpu2ClyTLJEWvvdSqBK/img.png)

---

### **4. UPDATE**

> **게시글 수정 시 작성자 확인**

-   수정도 마찬가지로 수정을 요청하려는 사람과 게시글을 작성한 사람을 비교하여 본인의 게시글만 수정할 수 있도록 함

![](https://blog.kakaocdn.net/dn/CzQx5/btrOrSZVZ3D/DIKzCP3CzamDjfWuXmgV51/img.png)

-   추가로 해당 게시글의 작성자가 아니라면, 수정/삭제 버튼을 출력하지 않도록 하기

![](https://blog.kakaocdn.net/dn/qskPy/btrOlQCXH7W/rDWaauMfFE1vX0CP6kgM7k/img.png)

---

### **5. READ**

> **게시글 작성자 출력**

-   index 템플릿과 detail 템플릿에서 각 게시글의 작성자 출력

![](https://blog.kakaocdn.net/dn/cv4SuE/btrOrfnxEXW/50IhhPvXfrogqyOI6DEFGK/img.png)
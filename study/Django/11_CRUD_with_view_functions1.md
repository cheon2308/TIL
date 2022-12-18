
#### **목차**

1. 사전 준비
2. Read / Create
3. redirect()
4. POST method
5. CSRF
6. DELETE
7. UPDATE

---

### **1. 사전 준비**

앞서 배웠던 경로 설정 및 base 템플릿 작성을 해보고 시작하자

-   base 템플릿 작성
    -   bootstrap CDN 및 템플릿 추가 경로 작성

![](https://blog.kakaocdn.net/dn/bAlEr1/btrLkvhqdB7/KEcadj4RsCXW7U2YG8VvvK/img.png)

-   URL 분리 및 연결

![](https://blog.kakaocdn.net/dn/b1eV97/btrLu3pDKw9/4wLdYeu1CElgjP7FTjxx10/img.png)

-   index 페이지 작성

![](https://blog.kakaocdn.net/dn/bfH0i3/btrLntDpijs/hYx769l2qCgF15pcZQTFDK/img.png)

![](https://blog.kakaocdn.net/dn/Txlfn/btrLulqMMz3/XyKb8MHfpwJKWTyVP0kUJK/img.png)

![](https://blog.kakaocdn.net/dn/rwJND/btrLk4qxuVX/SrKPFpum6NWIYzxiOH7gH0/img.png)

index 페이지 작성 순서와 같이 **항상 urls -> views -> templates의 순서를 지키면서** **작성하자!!**

---

### 2. READ / CREATE

**# READ 1(index page)** 

index page에서는 전체 게시글을 조회해서 출력하는데 앞서 urls는 작성해주었으므로 view 함수와 index를 작성해준다. 

![](https://blog.kakaocdn.net/dn/beAcee/btrLouWCYZL/u98hhFhnqsHrBYKdbjKhxk/img.png)

![](https://blog.kakaocdn.net/dn/bhQq6o/btrLqdmKX1a/7RGwlle1nAift4GgYFx5q1/img.png)

**# CREATE**

create 로직을 구현하기 위해서는 과연 몇 개의 view 함수가 필요할까?

1.  사용자의 입력을 받을 페이지를 **렌더링 하는** 함수 1개
    -   "new" function
2.  사용자가 입력한 데이터를 전송받아 **DB**에 저장하는 함수 1개
    1.  "create" view function

> **new**

우선 **new** function을 적용시켜주기 위해 url 작성을 해준다.

![](https://blog.kakaocdn.net/dn/bYKAEL/btrLuhaSbDr/BIQGQHp6BbAoSDCLxtAoa0/img.png)

페이지를 **렌더링**하는 것이 목적이므로 "**new.html"**로 정보를 바로 넘겨주자.

![](https://blog.kakaocdn.net/dn/cjpaqH/btrLovnHzGf/ySh5Mg3NCkxxR7wX6gmixk/img.png)

내가 생성할 정보들의 목록을 아래와 같이 Type과 함께 작성해주고, 뒤로 가기 위한 하이퍼링크를 작성해주는데 앞서 배웠듯이 "**app name:url name"으로** 작성해준다.

![](https://blog.kakaocdn.net/dn/bdX1Hj/btrLlF493Mx/2ie24mfwzW2ydgbDx8SJQ0/img.png)

하지만 아직 action 칸이 채워져 있지 않아 생성이 되지 않을 것이다!! 아래 create를 통하여 **DB에 저장**을 해주자

> **create**

마찬가지로 항상 url부터 작성해준다.

![](https://blog.kakaocdn.net/dn/ES1aJ/btrLvCZFeYj/j1zzZU3wf0kGjkj2I7QKKk/img.png)

그 이후 작성을 해주는데 데이터를 생성하는 3가지 방법 중 어떤 것을 사용하여도 괜찮으나 1번과 2번의 경우 **꼭!!!!** **.save()**를 해주어야 DB에 저장된다는 것을 잊지 말자.

![](https://blog.kakaocdn.net/dn/dchMXW/btrLkvaEjjl/H7i8n6gHyNkTamm7A3qkR0/img.png)

또한 여기서 2번째 방법을 사용한 이유는 

-   3번째와 같이 create 메서드가 더 간편해 보이지만 추후 데이터가 저장되기 전에 **유효성 검사 과정을 거치게 됨**
-   이때, **유효성 검사가 진행된 후에 save 메서드가 호출되는 구조**를 택하기 위해서이다.

게시글을 작성한 후 확인해보자!

![](https://blog.kakaocdn.net/dn/oskXs/btrLouoRkaO/WE0X8IQYZZUKRIO99L9yvk/img.png)

![](https://blog.kakaocdn.net/dn/qujDd/btrLu2xyFiz/kYMvm6ERGpbyU5EI3ehcuK/img.png)

이제는 action을 통하여 데이터를 보낼 곳이 생겼으므로 작성이 잘 되었을 것이다.

원하는 결과가 나왔는지 index 페이지에 렌더링 하기 위하여 view 함수 내부에 **return render(request, **'articles/index.html**')로 수정해주었다**.

![](https://blog.kakaocdn.net/dn/4oncQ/btrLuhaUwb8/oXs15AWaSJ2Rh8OkpZUzy1/img.png)

하지만 index 페이지에 돌아가서 확인해보면 아래와 같은 문제가 발생한 것을 확인할 수 있다.

1.  게시글 작성 후 index 페이지가 출력되지만 게시글은 조회되지 않음
    -   create함수에서 index.html 문서를 렌더링 해주기 위해 수정하는 과정에서 **context 데이터와** 함께 렌더링 하지 않았기 때문이다.
    -   index 페이지 url로 다시 요청을 보내면 해결된다!
2.  게시글 작성 후 URL은 여전히 create에 머물러 있다.
    -   index view 함수를 통해 렌더링 된 것이 아니기 때문
    -   즉, index view 함수의 반환 값이 아닌 **단순히 index 페이지만 render 된 것이다.**

---

### **3. Django shorcut function - "redirect()"**

-   인자에 작성된 곳으로 요청을 보낸다.
-   사용 가능한 인자
    -   **view name (URL pattern name)**
    -   **absolute or relative URL**

```PYTHON
# 1.
return redirect('articles:index')

# 2.
return redirect('/articles/')
```

-   따라서 view 함수 내부의 수정해주었던 return render(..)을 삭제하고 아래와 같이 재작성해준다.

![](https://blog.kakaocdn.net/dn/sH3H8/btrLqXYAKSU/Gr9THWgTYUTee3eDQGUob1/img.png)

게시글을 작성한 후에 터미널 로그를 확인하면 url이 달라진 것을 볼 수 있다.

![](https://blog.kakaocdn.net/dn/nPAHs/btrLr2yy8ng/5JkFLKHvZFRhKdltnhAkuk/img.png)

-   **동작 원리**
    1.  클라이언트가 create url로 요청을 보냄
    2.  create view 함수의 redirect 함수가 302 status code를 응답
    3.  응답받은 브라우저는 redirect 인자에 담긴 주소(index)로 사용자를 이동시키기 위해 index url로 Django에 재요청
    4.  index page를 정상적으로 응답 받음 (200 status code)

#### # 참고

> **302 Found**

-   HTTP response status code 중 하나
-   해당 상태 코드를 응답받으면 브라우저는 사용자를 해당 URL의 페이지로 이동 시킴

> **HTTP response status code**

-   클라이언트에게 특정 HTTP **요청이 성공적으로 완료되었는지 여부**를 알려줌
-   응답그룹 5개
    1.  Informational responses (1xx)
    2.  Successful responses (2xx)
    3.  Redirection messages (3xx)
    4.  Client error responses (4xx)
    5.  Server error responses (5xx)

---

### 4. POST method

> **HTTP method GET 재검토**

-   현재는 게시글이 작성될 때 **/articles/create/?title=11&content=22**와 같은 URL로 요청이 보내짐
-   GET은 쿼리 스트링 파라미터로 데이터를 보내기 때문에 url을 통해 데이터를 보냄
-   하지만 현재 요청은 데이터를 조회하는 것이 아닌 작성을 원하는 요청
-   GET이 아닌 다른 HTTP method를 알아보기

> **HTTP request method**

-   HTTP는 request method를 정의하여, 주어진 리소스에 수행하길 원하는 행동을 나타낸다.
-   **GET**
    -   특정 리소스를 가져오도록 요청할 때 사용
    -   반드시 데이터를 가져올 때만 사용해야 함
    -   DB에 변화를 주지 않음
    -   CRUD에서 **R 역할**을 담당
-   **POST**  
    -   서버로 데이터를 전송할 때 사용
    -   서버에 변경사항을 만듦
    -   리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
    -   GET의 쿼리 스트링 파라미터와 다르게 URL로 보내지지 않음
    -   CRUD에서 **C/U/D 역할**을 담당

**# 적용하기**

-   실제 네이버에서 로그인 부분을 확인해보면 GET이 아닌 POST를 사용하고 있는 것을 볼 수 있다.

![](https://blog.kakaocdn.net/dn/ukMni/btrLukyJU4e/pIwW3BZPe1R20DUg7pEwgK/img.png)

-   검색에서 GET을 사용한 이유가 뭘까?
    -   검색은 **서버에 영향을 미치는 것이 아닌 특정 데이터를 조회만 하는 요청이기 때문** 
    -   특정 페이지를 조회하는 요청을 보내는 HTML의 **'a tag' 또한 GET**을 사용
-   GET -> POST로 코드를 변경한 후 URL을 확인해보자. 쿼리 스트링 파라미터가 없어진 것을 볼 수 있다.

![](https://blog.kakaocdn.net/dn/brVqQC/btrLuCeO75s/QqkoLfz7pAhNaCdaVQpcHK/img.png)

![](https://blog.kakaocdn.net/dn/q7GVP/btrLvCMcNi8/RoxoT6uznjjm3Mzu71t8lk/img.png)

-   403 Forbidden 응답을 받았지만 이는 나중에 확인하고 요청된 URL(/articles/create/)을 확인
    -   개발자 도구 - NETWORK 탭 - Payload 탭의 Form-Data 확인

![](https://blog.kakaocdn.net/dn/cBBZAb/btrLsrFaXBK/EaUOKPU5LKVofCrtjbdkm0/img.png)

-   데이터의 담긴 위치가 바뀌었기 때문에 view함수에서도 수정이 필요하다.

![](https://blog.kakaocdn.net/dn/28TJB/btrLu9crLvv/LF4IvlR4liv7jVN1t5NeJ1/img.png)

> **정리**

-   GET은 단순히 조회하려는 경우
-   POST는 서버나 DB에 변경을 요청하는 경우

**# 참고**

> **403 Forbidden**

-   서버에 요청이 전달되었지만, 권한 때문에 거절되었다는 것을 의미
-   서버에 요청은 도달했으나 서버가 접근을 거부할 때 반환됨
-   즉, 게시글을 작성할 권한이 없다 -> Django 입장에서는 **"작성자가 누구인지 모르기 때문에 함부로 작성할 수 없다"**라는 의미
-   모델(DB)을 조작하는 것은 단순 조회와 달리 최소한의 신원 확인이 필요하기 때문

---

### 5. CSRF

-   **Cross-Site-Request-Forgery**
-   "사이트 간 요청 위조"
-   사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 **보안에 취약하게 하거나 수정, 삭제 등의 작업****을 하게 만드는 공격 방법**
-   실제 사례 - 2008년 옥x 개인정보 해킹 사건
    -   해커가 옥x 운영자에게 CSRF 코드가 포함된 가짜 사이트가 담긴 이메일을 보냄
    -   관리자는 해당 사이트에 정보를 입력하여 관련 정보가 해커에게 보내졌고, 해커는 관리자 권한을 얻어냄

> **CSRF 공격 방어**

-   **"Security Token 사용 방식 (CSRF Token)"**
    -   사용자의 데이터에 임의의 난수 값(token)을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송시키도록 함
    -   이후 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증
    -   일반적으로 데이터 변경이 가능한 **POST, PATCH, DELET Method** 등에 적용
    -   Django는 DTL에서 csrf_token 템플릿 태그를 제공

> **csrf_token 템플릿 태그**

![](https://blog.kakaocdn.net/dn/oZzdt/btrLvEiXOtO/yk4YkEUrtZx3ExYk5F564k/img.png)

-   해당 ㄷ태그가 없다면 Django 서버는 요청에 대해 403 forbidden으로 응답
-   템플릿에서 **내부 URL로 향하는 Post form을 사용하는 경우에 사용**
    -   **외부 URL로 향하는 POST form에 대해서는 CSRF 토큰이 유출되어 취약성**을 유발할 수 있기 때문에 사용해서는 안됨
-   태그 작성 후 확인해보면 **input type이 hidden**으로 작성되며 **value는 Django에서 생성한 hash 값**으로 설정 

![](https://blog.kakaocdn.net/dn/bbUrnj/btrLu3iYLcL/znfgMN0Qvwjn9qqEaA7Rv0/img.png)

![](https://blog.kakaocdn.net/dn/04IZj/btrLugiO9ux/X76wnq6MDrLGzoDZCf0ma1/img.png)

-   마지막으로 게시글을 작성하고 문제없이 저장되는지 확인해보자
-   **"csrf_token은 해당 POST 요청이 내가 보낸 것 인지를 검증하는 것"**


### **6. DELETE**

**# READ 2 (detail page)**

-   개별 게시글 상세 페이지 제작
-   모든 게시글마다 view function과 템플릿 파일을 만들 수는 없기 때문에 **글의 번호(pk)**를 활용하자

> **urls**

우선 URL로 특정 게시글을 조회할 수 있는 번호를 받자. 정수형이기 때문에 `**<int>**`를 이용해주었다.

![](https://blog.kakaocdn.net/dn/yXOeg/btrLulqUR40/6efYv9zQKhBEZC6kPd6dV0/img.png)

> **views**

view 함수에선 **Article.objects.get(pk=pk)**에서

    1. 오른쪽 pk는 variable routing을 통해 받은 pk

    2. 왼쪽 pk는 DB에 저장된 레코드의 id칼럼

![](https://blog.kakaocdn.net/dn/btM2d6/btrLlF5g37S/fqukwek9EkcKfVWkPnLiYK/img.png)

> **templates**

url에서 <int:pk>를 이용하여 번호를 받기 때문에 url주소와 함께 **article.pk** 정보를 함께 넘겨주어야 한다.

![](https://blog.kakaocdn.net/dn/OmEEF/btrLvKXMDdf/gxPKLPxSj3HHDLwX5FA82k/img.png)

![](https://blog.kakaocdn.net/dn/Ly4N6/btrLqcVPcyd/Mcec77DztK7QfakNibYIH1/img.png)

또한 게시글을 생성한 후 index 페이지가 아닌 detail페이지로 가기 위하여 redirect인자를 변경해줘 보자!

![](https://blog.kakaocdn.net/dn/bqZAbN/btrLuC0f0xS/wgqK7ZbaLyFFgT1E1tL6JK/img.png)

---

#### **# DELETE**

> **urls**

-   모든 글을 삭제하는 것이 아니라 **삭제하고자 하는 특정 글을 조회 후 삭제**해야 한다.

![](https://blog.kakaocdn.net/dn/Lwrc5/btrLuywOZOz/tGxyuG66NPvfYNs4bLzr9k/img.png)

> **views**

![](https://blog.kakaocdn.net/dn/Ckwdy/btrLvKcqFV4/4MiX1kE59NOGHSdCsA7O6k/img.png)

> **templates**

-   detail 페이지에 작성하며 DB에 영향을 끼치므로 **POST method 사용**

![](https://blog.kakaocdn.net/dn/bdPNhr/btrLuw6N9m1/usrt9x36brftjrmkpbsISk/img.png)

---

### **7. UPDATE**

-   수정은 CREATE 로직과 마찬가지로 2개의 view 함수가 필요하다.
    1.  사용자의 입력을 받을 페이지를 **렌더링**하는 함수 1개
        -   "edit" view function
    2.  사용자가 입력한 데이터를 전송받아 **DB에 저장**하는 함수 1개  
        -   "update" view function

> **edit : urls & views**

특정 글을 수정하므로 마찬가지로 **<int:pk>**를 받아준다.

![](https://blog.kakaocdn.net/dn/dppd3P/btrLk4jYDWB/UWpRRWVL6Gbj1WNq87UV4k/img.png)

> **edit : templates**

-   또한 수정을 처음부터 하는 것이 아닌 기존의 값에서 진행한다.
-   따라서 html 태그의 **value 속성을 사용**하여 기존에 입력되어 있던 데이터를 출력

![](https://blog.kakaocdn.net/dn/cfWmJ1/btrLk5b2Psm/1tdIYQ82au7G97vr3P7rfk/img.png)

-   Edit 페이지로 이동하기 위한 하이퍼 링크를 detail page에 작성해준다.

![](https://blog.kakaocdn.net/dn/bbGyV5/btrLtMCj8Xq/ayt8prVHuM7y9JWjKySxH0/img.png)

-   이후 Update를 위한 로직을 단계에 맞게 작성해주자.

![](https://blog.kakaocdn.net/dn/sbxcE/btrLtYirpvL/NVqhNpqxmK7pXk2HbWtOjK/img.png)

url

![](https://blog.kakaocdn.net/dn/DBKqM/btrLovg2UZ0/iEEsk6KL8LbgSj8rbgk7QK/img.png)

view

![](https://blog.kakaocdn.net/dn/vBrFv/btrLvDRVEzt/19fELnKSpXU51l7JJ69AEk/img.png)

template

여기까지 했다면 홈페이지 하나를 만들며 데이터를 처리하는 단계에 대해서 배웠기 때문에 실습을 해보는 걸 추천한다:)
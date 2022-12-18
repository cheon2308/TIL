웹 요청에 따른 인증 및 권한을 알아보기 전에 Django가 제공하는 built-in forms를 익히자

[https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.forms](https://docs.djangoproject.com/en/3.2/topics/auth/default/#module-django.contrib.auth.forms)



#### **목차**

1.  Login
2.  Authentication With User
3.  Logout

---

### **1. Login**

어떤 서비스를 이용하면서 회원가입과 로그인, 로그아웃을 해본 적이 있을 것이다.

Login을 개발자로서 설명하자면 **Session을 Create 하는** 과정이라고 말할 수 있다.

> **AuthenticationForm**

-   **로그인을 위한 built-in form**
    -   로그인하고자 하는 사용자 정보를 입력 받음
    -   기본적으로 username과 password를 받아 **데이터가 유효한지 검증**
-   **request를 첫 번째 인자**로 취함

**# 로그인 페이지 작성**

-   마찬가지로 url - view - templates의 흐름을 따라간다.

![](https://blog.kakaocdn.net/dn/bD6W5w/btrMkGB5pmi/t0FQf7ozf99BEHoUU88FnK/img.png)

![](https://blog.kakaocdn.net/dn/c3fCsv/btrMp2wRbqT/WUZPFWBvlqCeQzCU2PSUq1/img.png)

![](https://blog.kakaocdn.net/dn/Y610o/btrMoSBeJUk/ljDp18bT7NJ4sfD37Am1Xk/img.png)

> **login()**

```PYTHON
login(request, user, backend=None)
```

-   **인증된 사용자를 로그인 시키는 로직**으로 view 함수에서 사용됨
-   현재 세션에 연결하려는 인증 된 사용자가 있는 경우 사용
-   HttpRequest 객체와 User 객체가 필요

**# 로직 작성**

-   로그인 페이지 작성
-   view 함수 login과의 충돌을 방지하기 위하여 **import 한** **login 함수 이름**을 **auth_login**으로 변경해서 사용

![](https://blog.kakaocdn.net/dn/bH6ZvY/btrMkuhiTJg/85dN6pvEAquMetYJVJbWM0/img.png)

-   **get_user()**  
    -   AuthenticationForm의 인스턴스 메서드
    -   **유효성 검사를 통과**했을 경우 로그인 한 사용자 **객체를 반환**

> **세션 데이터 확인**

로그인 후 **개발자 도구**와 **DB**에서 django로부터 발급받은 **세션 확인** (로그인은 관리자 계정을 만든 후 진행)

1.  django_session 테이블에서 확인
2.  브라우저에서 확인
    -   개발자 도구 - Application - Cookies

![](https://blog.kakaocdn.net/dn/VT9Vi/btrMllc5tVV/yUKcu0YAXnyt1ne32xdYXK/img.png)

django-session 테이블

![](https://blog.kakaocdn.net/dn/bXgvN7/btrMlU0DAWr/Lm8bFNMa685ZSOF5CWwbDk/img.png)

개발자 도구

이전에도 봤듯이 편의를 위하여 base.html 템플릿에서 상속을 받아 사용하고 있다. 따라서 base 템플릿에 **로그인 페이지로 이동할** 수 있는 **하이퍼 링크 작성**

![](https://blog.kakaocdn.net/dn/cj5hWI/btrMqs993kR/kQm1hzMNN5NrdP0jXzloa1/img.png)

---

### **2. Authentication with User**

view.py와 urls.py에서 로그인을 위한 로직을 짰다면 이제 템플릿 (html)에서 **인증 관련 데이터를 출력**하는 방법을 알아보자.

> **현재 로그인되어있는 유저 정보 출력하기**

**1. 템플릿에서 인증 관련 데이터 출력**

-   accounts 앱이 아닌 base.html에서 {{ user }} 를 들고 오는데 어떻게 context도 받지 않고 가능할까?

![](https://blog.kakaocdn.net/dn/HZjKK/btrMtG7VJAg/7TkGj2AKfabUxXngsXQF9k/img.png)

**2. base 템플릿에서 context 데이터 없이 user 변수를 사용할 수 있는 이유**

-   settings.py의 **context processors** 설정 값 때문

> **context processors**

-   템플릿이 렌더링 될 때 호출 가능한 **컨텍스트 데이터 목록**
-   작성된 컨텍스트 데이터는 기본적으로 템플릿에서 **사용 가능한 변수**로 포함됨
-   즉, django에서 **자주 사용하는 데이터 목록**을 **미리 템플릿에 로드해** 둔 것

![](https://blog.kakaocdn.net/dn/AV9eo/btrMrS1Oqe2/w9d8rhKcdO1JO3G2fp4AGk/img.png)

-   현재 user 변수를 담당하는 프로세서는 **django.contrib.auth.context_processors.auth**
-   이외의 더 많은 Built-in template context processors들은 공식문서 참고
-   [https://docs.djangoproject.com/en/3.2/ref/templates/api/#built-in-emplate-context-processors](https://docs.djangoproject.com/en/3.2/ref/templates/api/#built-in-emplate-context-processors)


> django.contrib.auth.context_processors.auth  
> ****

-   현재 로그인한 사용자를 나타내는 **User 클래스의 인스턴스**가 템플릿 변수 **{{ user }}**에 저장됨
    -   클라이언트가 로그인하지 않은 경우 **AnonymousUser 클래스의 인스턴스**로 생성

![](https://blog.kakaocdn.net/dn/bSPFXo/btrMqsbe5G6/eh0vGGvFibrjlFslc3ZMs1/img.png)

로그인 상태와 비로그인 상태

---

### **3. Logout**

로그인이 Session의 Create과정이었다면, 로그아웃은 **Session을 Delete 하는** 과정

```PYTHON
logout(request)
```

-   **HttpRequest 객체를 인자**로 받고 **반환 값** **xxxxx**
-   사용자가 로그인하지 않은 경우 **오류를 발생시키지 xxxxxxx**
-   아래 2가지 일을 처리
    1.  현재 요청에 대한 session data를 DB에서 삭제
    2.  클라이언트의 쿠키에서도 sessionid를 삭제
        -   이는 다른 사람이 동일한 웹 브라우저를 사용하여 로그인하고, 이전 사용자의 세션 데이터에 액세스 하는 것을 방지하기 위함

**# 로직 작성**

![](https://blog.kakaocdn.net/dn/TZ2J2/btrMkgKp3LY/EBeosUk10ANzNHwDn3JEL0/img.png)

![](https://blog.kakaocdn.net/dn/A3VAo/btrMrxQWR2c/1TShFGGNIrWupyqjzjZCP1/img.png)

![](https://blog.kakaocdn.net/dn/bAG7U5/btrMkSWADe1/wKdRxBkUxdwdJHmd5KjEUK/img.png)
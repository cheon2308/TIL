앞서 회원가입, 로그인 등에 알아볼 수 있었다. 이번 글에서는 로그인 사용자에 대한 **접근 제한**에 대해 알아보자.

로그인 사용자에 대해 접근을 제한하는 방법은 아래 두 가지가 있다.

1.  The raw way
    -   is_authenticated attribute
2.  The login_required decorator

#### **목차**

1.  is_authenticated attribute
2.  The login_required decorator

---

### **1. is_authenticated attribute**

-   User model의 속성(attributes) 중 하나
-   사용자가 인증되었는지 여부를 알 수 있는 방법
-   모든 User 인스턴스에 대해 항상 True인 읽기 전용 속성
    -   **AnonymousUser**에 대해서는 항상 **False**
-   일반적으로 **request.user**에서 이 속성을 사용(request.user.is_authenticated)

**※ 권한(permission)과는 관련이 없으며, 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음**

![](https://blog.kakaocdn.net/dn/DW5Oi/btrNSCC7vUM/7V55V2em9qXDOObbA8enz1/img.png)

is_authenticated 코드 살펴보기

-   로그인과 비로그인 상태에서 출력되는 링크를 다르게 설정해줄 수 있다.

![](https://blog.kakaocdn.net/dn/2aX86/btrNSBEddvy/RYXh6GLEBykKNtBt01rqS1/img.png)

-   인증된 사용자만 게시글 작성 링크를 볼 수 있도록 처리해주자.
-   하지만 아직 비 로그인 상태로도 URL을 직접 입력하면 게시글 작성 페이지로 갈 수 있다.

![](https://blog.kakaocdn.net/dn/cndWX5/btrNNyCe54Z/maSh6njrkIbY6sJv2BTrz0/img.png)

-   인증된 사용자라면 로그인 로직을 수행할 수 없도록 처리한다.

![](https://blog.kakaocdn.net/dn/I6Uki/btrNMaoxRL2/XBrUsxJn5FPAL3Qzlue4cK/img.png)

---

### **2. login_required decorator**

-   사용자가 로그인 되어 있으면 정상적으로 view 함수를 실행
-   로그인하지 않은 사용자의 경우 settings.py의 LOGIN_URL 문자열 주소로 redirect
    -   **참고 - LOGIN_URL**의 기본 값은 /accounts/login/
    -   두 번째 app 이름을 accounts로 했던 이유 중 하나

-   로그인 상태에서만 글을 **C/U/D** 할 수 있도록 변경

![](https://blog.kakaocdn.net/dn/nXTad/btrNN0rLhw7/BKbrU0MpntbK0EpAAYW5hk/img.png)

-   login_required 적용을 확인해보자.
    1.  /articles/create/로 강제 접속 시도해보기
    2.  로그인 페이지로 리다이렉트 후 /accounts/login/?next=/articles/create/url 확인하기
-   인증 성공 시 사용자가 redirect 되어야 하는 경로는 "next"라는 쿼리 문자열 매개 변수에 저장됨
    -   예 - /accounts/login/?next=/articles/create

> **"next" query string parameter**

-   로그인이 정상적으로 진행되면 이전에 요청했던 주소로 redirect 하기 위해 Django가 제공해주는 **쿼리 스트링 파라미터**
-   해당 값을 처리할지 말지는 자유이며 별도로 처리해주지 않으면 view에 설정한 redirect 경로로 이동하게 됨

![](https://blog.kakaocdn.net/dn/ciXd6M/btrNOewG56V/Py5vRQuK6l4UU1km0BUlU0/img.png)

-   **주의사항**
    1.  만약 login 템플릿에서 form action이 작성되어 있다면 동작하지 않음
    2.  해당 action 주소 next 파라미터가 작성되어있는 현재 url이 아닌 /accounts/login/으로 요청을 보내기 때문

![](https://blog.kakaocdn.net/dn/Khqga/btrNSCQEEDc/kGLY40Osl1hluc4TsTcVKK/img.png)

> **두 데코레이터로 인해 발생하는 구조적 문제**

1.  먼저 비로그인 상태로 detail 페이지에서 게시글 삭제 시도
2.  delete view 함수의 **@login_required**로 인해 로그인 페이지로 리다이렉트
    -   http://127.0.0.1:8000/accounts/login/?next=/articles/1/delete/
3.  redirect로 이동한 로그인 페이지에서 로그인 진행
4.  delete view 함수의 **@require_POST**로 인해 405 상태 코드를 ㅂ다게 됨
    -   405(Method Not Allowed) status code 확인

-   로그인 성공 이후 GET method로 next 파라미터 주소에 리다이렉트 되기 때문

![](https://blog.kakaocdn.net/dn/bvg1Lr/btrNHT0wCCa/8JRNeWDcwqEprBWI446bX0/img.png)

-   아래 두 가지 문제가 발생한 것이다.
    1.  redirct 과정에서 POST 요청 데이터의 손실
    2.  redirect로 인한 요청은 GET 요청 메서드로만 요청됨
-   **해결방안**
    -   **@login_required는** GET request method를 처리할 수 있는 View 함수에서만 사용해야 함
    -   즉, POST method만 허용하는 delete 같은 함수는 내부에서는 is_authenticated 속성 값을 사용해서 처리

![](https://blog.kakaocdn.net/dn/clcv2x/btrNN0FjjDX/K9iMCRZna8aUSoXQi6XjA0/img.png)

![](https://blog.kakaocdn.net/dn/AtFJI/btrNQR1TZgK/n1iep0VrpVO4HUkMTWeeTK/img.png)
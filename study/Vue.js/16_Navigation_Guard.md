
#### **목차**

1.  전역 가드
2.  라우터 가드
3.  컴포넌트 가드
4.  404 Not Found

### **네비게이션 가드**

-   Vue router를 통해 특정 URL에 접근할 때 다른 url로 redirect를 하거나 해당 URL로의 접근을 막는 방법
    -   ex) 사용자의 인증 정보가 없으면 특정 페이지에 접근하지 못하게 함
-   https://v3.router.vuejs.org/guide/acvanced/navigation-guards.html

> **종류**

1.  전역 가드
    -   애플리케이션 전역에서 동작
2.  라우터 가드
    -   특정 URL에서만 동작
3.  컴포넌트 가드
    -   라우터 컴포넌트 안에 정의

---

### **1. 전역 가드**

> **Global Before Guard**

-   다른 url 주소로 이동할 때 항상 실행
-   router/index.js에 **router.beforeEach()**를 사용하여 설정
-   콜백 함수의 값으로 다음과 같이 3개의 인자를 받음
    -   **to :** 이동할 URL 정보가 담긴 Route 객체
    -   **from :** 현재 URL 정보가 담긴 Route 객체
    -   **next :** 지정한 URL로 이동하기 위해 호출하는 함수
        -   콜백 함수 내부에서 반드시 한 번만 호출되어야 함
        -   기본적으로 **to**에 해당하는 URL로 이동
-   URL이 변경되어 화면이 전환되기 전 **router.beforeEach()**가 호출됨
    -   화면이 전환되지 않고 대기 상태가 됨
-   변경된 URL로 라우팅하기 위해서는 **next()**를 호출해줘야 함
    -   **next()**가 호출되기 전까지 화면이 전환되지 않음

> Global Before Guard 실습

-   '/home'으로 이동하더라도 라우팅이 되지 않고 아래와 같이 로그만 출력됨
-   **next()**가 호출되지 않으면 화면이 전환되지 않음

![](https://k.kakaocdn.net/dn/3Q8gK/btrQKCu5UNI/rtRRTmDKv4KtpFyKXffsD1/img.png)

![](https://k.kakaocdn.net/dn/b9bXYK/btrQKuRi4OF/qAcpEysUcIXSaf7ScKiDB0/img.png)

-   **next()**가 호출되어야 화면이 전환됨

![](https://k.kakaocdn.net/dn/OWjA5/btrQMsrVxYg/QcKmP7VwKD2pZ1qGp0En6k/img.png)

-   About으로 이동해보기
    -   to에는 이동할 url인 about에 대한 정보가,
    -   from에는 현재 url인 home에 대한 정보가 들어있음

![](https://k.kakaocdn.net/dn/c0PGY9/btrQJIoX09f/SyKifQE94zzlG02jXts5x1/img.png)

> **Login 여부에 따른 라우팅 처리**

-   Login이 되어있지 않다면 Login 페이지로 이동하는 기능 추가

![](https://k.kakaocdn.net/dn/blgcTq/btrQOC1llC1/XJ4GwhY0gtcaK3hOL4ckuK/img.png)

-   LoginView에 대한 라우터 링크 추가

![](https://k.kakaocdn.net/dn/bkpVhO/btrQKbdmAX0/we0KK4v2d5OkKuFMvvgWS1/img.png)

-   HelloView에 로그인을 해야만 접근할 수 있도록 만들어 보기
-   로그인 여부에 대한 임시 변수 생성
-   로그인이 필요한 페이지를 저장
    -   로그인이 필요한 페이지들의 이름(라우터에 등록한 name)을 작성
-   앞으로 이동할 페이지(to)가 로그인이 필요한 사이트인지 확인

![](https://k.kakaocdn.net/dn/cAQ5qw/btrQOB9cIus/2o9QwKxQH9so2I3qw1mK2K/img.png)

-   isAuthRequired 값에 따라 로그인이 필요한 페이지이고 로그인이 되어있지 않으면
    -   Login 페이지로 이동
-   그렇지 않으면
    -   기존 루트로 이동
-   next() 인자가 없을 경우 to로 이동

![](https://k.kakaocdn.net/dn/c3m5AA/btrQOBuBZBS/EOEyVbk3tbFu594FQFRypk/img.png)

-   **isLoggedIn**이 **true**인 경우 (로그인 상태에서 로그인이 필요한 페이지로 접속)
    -   **/hello/harry**에 해당하는 컴포넌트가 정상적으로 렌더링

![](https://k.kakaocdn.net/dn/ccnq6a/btrQOyScaOn/b0GUAVQKdYof37Dykza4lK/img.png)

-   **isLoggedIn**이 **false**인 경우 (비로그인 상태에서 로그인이 필요한 페이지로 접속)
    -   **/hello/harry**을 렌더링하지 않고 Login 페이지로 이동됨

![](https://k.kakaocdn.net/dn/cHmLCo/btrQOlyPi3S/SJHk9Er3UomQfYdT1svEHK/img.png)

-   Home => Login으로 이동했는데 console창에 log가 2개가 찍힌 이유
    -   첫 번째 출력은 /hello/harry/로 접속 시도 후 (전역 가드에 막힘) 전역 가드에서 login으로 이동 요청 할 때 출력
    -   두 번째 출력은 /login으로 이동 요청 할 때 출력
-   **/hello/:userName** 페이지를 제외하고는 전역 가드에서 기존 주소로 이동하기 때문에 정상적으로 작동
-   로그인이 필요한 페이지에 추가하면 비로그인 시 해당 페이지에 접근 불가

![](https://k.kakaocdn.net/dn/wM7X1/btrQKCu85Fc/f7WJZRvdmA96HI1y43s3qk/img.png)

-   만약 view들이 여러 개라면 모두 추가해주어야 할까?
    -   반대로 Login하지 않아도 되는 페이지들을 모아 둘수도 있음

![](https://k.kakaocdn.net/dn/mJBb5/btrQOC79WcI/kizPdnfEZKrMxkwAGcPork/img.png)

---

### **2. 라우터 가드**

-   전체 route가 아닌 특정 route에 대해서만 가드를 설정하고 싶을 때 사용
-   **beforeEnter()**
    -   route에 진입했을 때 실행됨
    -   라우터를 등록한 위치에 추가
    -   단 매개변수, 쿼리, 해시 값이 변경될 때는 실행되지 않고 다른 경로에서 탐색할 때만 실행됨
    -   콜백 함수는 **to, from, next**를 인자로 받음

> **Login 여부에 따른 라우팅 처리**

-   "이미 로그인 되어있는 경우 HomeView로 이동하기"
-   라우터 가드 실습을 위해 전역 가드 실습코드는 주석처리
-   로그인 여부에 대한 임시 변수 생성
-   로그인이 되어있는 경우 home으로 이동
-   로그인이 되어있지 않은 경우 login으로 이동

![](https://k.kakaocdn.net/dn/8dxB5/btrQNJGZFxb/dEIsCIVYNIm6TDtYkGyJp1/img.png)

-   **isLoggedIn = true** 인 경우 (로그인 상태인 경우)  
    -   **/login**으로 접속을 시도하면 Home으로 이동

![](https://k.kakaocdn.net/dn/czeprf/btrQK0Jeg9D/wtavYJf0faYZqZbhuYqnkK/img.png)

-   Login을 제외한 다른 페이지로 이동하면 라우터 가드를 따로 설정해주지 않았기 때문에 라우터 가드가 동작하지 않음
-   이런식으로 특정 라우트만 따로 가드를 하고 싶은 경우에는 라우터 가드를 사용
-   isLoggedIn = false로 변경하면 Login페이지로 정상 이동 가능

---

### **3. 컴포넌트 가드**

-   특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
-   **beforeRouteUpdate()**
    -   해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행

> **Params 변화 감지**

-   about에서 jun에게 인사하는 페이지로 이동

![](https://k.kakaocdn.net/dn/b2aINQ/btrQOj8RxAm/LfbSilhbQv44sq4Hk2lSnk/img.png)

-   navbar에 있는 Hello를 눌러 harry에게 인사하는 페이지로 이동
    -   URL은 변하지만 페이지는 변화하지 않음

![](https://k.kakaocdn.net/dn/cLthti/btrQMsrYZze/xlijurQt6iZ7zrRTJV0MK1/img.png)

-   변화하지 않는 이유
    -   컴포넌트가 재사용되었기 때문
    -   기존 컴포넌트를 지우고 새로 만드는 것보다 효율적
        -   단, **lifecycle hook이 호출되지 않음**
        -   따라서 **$route.params**에 있는 데이터를 새로 가져오지 않음
-   **beforeRouteUpdate()**를 사용해서 처리
    -   userName을 이동할 params에 있는 userName으로 재할당

![](https://k.kakaocdn.net/dn/tVXGr/btrQK6W4N6t/u3cBLlkSVRRkg2XabahXRK/img.png)

---

### **4. 404 Not Found**

-   사용자가 요청한 리소스가 존재하지 않을 때 응답

![](https://k.kakaocdn.net/dn/b6NeU6/btrQKhLzcmi/PxfSksoGGpiKomaKKWE9C0/img.png)

-   http://localhost:8080/404 확인
-   이렇게 직접 요청하는 방식이 아닌, 요청한 리소스가 존재하지 않을 때 404로 이동하도록 하려면 어떻게 해야 할까?

> **요청한 리소스가 존재하지 않는 경우**

-   모든 경로에 대해서 404page로 redirect 시키기
    -   기존에 명시한 경로가 아닌 모든 경로가 404 page로 redirect 됨
    -   **이 때, routes에 최하단부에 작성해야 함** 

![](https://k.kakaocdn.net/dn/diuWJH/btrQKaZVGYX/v9KxAw3uLFI8KQSoaqWnfk/img.png)

> **형식은 유효하지만 특정 리소스를 찾을 수 없는 경우**

-   예) Django에게 **articles/1/**로 요청을 보냈지만, 1번 게시글이 삭제된 상태
    -   이 때는 **path: `***` 를 만나 404 page가 렌더링 되는 것이 아니라 기존에 명시한 **articles/:id/** 에 대한 components가 렌더링됨
    -   하지만 데이터가 존재하지 않기 때문에 정상적으로 렌더링이 되지 않음
-   해결책
    -   데이터가 없음을 명시
    -   404page로 이동해야 함
-   Dog API 문서(https://dog.ceo/dog-api/)를 참고하여 동적 인자로 강아지 품종을 전달해 품종에 대한 랜덤 이미지를 출력하는 페이지를 만들어보기

-   Axios 설치 - DogView 컴포넌트 작성 - routes에 등록
    -   `*` 보다 상단에 등록

![](https://k.kakaocdn.net/dn/svqH6/btrQOadiJMf/cxSkKrHR4vnvCcySO2Ru3K/img.png)

-   Dog api 문서를 참고하여 axios 로직을 작성

![](https://k.kakaocdn.net/dn/Snrsi/btrQK0CvlzX/tWvKwQyQxPZoy34tf0kEe0/img.png)

![](https://k.kakaocdn.net/dn/oZGL2/btrQK0JfvWG/OjDmQJwZcpGtAZgvYeki7k/img.png)

-   **/dog/hound**에 접속하면 hound 품종에 대한 랜덤 사진이 출력
-   axios 요청이 오는 중 동작하고 있음을 표현하기 위한 로딩 메시지 정의

![](https://k.kakaocdn.net/dn/b1HzkU/btrQOP0wZUU/ljWOCTZo5Wj6wFCg5JDlwk/img.png)

-   axios 요청이 실패할 경우 자료가 없음을 표현하기

![](https://k.kakaocdn.net/dn/bfQbxv/btrQK2tz7sF/DOYCbx9uiT97JneZKJkilk/img.png)

> **404 Not Found**

-   이전처럼 메세지를 바꿀수도 잇지만 axios 요청이 실패할 경우 404 페이지로 이동 시킬 수도 있음

![](https://k.kakaocdn.net/dn/IhXYo/btrQK7aAIyg/Edv7YmgKXYL9khUD9Yolfk/img.png)
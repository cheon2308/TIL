
#### **목차**

1.  Cross-Origin Resource Sharing
2.  How to set CORS

---

### **1. Cross-Origin Resource Sharing**

> **What Happened?**

-   브라우저가 요청을 보내고 서버의 응답이 브라우저에 도착
    -   Server의 log는 **200(정상)** 반환
    -   즉 Server는 정상적으로 응답했지만 브라우저가 막은 것
-   보안상의 이유로 브라우저는 **동일 출처 정책(SOP)**에 의해 다른 출처의 리소스와 상호작용 하는 것을 제한 함

> **SOP(Same - Origin Policy)**

-   "동일 출처 정책"
-   불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용 하는 것을 제한하는 보안 방식
-   잠재적으로 해로울 수 있는 문서를 분리함으로써 공격받을 수 있는 경로를 줄임
-   https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy

> **Origin - "출처"**

-   **URL의 Protocol, Host, Port를 모두 포함**하여 출처라고 부름
-   Same Origin 예시
    -   아래 세 영역이 일치하는 경우에만 동일 출처로 인정

![](https://blog.kakaocdn.net/dn/bcQ5eS/btrRaDFFLJc/DkPImi1ifDyZdyaDmlkf30/img.png)

-   **http://localhost:3000/posts/3/** 을 기준으로 출처를 비교

![](https://blog.kakaocdn.net/dn/dX7Urf/btrQ2d2OeyB/Ux66QAHi2Nt89nElqBQghk/img.png)

> **CORS - 교차 출처 리소스 공유**

-   추가 **HTTP Header**를 사용하여, 특정 출처에서 실행 중인 웹 어플리케이션이 **다른 출처의 자원에 접근할 수 있는 권한**을 부여하도록 브라우저에 알려주는 체제
    -   어떤 출처에서 자신의 컨텐츠를 불러갈 수 있는지 **서버에 지정**할 수 있는 방법
-   리소스가 자신의 출처와 다를 때 교차 출처 HTTP **요청**을 실행
    -   만약 다른 출처의 리소스를 가져오기 위해서는 이를 제공하는 서버가 브라우저에게 **다른 출처지만 접근해도 된다는 사실을 알려야 함**
    -   "교차 출처 리소스 공유 정책 (CORS policy)"
-   다른 출처에서 온 리소스를 공유하는 것에 대한 정책
-   CORS policy에 위배되는 경우 브라우저에서 해당 응답 결과를 사용하지 않음
    -   Server에서 응답을 주더라도 브라우저에서 거절
-   다른 출처의 리소스를 불러오려면 그 출처에서 **올바른 CORS header**를 포함한 응답을 반환해야함
-   https://developer.mozilla.org/ko/docs/Web/HTTP/CORS

---

### **2. How to set CORS**

-   CORS 표준에 의해 추가된 HTTP Response Header를 통해 이를 통제 가능
-   HTTP Response Header 예시
    -   Access-Control-Allow-Origin
    -   단일 출처를 지정하여 브라우저가 해당 출처가 리소스에 접근하도록 허용

> **django-cors-headers library 사용하기**

-   django-cors-headers github에서 내용 확인
    -   https://github.com/adamchainz/django-cors-headers
-   **응답에 CORS header****를 추가**해주는 라이브러리
-   다른 출처에서 Django 애플리케이션에 대한 브라우저 내 요청을 허용함
-   라이브러리 설치 및 **requirements.txt** 업데이트

![](https://blog.kakaocdn.net/dn/y0LEm/btrRb8y616r/No03nQxQQlq9xIGtXMTrUk/img.png)

-   **App** 추가 및 **MIDDLEWARE** 추가 주석 해제 
    -   **※ 주의 ) CorsMiddleware는 가능한 CommonMiddleware 보다 먼저 정의 되어야 함**

![](https://blog.kakaocdn.net/dn/bP1tzW/btrRbZ3fJQ6/s1YXhE6MckFfMegnJlEFE1/img.png)

-   **CORS_ALLOWED_ORIGINS**에 교차 출처 자원 공유를 허용할 Domain 등록

![](https://blog.kakaocdn.net/dn/p1VTK/btrQ4a52cyS/u9X6Mj9zgguvUxQecfrtt0/img.png)

-   만약 모든 Origin을 허용하고자 한다면

![](https://blog.kakaocdn.net/dn/Q8wTg/btrQ5j9wD2e/gx5Wkgwj3qsCxkGU24ZZd1/img.png)
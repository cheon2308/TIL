#### **목차**

1.  JS를 배워야 되는 이유 
2.  JS의 역사
3.  JS 실행환경 구성

---

### **1. JS를 배워야 하는 이유**

> **Web 기술의 기반이 되는 언어**

-   HTML 문서의 컨텐츠를 **동적으로 변경**할 수 있는 언어
-   Web이라는 공간에서 채팅, 게임 등 다양한 동작을 할 수 있게 된 기반

> **다양한 분야로 확장이 가능한 언어**

-   JS는 Web을 위해 탄생한 언어로서 버전이 올라가며 하나의 단단한 언어로 자리 매김
-   단순히 Web 조작을 넘어서 **서버 프로그래밍, 모바일 서비스, 컴퓨터 응용프로그래밍, 블록체인, 게임 개발 등 다양한 분야에서 활용이 가능한 언어**가 됨

> **2022년 현재, 가장 인기있는 언어**

![](https://blog.kakaocdn.net/dn/bIDusj/btrOQnE0kKd/Nk3mb2iLK89SoyhPVtArk1/img.png)

---

### **2. JS의 역사**

> **개요**

-   Web을 조작하기 위한 언어인 만큼 **Web Browser와도 깊은 연관 관계가 있음**
-   이러한 이유 때문에 JS를 처음 학습할 때 다양한 용어를 접하게 되는데 역사를 통해 전체적인 그림을 그려보고자 함

> **웹 브라우저의 역할**

-   URL을 통해 Web(WWW)을 탐색함
-   **HTML/CSS/JavaScript**를 이해한 뒤 해석해서 사용자에게 하나의 화면으로 보여줌
-   웹 서비스 이용 시 클라이언트의 역할을 함
-   즉, 웹 페이지 코드를 이해하고, 보여주는 역할ㅇ르 하는 것이 바로 웹 브라우저

> **웹 브라우저와 스크립트 언어**

-   **1993, Mosaic Web Browser**
    -   유저가 웹을 쉽게 탐색할 수 있게 버튼 등을 탑재한 GUI 기반의 웹 브라우저
-   **1994, Netscape Navigator**
    -   Mosaic Web Brower를 개선한 후속작, 시장 점유율 80% 차지
-   이 때까지만 해도 **정적 웹페이지를 단순히 보여주는 용도**에 그침
-   웹 브라우저에 탑재해서 웹 페이지를 동적으로 바꿔줄 Script 언어 개발 필요

**※ Script 언어?**

-   소스 코드를 기계어로 바꿔주는 컴파일러 없이 바로 실행 가능한 언어
-   속도가 느리다는 단점이 있음

-   Netscape에서 약 10일의 개발 기간을 통해 Script언어인 Mocha 개발
-   이후 LiveScript로 이름 변경 후 브라우저에 LiveScript를 해석해주는 Engine을 내장
-   이후 당시 인기있던 JAVA의 명성에 기대보고자 JavaScript로 이름 변경

-   **1995, Microsoft의 Internet Explorer**
    -   JavaScript를 그대로 복사한 JavaScriptcript라는 언어 제작 후 이를 탑재한 Web Browser인 Internet Explorer 출시
    -   이후 JavaScript와 JavaScriptcript는 각자의 기능을 추가하기 시작
    -   개발 자들은 Netscape Navigator와 Internet Explorer 각각에 대한 코드를 작성 해야하는 상황 맞이함
-   **1996-2000, ECMA 표준 발의**
    -   Netscape가 정보 통신에 관한 규약을 만드는 비영리 단체 ECMA에게 JavaScript 기반의 표준안 발의 제안, ECMAScript 1 출시
    -   이후 여러가지 문법이 추가되며 ECMAScript의 버전이 올라감
    -   이 상황을 지켜보던 Microsoft - "Windows에 기본적으로 Internet Explorer 탑재함"
    -   결국 시장 점유율 95% 이상으로 증가, ECMAScript 표준안 지키지 않겠다 선언
-   **2001-2004, 다양한 웹 브라우저의 등장**
    -   ActionScript3라는 스크립트 언어를 기반으로 한 Firefox 웹 브라우저 출시
    -   개발자 : Netscape Navigator & Internet Explorer & Firefox 지원 위해 고통
    -   이후 Opera등의 다양한 웹 브라우저가 계속 시장에 출시
    -   다양성으로 인해 더더욱 많은 개발자가 필요해졌고, 이는 집단 지성을 형성
-   **jQuery 등의 라이브러리 등장**
    -   각 브라우저의 엔진에 맞는 스크립트를 여러 번 작성하는 것이 고통
    -   **중간에 하나의 레이어**를 두고 코딩하는 것 = **jQuery**
        -   jQuery 문법에 맞춰 작성하면 브라우저별 엔진에 맞는 스크립트 변환은 jQuery가 알아서 변환
    -   이후 아주 많은 코드가 jQuery로 작성
-   **2008, Google의 Chrome 등장과 대통합의 시대**
    -   V8라는 강력한 엔진을 탑재한 Chrome 등장
        -   JavaScript 해석이 다른 웹 브라우저에 비해 월등히 빠름
        -   이로 인해 웹 브라우저가 버벅임이 없고 매우 빠르게 동작
    -   Chrome의 성능 앞에서 다른 웹 브라우저들이 함께 표준안을 만들자고 제안
-   **2009, ECMAScript5(ES5) 표준안 제정**
-   **2015, ECMAScript6(ES6) 표준안 제정**
-   이후에도 계속 버전 업데이트 중이나, **큰 변화**는 **ES6**에서 이루어짐

> **정리**

-   웹 브라우저는 JavaScript를 해석하는 엔진 가지고 있음
-   현재의 JavaScript는 이제 시장에서 자리를 잡은 언어이며, 개발에서 큰 축을 담당하는 언어
-   더 이상 jQuery등의 라이브러리를 사용할 필요가 없음(모든 웹 브라우저가 표준안을 따름)
-   **특히,**
    -   Chrome V8의 경우 JavaScript를 번역하는 속도가 매우 빠름
        -   Web Browser에서만 사용하지 말고 다른 개발에서도 활용해보자!
        -   node.JavaScript, react.JavaScript, electron 등의 내부 엔진으로 사용
        -   그 결과, back-end, mobile, desktop app등을 모두 JavaScript로 개발이 가능해짐

---

### **3. JS 실행환경 구성** 

> **Web Browser로 실행하기**

-   Web Browser에는 JavaScript를 해석할 수 있는 엔진이 있어 실행할 수 잇음
-   HTML 파일에 직접 jAVAsCRIPT를 작성 후 웹 브라우저로 열기

![](https://blog.kakaocdn.net/dn/ybOfv/btrOQBcjnVL/jnddc2JIYNq8dPwzuToil1/img.png)

-   Chrome의 개발자 도구 - Console 탭에서 결과 확인 가능

![](https://blog.kakaocdn.net/dn/SLaXl/btrO2pchidG/YrxMWhvbxzVmUYDe8wKaEk/img.png)

-   .JavaScript 확장자를 가진 파일에 JavaScript를 작성하고, 해당 파일을 HTML에 프로그래밍

![](https://blog.kakaocdn.net/dn/dUl9cO/btrODOjJL40/X8Bu3Eby4JYoFtlz5vbEd0/img.png)

-   웹 브라우저의 console에서 바로 JavaScript를 입력해도 된다 (엔진이 있으니까!)

![](https://blog.kakaocdn.net/dn/bL6lci/btrO0Ip3aku/qfUfs7dFRxUrhKafTAJ0a0/img.png)

-   특별하게 웹 브라우저에서 바로 실행할 수 있는 JavaScript 문법들을 **Vanilla JavaScript**라고 부름

> **Node.JavaScript로 실행하기**

-   웹 브라우저를 이용하지 않고 JavaScript를 실행할 수 있음 (엔진이 있으니까)
-   "Node.JavaScript 설치 하기 
    -   nodejs 홈페이지 -> LTS 버전 선택
    -   git bash 에서 설치 버전 확인

![](https://blog.kakaocdn.net/dn/bS1AWc/btrO0IwUF7u/MikKFNgLeIUIveMBx6IlK1/img.png)

#### **목차**

1.  사전 준비
2.  Front-end Development
3.  Why Vue
4.  Vue 2 vs Vue 3

---

### **1. 사전 준비**

  **1. VSCode Vetur extension 설치**

-   문법 하이라이팅, 자동완성, 디버깅 기능 제공

   **2. Chrome Vue devtools extension 설치 및 설정**

-   크롬 브라우저 개발자 도구에서 vue 디버깅 기능 제공
-   extension 설치 후 확장 프로그램 관리 - 파일 URL에 대한 액세스 허용

![](https://k.kakaocdn.net/dn/ewqmuh/btrP3kOj0UN/FHiKmlH6RFMJTd1oKKeQc0/img.png)

---

### **2. Front-end Development**

Back-end 개발은 Django로 진행, 따라서 앞으로 Javascript를 활용한 Front-end 개발에는 **Vue.js**로 진행한다.

-   **Vue.js === JavaScript Front-end Framework**

> **Front-end Framework**

-   Front-end(FE) 개발이란?
    1.  사용자에게 보여주는 화면 만들기
-   **Web App**(SPA)을 만들 때 사용하는 도구
    -   SPA - Single Page Application

> **Web App**

-   웹 브라우저에서 실행되는 어플리케이션 소프트웨어
-   ex) vibe 웹 사이트 이동
-   개발자 도구 -> 디바이스 모드

![](https://k.kakaocdn.net/dn/rBOSd/btrPU0XXdsT/e2AWH01SzGfcxlNfxWUiG1/img.png)

-   웹 페이지가 그대로 보이는 것이 아닌 **디바이스에 설치된 App**처럼 보이는 것
-   웹 페이지가 디바이스에 맞는 적절한 UX/UI로 표현되는 형태

> **SPA(Single Page Application)**

-   Web App과 함께 자주 등장할 용어 **SPA**
-   이전까지는 사용자의 요청에 적절한 페이지 별 template을 반환
-   SPA는 서버에서 **최초 1장의 HTML만 전달받아 모든 요청에 대응하는 방식**을 의미
    -   어떻게 한 페이지로 모든 요청에 대응 할 수 있을까?
    -   **CSR(Client Side Rendering)** 방식으로 요청을 처리하기 때문

**※ 참고 - SSR(Server Side Rendering) 이란?**

-   기존 요청 처리 방식은 SSR
-   Server가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
-   전달 받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행

![](https://k.kakaocdn.net/dn/swmZd/btrP3Sw0c0P/PM241DzwnuHp89JjltZS70/img.png)

![](https://k.kakaocdn.net/dn/LC0rr/btrP3mSVaBn/Z7SUSLlzAuOAtEJehOQGd0/img.png)

> **CSR (Client Side Rendering)**

-   최초 한 장의 HTML을 받아오는 것은 동일
    -   단, server로부터 최초로 받아오는 문서는 빈 html 문서

![](https://k.kakaocdn.net/dn/z12Mc/btrPU1CAxO5/SFKkg8vM6NTdxUYuIk6qCK/img.png)

-   각 요청에 대한 대응을 JavaScript를 사용하여 필요한 부분만 다시 렌더링
    1.  새로운 페이지를 서버에 **AJAX**로 요청
    2.  서버는 화면을 그리기 위해 필요한 데이터를 **JSON** 방식으로 전달
    3.  **JSON** 데이터를 JavaScript로 처리, DOM 트리에 반영(렌더링)

![](https://k.kakaocdn.net/dn/bUqEq2/btrP3AKbugG/iSV6DqSF0TL6a0146qxFtK/img.png)

![](https://k.kakaocdn.net/dn/C7Eqz/btrPWVhMxZS/VzWXkpUiuTxDYUeGjF60Kk/img.png)

> **왜 CSR 방식을 사용?**

1.  모든 HTML 페이지를 서버로부터 받는 것이 아니기 때문
    -   **클라이언트** - 서버간 통신 즉, 트래픽이 감소
    -   **트래픽이 감소**한다 = 응답 속도가 빨라진다.
2.  매번 새 문서를 받아 새로고침하는 것이 아니라 **필요한 부분**만 고쳐나가므로 각 요청이 끊김없이 진행
    -   SNS에서 추천을 누를 때 마다 첫 페이지로 돌아간다 = 끔찍!!
    -   요청이 자연스럽게 진행이 된다 = UX 향상
3.  BE와 FE의 작업 영역을 명확히 분리 할 수 있음
    -   각자 **맡은 역할을 명확히 분리**한다 = **협업이 용이**해짐

> **CSR은 만능일까?**

-   첫 구동 시 필요한 데이터가 많으면 많을수록 최초 작동 시작까지 오랜 시간이 소요
-   Naver, Netflix, Disney+ 등 모바일에 설치된 Web-App을 실행 하게 되면 잠깐의 로딩 시간이 필요
-   **검색 엔진 최적화**(SEO, Search Engine Optimization)가 어려움
    -   서버가 제공하는 것은 텅 빈 HTML
    -   내용을 채우는 것은 AJAX 요청으로 얻은 J**SON 데이터로 클라이언트(브라우저)가 진행**
-   대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움

**※ 참고 - SEO(Search Engine Optimization)**

-   google, bing과 같은 검색 엔진 등에 내 서비스나 제품 등이 **효율적으로 검색 엔진에 노출되도록 개선**하는 과정을 일컫는 작업
-   **검색** = 각 사이트가 운용하는 검색 엔진에 의해 이루어지는 작업
-   **검색 엔진** = 웹 상에 존재하는 가능한 모든 정보들을 긁어 모으는 방식으로 동작
    -   정보의 대상은 주로 HTML에 작성된 내용
    -   JavaScript가 실행된 이후의 결과를 확인하는 과정이 없음
-   최근에 SPA, 즉 CSR로 구성된 서비스의 비중이 증가
    -   SPA 서비스도 검색 대상으로 넓히기 위해 JS를 지원하는 방식으로 발전
-   단, 단순 HTML만을 분석하는 것보다 몇 배의 리소스가 필요한 작업이기에 여전히 CSR의 검색 엔진 최적화 문제가 모두 해결된 것은 아님

> **CSR vs SSR**

-   CSR과 SSR은 흑과 백이 아니다
    -   내 서비스에 적합한 렌더링 방식을 적절하게 활용할 수 있어야 한다.
-   SPA 서비스에서도 SSR을 지원하는 Framework도 발전하고 있는
    -   Vue의 Nuxt.js
    -   React의 Next.js
    -   Angular Universal 등

> **이런 프레임워크를 꼭 써야 하나?**

-   NO!!! 더 쉽게 개발하기 위해 사용하는 것
-   실제로 Github은 이러한 Front-end Framework를 사용하지 않음
-   하지만 **대부분의 기업**에서는 **생산성과 협업**을 위해 Framework를 사용해서 개발

---

### **3. Why Vue?**

> **Vue를 배우는 이유**

-   쉽다.
-   Vue는 타 Framework에 비해 입문자가 시작하기에 좋은 Framework
-   왜 Vue는 상대적으로 낮은 진입 장벽을 가질 수 있었을까?
-   구글의 Angular 개발자 출신이 Angular보다 **가볍고, 간편하게 사용할 수 있는**Framework를 만들기 위해 퇴사 후 Vue 발표
-   Vue를 활용한 실 사례

![](https://k.kakaocdn.net/dn/pgzzS/btrP2pboI1e/5IXDHBtNEoKnssT0ti46u1/img.png)

> **Vue가 쉬운 이유**

-   Vue 구조는 매우 직관적임
-   FE Framework를 빠르고 쉽게 학습하고 활용 가능
-   추후 필요하다면, 다른 FE Framework 학습 시 빠르게 적응 가능

![](https://k.kakaocdn.net/dn/JD1Sz/btrPUZZaOtZ/sARqf5rWwksth7FlpfDsF0/img.png)

-   Vue 없이 코드를 작성한다면, 태그에 값을 추가할 때, 기존에 가지고 있던 text도 신경 써야한다.
    -   즉, data를 관리하기 위한 추가 작업이 필요하다.

> **Vue CDN**

-   Vue로 작업을 시작하기 위해서는 CDN을 가져와야 한다.
-   Django == Python Web Frame work
    -   pip install
-   Vue == JS Front-end Framework
    -   Bootstrap에서 사용하였던 CDN 방식 제공

-   Vue CDN을 위하여 Vue2 공식 문서 접속  
    -   https://v2.vuejs.org/
    -   Getting Started
    -   Installation
    -   Development version CDN 복사

> **Vue로 코드 작성하기**

1.  Vue CDN 가져오기
2.  Vue instance 생성
    -   Vue instance - 1개의 Object
    -   정해진 속성명을 가진 Object
3.  **el, data** 설정
    -   data에 관리할 속성 정의
4.  선언적 렌더링 **{{ }}**
    -   Vue data를 화면에 렌더링
5.  input tag에 v-model 작성
    -   input에 값 입력 -> Vue data 반영
    -   Vue data => Dom 반영

**※ Dev Tools 확인**

-   Vue devtools에서 data 변경 -> DOM 반영
-   눈에 보이는 화면을 조작하는 것이 아닌 Vue가 가진 data를 조작

-   Vue를 통해 데이터를 관리한다면? = 변경 사항도 한 번에 반영

![](https://k.kakaocdn.net/dn/sDM1D/btrPVEOhF9N/2Km9o5yZKSmqf3jzXIcYx0/img.png)

---

### **4. Vue 2 vs Vue 3**

> **Vue3**

-   2022년 02월 부터 vue 프레임워크의 기본 버전이 3버전으로 전환
-   대체적인 설정들이 Vue3을 기본으로 적용되어 잇음
    -   ex) 공식문서, CDN, npm 등

> **Vue2**

-   여전히 vue2가 많이 사용됨 (legacy code)
-   사용된 기간이 긴 만큼 상대적으로 많은 문서의 양, 참고자료, 질문/답변
-   안정적 측면에서 아직 vue2가 우세
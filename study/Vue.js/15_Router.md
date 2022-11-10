
#### **목차**

1.  Routing
2.  Router
3.  실습

---

### **1. Routing**

-   네트워크에서 경로를 선택하는 프로세스
-   웹 서비스에서의 라우팅
    -   유저가 방문한 URL에 대해 적절한 결과를 응답하는 것
-   예시
    -   **/articles/index/** 에 접근하면 articles의 index에 대한 결과를 보내줌

> **Routing in SSR**

-   Server가 모든 라우팅을 통제
-   URL로 요청이 들어오면 응답으로 완성된 HTML 제공
    -   Django로 보낸 요청의 응답 HTML은 완성본인 상태였음
-   결론적으로, Routing(URL)에 대한 결정권을 서버가 가짐

> **Routing in  SPA / CSR**

-   서버는 하나의 HTML(index.html) 만을 제공
-   이후에 모든 동작은 하나의 HTML 문서 위에서 JavaScript 코드를 활용
    -   DOM을 그리는데 필요한 추가적인 데이터가 있다면 axios와 같은 AJAX 요청을 보낼수 있는 도구를 사용하여 데이터를 가져오고 처리
-   즉, **하나의 URL만 가질 수 있음** 

> **Why routing?**

-   그럼 동작에 따라 URL이 반드시 바뀌어야 하나?
    -   No !! 단, 유저의 사용성 관점에서는 필요함
-   Routing이 없다면,
    -   유저가 URL을 통한 페이지의 변화를 감지할 수 없음
    -   페이지가 무엇을 렌더링 중인지에 대한 상태를 알 수 없음
        -   새로고침 시 처음페잉지로 돌아감
        -   링크를 공유할 시 처음 페이지만 공유 가능
    -   브라우저의 뒤로 가기 기능을 사용할 수 없음

---

### **2. Vue Router**

-   Vue의 공식 라우터
-   SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공
-   라우트(routes)에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
    -   즉, SPA의 단점 중 하나인 **"URL이 변경되지 않는다."**를 해결
-   ※ 참고 - MPA (Multiple Page Application)
    -   여러 개의 페이지로 구성된 애플리케이션
    -   SSR 방식으로 렌더링

> **시작하기**

![](https://k.kakaocdn.net/dn/bASYU4/btrQMsqV8Dg/QceKliImS8lJK7x7opgInk/img.png)

![](https://k.kakaocdn.net/dn/cWlVJ8/btrQKiCzP9Q/LVuIwXYY6z8eM9sLMAvbl1/img.png)

> **History mode**

-   브라우저의 History API를 활용한 방식
    -   새로고침 없이 URL 이동 기록을 남길 수 있음
-   우리에게 익숙한 URL 구조로 사용 가능
    -   예) https://localhost:8080/index

**※ 참고 - History mode를 사용하지 않으면 Default 값인 hash mode로 설정됨('#'을 통해 URL을 구분하는 방식)**

-   예 - http://localhost:8080#index

> **App.vue**

-   router-link 요소 및 router-view가 추가됨

![](https://k.kakaocdn.net/dn/cWjyiO/btrQJPUYUcK/jKLSO3y61ZvPVGwMJPLn51/img.png)

-   **router/index.js** 생성
-   **views** 폴더 생성

![](https://k.kakaocdn.net/dn/cwMUlu/btrQI79VujC/Lyc7hwY34kLsydvGILE3DK/img.png)

> **router-link**

-   a 태그와 비슷한 기능 => URL을 이동시킴
    -   routes에 등록된 컴포넌트와 매핑됨
    -   히스토리 모드에서 router-link는 클릭 이벤트를 차단하여 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
-   목표 경로는 **'to'** 속성으로 지정됨
-   기능에 맞게 HTML에서 a 태그로 rendering 되지만, 필요에 따라 다른 태그로 바꿀 수 있음

> **router-view**

-   주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트
-   실제 component가 DOM에 부착되어 보이는 자리를 의미
-   router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링

-   Django에서의 block tag와 비슷함
    -   App.vue는 base.html의 역할
    -   router-view는 block 태그로 감싼 부분

> **src/router/index.js**

-   라우터에 관련된 정보 및 설정이 작성 되는 곳
-   Django에서의 urls.py에 해당
-   routes에 URL와 컴포넌트를 매핑
-   Django와의 비교

![](https://k.kakaocdn.net/dn/bgM5Oh/btrQI727SVH/zs51fAP9Lm8gOW8C8zhtnK/img.png)

![](https://k.kakaocdn.net/dn/JBAtg/btrQJhqSots/kpEB9KqBAmpeJABIwblnL1/img.png)

> **src/Views**

-   router-view에 들어갈 component 작성
-   기존에 컴포넌트를 작성하던 곳은 components 폴더 뿐이었지만 이제 두 폴더로 나뉘어짐
-   각 폴더 안의 .vue 파일들이 기능적으로 다른 것은 아님
-   이제 폴더별 컴포넌트 배치는 아래와 같이 진행 (**규약은 아님**)

-   **views/**  
    -   routes에 매핑되는 컴포넌트, 즉 `<**router-view**>의 위치에 렌더링 되는 컴포넌트를 모아두는 폴더
    -   다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것을 권장
    -   ex) App 컴포넌트 내부의 AboutView & HomeView 컴포넌트
-   **components/**
    -   routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더
    -   ex) HomeView 컴포넌트 내부의 HelloWorld 컴포넌트

---

### **3. 실습**

> **주소를 이동하는 2가지 방법**

1.  선언적 방식 네비게이션
2.  프로그래밍 방식 네비게이션

> **선언적 방식 네비게이션**

-   router-link의 **'to'** 속성으로 주소 전달
    -   routes에 등록된 주소와 매핑된 컴포넌트로 이동

![](https://k.kakaocdn.net/dn/d0USIc/btrQJn5Wq1E/u95moDuI3jv1MEGLPhGvT0/img.png)

-   동적인 값을 사용하기 때문에 **v-bind**를 사용해야 정상적으로 작동

![](https://k.kakaocdn.net/dn/bPWmfq/btrQK09LzEZ/K60NDCIvtccgqtuMJUWbDK/img.png)

> **Named Routes**

-   이름을 가지는 routes
    -   Django에서 path 함수의 name 인자의 활용과 같은 방식

![](https://k.kakaocdn.net/dn/MqomO/btrQNHhxJ6h/hp0hn005fbteyRXGz5HmSK/img.png)

> **프로그래밍 방식 네비게이션**

-   Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`**로 접근 할 수 있음
-   다른 URL로 이동하려면 **this.$router.push**를 사용
    -   history stack에 이동할 URL을 넣는(push) 방식
    -   history stack에 기록이 남기 때문에 사용자가 브라우저의 뒤로 가기 버튼을 클릭하면 이전 URL로 이동할 수 있음
-   결국 **`<router-link :to="...">`** 를 클릭하는 것과 `router.push(...)`**를 호출하는 것은 같은 동작
-   동작 원리는 선언적 방식과 같음

![](https://k.kakaocdn.net/dn/dL7bT8/btrQMsrqG67/MywLgqsla0df86h2Cgl2Ok/img.png)

![](https://k.kakaocdn.net/dn/bHbDhj/btrQNKeiDGd/7liKpPFVcxANEn91n0CLN1/img.png)

> **Dynamic Route Matching**

-   동적 인자 전달
    -   URL의 특정 값을 변수처럼 사용할 수 있음
    -   ex) Django에서의 variable routing
-   HelloView.vue 작성 및 route 추가
-   route를 추가할 때 동적 인자를 명시

![](https://k.kakaocdn.net/dn/OYnBt/btrQJjph40l/ZeGRgZNGks4Vb5EcUu9tQK/img.png)

![](https://k.kakaocdn.net/dn/bTqIzu/btrQN9x7Ec2/XbrlcJGzKNRC2lEtmxihJ1/img.png)

-   `**$route.params**` 로 변수에 접근 가능

![](https://k.kakaocdn.net/dn/byqHRt/btrQOacKIJu/SKyJLyitfAX8TE8BkwdT2k/img.png)

-   다만 HTML에서 직접 사용하기 보다는 data에 넣어서 사용하는 것을 권장

![](https://k.kakaocdn.net/dn/bGjK8l/btrQMxsLfih/1yakpF2gXHOFlZCzt1N4uk/img.png)

> **Dynamic Route Matching - 선언적 방식 네비게이션**

-   App.vue에서 harry에게 인사하는 페이지로 이동해보기
-   params를 이용하여 동적 인자 전달 가능

![](https://k.kakaocdn.net/dn/b5G5nh/btrQKbqtA8b/UccgWzRK8dFnTWmm5xjsUk/img.png)

> **Dynamic Route Matching - 프로그래밍 방식 네비게이션**

-   AboutView에서 데이터를 입력 받아 HelloView로 이동하여 입력받은 데이터에게 인사하기

![](https://k.kakaocdn.net/dn/bJce1o/btrQK8z5CFI/PmqybBF0uBBqEJTZyzQ5d0/img.png)

![](https://k.kakaocdn.net/dn/3snc7/btrQJiw9HGK/cSL9lSNC7sEk9IOCZstwf1/img.png)

> **route에 컴포넌트를 등록하는 또 다른 방법**

-   router/index.js에 컴포넌트를 등록하는 또 다른 방식이 주어지고 있음(about)

![](https://k.kakaocdn.net/dn/oMadT/btrQNIt3T1J/6i5PAksz6IitUWy4e53h81/img.png)

> **lazy-loading**

-   모든 파일을 한 번에 로드하려고 하면 모든 걸 다 읽는 시간이 매우 오래 걸림
-   미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식을 활용할 수 있음
    -   모든 파일을 한 번에 로드하지 않아도 되기 때문에 최초에 로드하는 시간이 빨라짐
    -   당장 사용하지 않을 컴포넌트는 먼저 로드하지 않는 것이 핵심
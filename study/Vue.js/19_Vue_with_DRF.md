
### **1. Again DRF**

-   lab.ssafy의 **Skeleton code 확인**
-   Model 구조 확인

![](https://blog.kakaocdn.net/dn/bhsaWD/btrQ4Xrk25x/KY9DLjwkiNuHEpEPJxbUR0/img.png)

-   요청 경로 확인

![](https://blog.kakaocdn.net/dn/nRRIq/btrQ0YEZEng/258T55Eu7fu47qGqgkUTTk/img.png)

-   미리 준비해둔 Dummy data 확인 및 데이터 삽입

![](https://blog.kakaocdn.net/dn/b4UAHD/btrQ28tkHyJ/3E5vw7wyjUeoqrSo0XK8Vk/img.png)

![](https://blog.kakaocdn.net/dn/teJVl/btrRaFi9oF3/LJTWNE9oyewKzz7882LHr1/img.png)

-   서버 실행 후, 전체 게시글 조회
    -   Browser에서 serve에 전체 게시글 조회 요청 => 데이터 반환 확인
    -   Postman에서 올바른 방법으로 요청 => 데이터 반환 확인

![](https://blog.kakaocdn.net/dn/P271N/btrQ1lNrREi/DU5ZOkbCrf0hRxSO8a7Kfk/img.png)

---

### **2. Back to Vue**

-   Skeleton code 확인
-   **front-server** 폴더 구조 확인 및 서버 구동 준비

![](https://blog.kakaocdn.net/dn/6YdWF/btrQ6HIARfJ/OoySt2qnKWoOuKCBwIkXjk/img.png)

-   컴포넌트 구조 확인

![](https://blog.kakaocdn.net/dn/bPfPpI/btrQ0SkvZe4/rDkBdkkhTSJDtFPZT7MuJ0/img.png)

> **메인 페이지 구성**

-   **views/ArticleView.vue** component 확인 및 route 등록

![](https://blog.kakaocdn.net/dn/cJ0L7j/btrQ0R60cUS/u1AeQQC3tsJw4OMpwyuRI1/img.png)

-   **src/App.vue** router-link 주석 해제 및 결과 확인

![](https://blog.kakaocdn.net/dn/beyEzd/btrQ5kmxv84/cpF5lTwUG57or6d0IEBIKk/img.png)

-   **components/ArticleList.vue** 확인  
    -   전체 게시물을 표현할 컴포넌트
    -   화면 구성을 위한 최소한의 style 포함

![](https://blog.kakaocdn.net/dn/FROCz/btrQ3UuUef9/Wfo3b4d3dI2T3DDbe9Cn1K/img.png)

-   **views/ArticleView.vue** 주석 해제
-   'ArticleList' 하위 컴포넌트 등록
    1.  불러오기
    2.  등록하기
    3.  보여주기

![](https://blog.kakaocdn.net/dn/dvuVx3/btrQ66VSolR/1g3XOEqoX8wZzbN4TeJWw0/img.png)

-   **components/ArticleListItem.vue** 확인  
    -   각 게시글들의 정보를 표현할 컴포넌트
    -   데이터 없이 최소한의 기본 구조만 확인

![](https://blog.kakaocdn.net/dn/b6dZmV/btrQ1mlhqTh/ogBObEBeyYfLG7zQUhZt6K/img.png)

-   **components/ArticleList.vue** 주석 해제
-   'ArticleListItem' 하위 컴포넌트 등록
    1.  불러오기
    2.  보여주기
    3.  등록하기

![](https://blog.kakaocdn.net/dn/cLLL13/btrRa2ektzm/mJlgPNlzXDJxyJzYh4YnkK/img.png)

-   **store/index.js** 주석 해제
-   state에 articles 배열 정의
-   화면 표현 체크용 데이터 생성

![](https://blog.kakaocdn.net/dn/bmiBSz/btrRa2ek1nm/5pckkWQ9nXLHlHz8ehzwP1/img.png)

-   **components/ArticleList.vue** 코드 수정  
    -   state에서 articles 데이터 가져오기
    -   v-for 디렉티브를 활용하여 하위 컴포넌트에서 사용할 article 단일 객체 정보를 pass props

![](https://blog.kakaocdn.net/dn/U0Ses/btrQ66Bywvc/84UaDCHjkLb4QqlKXgP1y1/img.png)

-   **components/ArticleListItem.vue** 수정  
    -   내려 받은 prop 데이터로 화면 구성
    -   prop 데이터의 타입은 명확하게 표기할 것

![](https://blog.kakaocdn.net/dn/0Jj3W/btrQ3TisDRy/1kOE4hA33GV2u5oYOApRx0/img.png)

---

### **3. Vue with DRF**

> **AJAX 요청 준비**

-   **axios** 설정  
    -   설치 -> npm install axios
    -   **store/index.js**에서 불러오기
        -   요청 보낼 API server 도메인 변수에 담기

![](https://blog.kakaocdn.net/dn/yJ4aC/btrQ2etL0aq/kArbB8sVBSpkMLjAlP1LiK/img.png)

-   **store/index.js** 주석 해제  
    -   'getArticles' 메서드 정의
    -   요청 보낼 경로 확인 필수
    -   성공 시 .then
    -   실패 시 .catch

![](https://blog.kakaocdn.net/dn/qlCMy/btrQ3TbFXWi/RJ7H2x3JOWX7RdYuaGku9K/img.png)

-   **views/ArticleView.vue** 주석 해제  
    -   'getArticles' actions 호출
    -   인스턴스가 생성된 직후 요청을 보내기 위해 **created()** hook 사용

![](https://blog.kakaocdn.net/dn/b67mFn/btrRa2SWP8f/UyJ6uggGZTR27yCRY0SrF1/img.png)

> **요청 결과 확인**

-   Vue와 Django 서버를 모두 켠 후 메인 페이지 접속
-   Server에서는 200을 반환하였으나 Client Console에서는 Error를 확인

![](https://blog.kakaocdn.net/dn/cr1hE2/btrQ0YrtnCH/ru69KGwQiTdyVXKSt2ljH0/img.png)
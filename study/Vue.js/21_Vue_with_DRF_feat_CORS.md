
### **1. Article Read**

-   응답 받은 데이터 구조 확인
    -   **'data Array'**에 각 게시글 객체
    -   각 게시글 객체는 다음으로 구성
        1.  id
        2.  title
        3.  content

![](https://blog.kakaocdn.net/dn/nvSE0/btrRc8SVMbY/MofxBscuUw3MRAj3krdcxK/img.png)

-   **store/index.js** 수정  
    -   기존 articles 데이터 삭제
    -   Mutations 정의
        -   응답 받아온 데이터를 state에 저장

![](https://blog.kakaocdn.net/dn/MhNKD/btrQ4a6jeaA/4QIkxAzpD26tcZMO5pi2b0/img.png)

---

### **2. Article Create**

-   **views/CreateView.vue** 코드 확인  
    -   게시글 생성을 위한 form을 제공
    -   **v-model.trim**을 활용해 사용자 입력 데이터에서 공백 제거
    -   **.prevent**를 활용해 form의 기본 이벤트 동작 막기

![](https://blog.kakaocdn.net/dn/epDRkB/btrQ9bXX6yl/ByDhxOsQaK6GFf5GRoe6uK/img.png)

-   **views/CreateView.vue** 코드 확인  
    -   title, content가 비었다면 **alert**를 통해 경고창을 띄우고
    -   **AJAX** 요청을 보내지 않도록 **return** 시켜 함수를 종료

![](https://blog.kakaocdn.net/dn/bz0qYP/btrRdBnipOn/tyF6qinBrZG3y2ttJmk4bK/img.png)

-   **views/CreateView.vue** 코드 확인  
    -   axios를 사용해 server에 게시글 생성 요청
-   **actions**를 사용하지 않나요?
    -   **state**를 변화 시키는 것이 아닌 DB에 게시글 생성 후, **ArticleView**로 이동할 것이므로 **methods**에서 직접 처리

![](https://blog.kakaocdn.net/dn/bfn2gk/btrQ4XeQ89g/BKZXbNnmDyRx7okFGxqiEK/img.png)

-   **router/index.js** 주석 해제

![](https://blog.kakaocdn.net/dn/bbHDPJ/btrRc9kiHir/UFNiFNGBwQrL35GP5NUe21/img.png)

-   **views/ArticleView.vue** 주석 해제  
    -   router-link를 통해 CreateView로 이동

![](https://blog.kakaocdn.net/dn/barTd7/btrRa1OjGHc/8u2FvvFjIzVRkCvuVmPcbk/img.png)

-   **views/CreateView.vue 코드 수정**  
    -   **createArticle method** 수정 게시글 생성 완료 후, ArticleView로 이동
-   응답 확인을 위해 정의한 인자 **res** 제거

![](https://blog.kakaocdn.net/dn/9HwME/btrQ5l7VlFe/M5es7ZKd71GdNyfosE5RR1/img.png)

-   게시글 작성 요청 결과 재확인
    -   게시글 생성 후, **ArticleView**로 이동
    -   새로 생성된 게시글 확인 가능
-   어떻게 router로 이동만 했는데 보일까?
    -   **ArticleView**가 create 될 때 마다 server에 게시글 전체 데이터를 요청하고 있기 때문

**※ 참고 - 지금의 요청 방식은 효율적인가?**

-   비효율적인 부분이 존재
    -   전체 게시글 정보를 요청해야 새로 생성된 게시글을 확인 할 수 있음
    -   만약 vuex state를 통해 전체 게시글 정보를 관리하도록 구성한다면?
    -   내가 새롭게 생성한 게시글은 확인할 수 있겠지만...
    -   나 이외의 유저들이 새롭게 생성한 게시글은 언제 불러 와야 할까?
    -   무엇을 기준으로 새로운 데이터가 생겼다는 것을 확인 할 수 있을까?
-   내가 구성하는 서비스에 따라 데이터 관리 방식을 고려해 보아야 함

---

### **3. Article Detail**

-   **views/DetailView.vue** 코드 확인  
    -   게시글 상세 정보를 표현할 컴포넌트
    -   AJAX 요청으로 응답 받아올 article의 상세 정보들을 표현

![](https://blog.kakaocdn.net/dn/bkYKTa/btrRcPfioBU/1TaNpj7xZe1kwC18KGEmvk/img.png)

-   **router/index.js** 주석 해제  
    -   id를 동적 인자로 입력 받아 특정 게시글에 대한 요청

![](https://blog.kakaocdn.net/dn/Kj32m/btrQ4aZRY0q/m1kHQ4PSXeUmGwqh1vqJO0/img.png)

-   **components/ArticleListItem.vue** 주석 해제  
    -   router-link를 통해 특정 게시글의 id 값을 동적 인자로 전달
    -   게시글 상세 정보를 Server에 요청

![](https://blog.kakaocdn.net/dn/bxVFM0/btrQ4bxHImU/Rx4XAhX527OxTYmf8j4uH1/img.png)

-   **views/DetailView.vue** 코드 확인  
    -   **this.$route.params**를 활용해 컴포넌트가 create될 때, 넘겨받은 id로 상세 정보 AJAX 요청

![](https://blog.kakaocdn.net/dn/A9Gjr/btrRb8zINRp/GAWkBqvtZDEqK0OSduqMy0/img.png)

-   **views/DetailView.vue** 수정  
    -   응답 받은 정보를 data에 저장
    -   data에 담기까지 시간이 걸리므로 optional chaining을 활용해 데이터 표기

![](https://blog.kakaocdn.net/dn/bPEi2o/btrRcGJEs1O/9SiBMsJrf2UBlv7rBGX4bK/img.png)
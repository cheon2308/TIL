
지금까지 배운 내용들을 종합하여 Django에서 만들었던 게시판 만들어보자

-   구현기능
    -   Index
    -   Create
    -   Detail
    -   Delete
    -   404
-   컴포넌트 구성

![](https://k.kakaocdn.net/dn/5VVEk/btrQOktbGJ4/8MwXej0Blin0R0vKQql18K/img.png)

#### **목차**

1.  Index
2.  Create
3.  Detail
4.  Delete
5.  404 Not Found

#### **사전 준비**

-   프로젝트 시작

```
vue create articles
cd articles
vue add vuex
vue add router
```

-   App.vue는 아래 코드만 남김 (CSS 코드 유지)

![](https://k.kakaocdn.net/dn/TutAy/btrQN7nme2a/KYDSFSPIvpon4Gv2LF8881/img.png)

---

### **1. Index**

> **구현**

-   state
-   게시글의 필드는 id, 제목, 내용, 생성일자
-   DB의 **AUTO INCREMENT**를 표현하기 위해 **article_id**를 추가로 정의해줌 (다음 article의 id로 사용 예정)

![](https://k.kakaocdn.net/dn/v150k/btrQOzXXrqv/DQxPtLC7y06s0OugszS8ck/img.png)

-   IndexView 컴포넌트 및 라우터 작성

![](https://k.kakaocdn.net/dn/cjYWm6/btrQKhENhxM/OHirSLLvUT268jI6pX68BK/img.png)

-   state에서 불러온 articles 출력하기

![](https://k.kakaocdn.net/dn/bRIfP7/btrQNGQ59EL/vIZXsGYbmNIdmKRhY28fo1/img.png)

-   ArticleItem 컴포넌트 작성

![](https://k.kakaocdn.net/dn/bAs1vh/btrQK79xm3v/mHXv0dqTKIJiZF6CXLMWhk/img.png)

-   IndexView 컴포넌트에서 ArticleItem 컴포넌트 등록 및 props 데이터 전달

![](https://k.kakaocdn.net/dn/bf9bSw/btrQOQ6em6E/jk7XKeeeNOIkqbrmSGHbMK/img.png)

-   props 데이터 선언 및 게시글 출력

![](https://k.kakaocdn.net/dn/o0bMi/btrQKvCMtfw/OL1uya8FxxI14GijVMxPk0/img.png)

---

### **2. Create**

-   CreateView 컴포넌트 및 라우터 작성

![](https://k.kakaocdn.net/dn/dIjwzH/btrQMxAckUP/wScGEBKqKBaCIifO9BidQK/img.png)

-   Form 생성 및 데이터 정의

![](https://k.kakaocdn.net/dn/bGr3wU/btrQN87Fy2k/1wYfr5P8XBdI5jVqc4oCcK/img.png)

-   **v-on: {event}.prevent**를 활용하여 submit 이벤트 동작을 취소하기

![](https://k.kakaocdn.net/dn/bIx4SD/btrQKD8EQRp/oHnyPv7TYk4dA17yOIVR70/img.png)

-   actions에 여러 개의 데이터를 넘길 때 하나의 object로 만들어서 전달

![](https://k.kakaocdn.net/dn/xXVEm/btrQKiwXBiS/s5t6ZvzfWzSszQIt2TlKqk/img.png)

-   **v-model.trim**을 활용하여 입력 값의 공백을 제거

![](https://k.kakaocdn.net/dn/cdmCZy/btrQNJmKusM/1xiwsvqrvfhCBfV5eebXY0/img.png)

-   데이터가 없는 경우 alert & 데이터가 있는 경우 actions로 전달

![](https://k.kakaocdn.net/dn/cBKvk7/btrQKhLCUV3/Dl8f1KTtK1w2lKbWflUgg1/img.png)

-   actions에서는 넘어온 데이터를 활용하여 article 생성 후 mutations 호출
    -   이 때, id로 article_id 활용

![](https://k.kakaocdn.net/dn/bMvOWH/btrQNHvJnUw/RdLXksS0ooa5GKphDqlL40/img.png)

-   mutations에서는 전달된 article 객체를 사용해 게시글 작성
    -   다음 게시글을 위해 article_id 값 1 증가

![](https://k.kakaocdn.net/dn/d338Tl/btrQK1Bsgaz/BQSRXL4A6KyLsNISDw576k/img.png)

-   CreateView 컴포넌트에 Index 페이지로 이동하는 뒤로가기 링크 추가

![](https://k.kakaocdn.net/dn/mOQFG/btrQKvJAK0c/4IJ8PpJ07BaSxd5Ss0rLjk/img.png)

-   게시글 생성 후 Index 페이지로 이동하도록 네비게이터 작성

![](https://k.kakaocdn.net/dn/DgFPR/btrQN7noMg5/2qjTFzPT8KNkyDCI1mwtPK/img.png)

-   IndexView 컴포넌트에 게시글 작성 페이지로 이동하는 링크 추가

![](https://k.kakaocdn.net/dn/Y5qnA/btrQMslgsth/1j3lIDkL4kCMgtOsfPfmL1/img.png)

---

### **3. Detail**

-   DetailView 컴포넌트 및 라우터 작성
-   id를 동적인자로 전달

![](https://k.kakaocdn.net/dn/bmocMe/btrQOnKhmX6/zxAj4zpeLkRQG46nvKHPk1/img.png)

-   article 정의 및 state에서 articles 가져오기

![](https://k.kakaocdn.net/dn/kwOMc/btrQOaj7ieo/8wKeCmnHuKKCVgFSbbowVK/img.png)

-   articles에서 동적인자를 통해 받은 id에 해당하는 article 가져오기
-   이 때, 동적 인자를 통해 받은 id는 str이므로 형변환을 해서 비교

![](https://k.kakaocdn.net/dn/cvnRbt/btrQOjA5JV1/kDD82WKqlh7Srqk5vKc0z1/img.png)

![](https://k.kakaocdn.net/dn/cmZKFn/btrQNH3xDKN/G5Z7HNeWvOMKEicEy54ni1/img.png)

-   created lifecycle hook을 통해 인스턴스가 생성되었을 때 article을 가져오는 함수 호출

![](https://k.kakaocdn.net/dn/cQ3cCQ/btrQOaxD0nM/6FIqK3XX3Wbq5TQEVD1lEk/img.png)

> **만약 서버에서 데이터를 가져왔다면?**

-   우리는 현재 state를 통해 데이터를 동기적으로 가져오지만, 실제로는 서버로부터 가져옴
    -   데이터를 가져오는데 시간이 걸림
-   created를 주석처리하고 데이터가 서버로부터 오는데 시간이 걸림을 가정

![](https://k.kakaocdn.net/dn/lpugw/btrQOSbVwhU/Qjncuk03xmFWzXSmKMHkS1/img.png)

-   그런데 article이 null이기 때문에 id 등의 속성을 가져올 수 없음

![](https://k.kakaocdn.net/dn/lgJqr/btrQK7uVQgL/xCkFkqZP1F9fjBHokXTttk/img.png)

-   optional chaining(**?.**)을 통해 article 객체가 있을 때만 출력되도록 수정
-   created 주석을 다시 해제

![](https://k.kakaocdn.net/dn/Pd1yl/btrQJIvQ1ek/zfPc7TfuLtDkPMLzMEP8s0/img.png)

**※ 참고 - Optional Chaining**

-   Optional Chaining(**?.**) 앞의 평가 대상이 undefined나 null이면 에러가 발생하지 않고 undefined를 반환 (ES2020에서 추가된 문법)

![](https://k.kakaocdn.net/dn/zgW1Y/btrQOBVOaxO/ut8WomYxZD1i9CTL52sSck/img.png)

> **Date in JavaScript**

-   JavaScript에서 시간을 나타내는 Date 객체는 1970년 1월 1일 UTC(협정 세계시) 자정과의 시간 차이를 밀리초로 나타내는 정수 값을 담음
    -   **Date.toLocaleString()**을 사용하여 변환
-   로컬시간으로 변환해주는 computed 값 작성 및 출력

![](https://k.kakaocdn.net/dn/bmyzPi/btrQNIVKvkK/GIxSVEE3X7iqqGLYE4pCu1/img.png)

![](https://k.kakaocdn.net/dn/bQxbbN/btrQOON9xsD/im8Esbn5wluRukVk7vZnL0/img.png)

-   DetailView 컴포넌트에 뒤로가기 링크 추가

![](https://k.kakaocdn.net/dn/puCOG/btrQOnpYXry/wpeFjKOU99tbo7KIcA4yQk/img.png)

-   각 게시글을 클릭하면 detail 페이지로 이동하도록 ArticleItem에 이벤트 추가
-   v-on 이벤트 핸들러에도 인자 전달 가능

![](https://k.kakaocdn.net/dn/dhkxun/btrQOAP8oAL/9kXrJPoXUFwdHF0HEEnJtK/img.png)

---

### **4. Delete**

-   DeleteView 컴포넌트에 삭제 버튼을 만들고, mutations를 호출

![](https://k.kakaocdn.net/dn/EDwul/btrQNHbtfw0/I5GexWmnlC4C4mwC88esgK/img.png)

-   mutations에서 id에 해당하는 게시글을 지움

![](https://k.kakaocdn.net/dn/PUBZf/btrQOOtP2pz/1vLFRKtkuKlFpbgJaDkq9k/img.png)

-   삭제 후 index 페이지로 이동하도록 네비게이션 작성

![](https://k.kakaocdn.net/dn/qefL0/btrQOAii53e/V20JOK3I2AoX0rtuRWuNu1/img.png)

---

### **5. 404 Not Found**

-   NotFound404 컴포넌트 및 라우터 작성
-   Detail에 대한 route보다 먼저 등록해줘야 함
    -   또한, /404로 등록하면 404번째 게시글과 혼동할 수 있게 됨

![](https://k.kakaocdn.net/dn/dgaDIK/btrQOnKi3L5/jSVxQfMNrimKSObqIhuZBK/img.png)

-   DetailView 컴포넌트에 id에 해당하는 article이 없으면 404 페이지로 이동

![](https://k.kakaocdn.net/dn/vBhOo/btrQMylwclG/mX4G2Qe6uUOa54LVJpSf20/img.png)

-   요청한 리소스가 존재하지 않는 경우 없는 id가 아닌 전혀 다른 요청에도 대비하여 404 page로 **redirect** 시키기
    -   **$router.push**와 마찬가지로 name을 이용하여 이동할 수 있음

![](https://k.kakaocdn.net/dn/dpPvow/btrQKbYS72K/4ARKT8WyAm3opMgj6621Z0/img.png)
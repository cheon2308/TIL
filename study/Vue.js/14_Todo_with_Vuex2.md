

#### **목차**

1.  상태별 todo 개수 계산
2.  Local Storage

---

### **1. 상태별 todo 개수 계산**

> **전체 todo 개수**

-   **allTodosCount** getters 작성
-   state에 있는 todos 배열의 길이 계산

![](https://k.kakaocdn.net/dn/2kJuG/btrQCUWc2if/GD9Qc9FmXpkhzKv4okAJ6K/img.png)

-   getters에 계산된 값을 각 컴포넌트의 computed에서 사용하기

![](https://k.kakaocdn.net/dn/A3vfk/btrQyvXdyyh/OsBWqUMz2bsPXFTQxEXB20/img.png)

> **완료된 todo 개수**

-   **completedTodosCount** getters 작성
-   isCompleted가 true인 todo들만 필터링한 배열을 만들고 길이 계싼
-   **filter**를 활용하여 완료 여부에 따른 새로운 객체 목록을 작성 후 길이 반환

![](https://k.kakaocdn.net/dn/tNa0W/btrQEacLe0M/0byh53VeSjlyN8RpMflY01/img.png)

-   getters에 계산된 값을 각 컴포넌트의 computed에서 사용하기 

![](https://k.kakaocdn.net/dn/dG5qAJ/btrQyWmOXG7/yskFBXOxmvXkGTwFohvw11/img.png)

> **미완료된 todo 개수**

-   미완료된 todo 개수 === 전체 개수 - 완료된 개수
-   getters가 두번째 인자로 getters를 받는 것을 활용하기
-   **unCompletedTodosCount** getters 작성

![](https://k.kakaocdn.net/dn/dqgNge/btrQywhufxU/lEdfBBKOodN5RmDI9Aks2k/img.png)

-   getters에 계산된 값을 각 컴포넌트의 computed에서 사용하기

![](https://k.kakaocdn.net/dn/em7ljO/btrQyvQqBH0/E0Yb1SBqITvLhVnSrn0lDK/img.png)

---

### **2. Local Storage**

> **개요**

-   브라우저의 **Local Storage**에 todo 데이터를 저장하여 브라우저를 종료하고 다시 실행해도 데이터가 보존될 수 있도록 하기

> **Window.localStorage**

-   브라우저에서 제공하는 저장공간 중 하나인 Local Storage에 관련된 속성
-   만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨
-   데이터가 문자열 형태로 저장됨
-   관련 메서드
    -   **setItem(key, value) -** key, value 형태로 데이터 저장
    -   **getItem(key) -** key에 해당하는 데이터 조회
-   https://developer.mozilla.org/ko/docs/Web/API/Window/localStorage

> **실습**

-   todos 배열을 Local Storage에 저장하기
-   데이터가 문자열 형태로 저장되어야 하기 때문에 **JSON.stringify**를 사용해 문자열로 변환해주는 과정 필요
-   state를 변경하는 작업이 아니기 때문에 mutations가 아닌 actions에 작성

![](https://k.kakaocdn.net/dn/plbGc/btrQBMjMSnW/ewTKLqNaK4KvggPjXwkZN1/img.png)

-   todo 생성, 삭제, 수정시에 모두 **saveTodosToLocalStorage** action 메서드가 실행 되도록 함

![](https://k.kakaocdn.net/dn/bHrLIa/btrQDk1gWwd/NiyDVVcXN80hFXaL9OcgMK/img.png)

-   개발자도구 => Application => Storage => Local Storage에서 todos가 저장된 것을 확인
-   하지만 아직 Local Storage에 있는 todo 목록을 불러오는 것이 아니기 때문에 페이지 새로고침 이후 목록이 모두 사라짐
-   불러오기 버튼을 누르면 Local Storage에 저장된 데이터를 가져오도록 할 것
    1.  불러오기 버튼 작성
    2.  **loadTodos** 메서드 작성
    3.  **loadTodos** action 메서드 작성
    4.  **LOAD_TODOS** mutations 메서드 작성

![](https://k.kakaocdn.net/dn/WKQ4w/btrQxcja9bm/qSH0kGH1edqGsPOOSfPa21/img.png)

1

![](https://k.kakaocdn.net/dn/6ZYOi/btrQBK7mEKi/1EKubLuIDDmVHhzSokPjiK/img.png)

2

![](https://k.kakaocdn.net/dn/YOGcr/btrQAxNUsvF/yrGb4XZS3xjvHWELtCQaD0/img.png)

3

![](https://k.kakaocdn.net/dn/7Z8fJ/btrQyWf3Gk5/KmofT0zw6CjQREwmq8hwZk/img.png)

4

-   문자열 데이터를 다시 object 타입으로 변환 (**JSON.parse**)하여 저장

> **vuex-persistedstate**

-   Vuex state를 자동으로 브라우저의 Local Storage에 저장해주는 라이브러리 중 하나
-   페이지가 새로고침 되어도 Vuex state를 유지시킴
-   Local Storage에 저장된 data를 자동으로 state로 불러옴

-   설치

```
npm i vuex-persistedstate
```

-   적용

![](https://k.kakaocdn.net/dn/bIwCUJ/btrQDdH0duB/guvAewVtc63JtaMBIynRs0/img.png)

-   이전에 작성한 localStorage 관련 코드를 모두 주석 처리
    -   **App.vue**
        -   불러오기 버튼
        -   loadTodos 메서드
    -   **index.js**
        -   LOAE_TODOS mutation 메서드
        -   saveTodosToLocalStarage action 메서드
        -   loadTodos action 메서드
        -   context.dispatch('saveTodosToLocalStarage') 코드 3줄

> **마무리**

-   **그냥 mutations으로만 state를 변경하면 안될까?**  
    -   "가능하다"
    -   단 저장소의 각 컨셉(state, getters, mutations, actions)은 각자의 역할이 존재하도록 설계 되어있음
    -   물론 우리가 작성한 todo app처럼 actions의 로직이 특별한 작업 없이 단순히 mutations만을 호출하는 경우도 있으나 이 경우는 Vuex 도입의 적절성을 판단해 볼 필요가 있음
-   **Vuex, 언제 사용해야 할까?**
    -   Vuex는 공유된 상태 관리를 처리하는 데 유용하지만, 개념에 대한 이해와 시작하는 비용이 큼
    -   애플리케이션이 단순하다면 Vuex가 없는 것이 더 효율적일 수 있음
    -   그러나 중대형 규모의 SPA를 구축하는 경우 Vuex는 자연스럽게 선택할 수 있는 단계가 오게 됨
    -   결과적으로 역할에 적절한 상황에서 활용 했을 때 Vuex 라이브러리 효용을 극대화 할 수 있음
    -   즉, 필요한 순간이 왔을 때 사용하는 것을 권장
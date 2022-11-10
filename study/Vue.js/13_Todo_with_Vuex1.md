
![](https://k.kakaocdn.net/dn/bmItF2/btrQw19zJIi/9d7Fi5lmVpbc4FeSMFqOEK/img.png)

위와 같은 컴포넌트 구성을 이루는 Todo 프로젝트를 만들어보자.

#### **목차**

1.  사전준비
2.  Read Todo
3.  Create Todo
4.  Delete Todo
5.  Update Todo

---

### **1. 사전준비**

> **Init Project**

1.  프로젝트 생성 및 vuex 플러그인 추가
2.  HelloWorld 컴포넌트 및 관련 코드 삭제
    -   **App.vue**의 CSS 코드는 남김

![](https://k.kakaocdn.net/dn/dfBz7J/btrQvNRjVnh/1mciXOXpJIY0h60aTkNpfK/img.png)

> **컴포넌트 작성**

-   TodoListItem.vue

![](https://k.kakaocdn.net/dn/bGzo59/btrQuI3KZJ5/mDTJxcB3tSavI1j4PetjZk/img.png)

-   TodoList.vue

![](https://k.kakaocdn.net/dn/lWshR/btrQC8T4vtz/5zBkbyAq30Mxy7gGVgheSK/img.png)

-   TodoForm.vue

![](https://k.kakaocdn.net/dn/sD975/btrQyW1dK5r/xbTHKf6Fu9iZTHPJmQuwhk/img.png)

-   App.vue

![](https://k.kakaocdn.net/dn/dDnaI1/btrQywO6kAU/deiKyO7V4uYRDheOeXuXdk/img.png)

---

### **2. Read Todo**

> **State 세팅**

-   출력을 위한 기본 todo 작성 
-   Vue 개발자 도구에서 state 데이터 확인

![](https://k.kakaocdn.net/dn/Km3JP/btrQyV2ji3P/5a54Ow9lR7wR2alc3yGQQk/img.png)

![](https://k.kakaocdn.net/dn/ur0l6/btrQxbqNaQ6/7W9kEtKTmzVsB5DrEyz321/img.png)

> **state 데이터 가져오기**

-   컴포넌트에서 Vuex Store의 state에 접근($store.state)
-   computed로 계산된 todo 목록을 가져올 수 있도록 설정

**※ v-for의 key는 배열의 각 요소 간의 유일한 식별자 값을 사용해야 하지만 vuex 흐름에 집중하기 위해 index를 key로 사용하도록 함**

![](https://k.kakaocdn.net/dn/cghgui/btrQDk7SXU1/uMHawlWBdk54kSOOpqKlc1/img.png)

> **Pass Props**

-   TodoList.vue -> Todo.vue

![](https://k.kakaocdn.net/dn/K9xJB/btrQw3flRSB/5nXIVXmdFtVGKmk65FMLvk/img.png)

-   TodoList.vue -> Todo.vue
-   todo 데이터 내려받기

![](https://k.kakaocdn.net/dn/HxSpL/btrQDv2x2JH/D3AeZUdaT625dRTsw18XkK/img.png)

---

### **3. Create Todo**

> **TodoForm**

-   todoTitle을 입력 받을 input 태그 생성
-   todoTitle을 저장하기 위해 data를 정의하고 input과 v-model을 이용해 양방향 바인딩
-   enter 이벤트를 사용해 createTodo 메서드 출력 확인

![](https://k.kakaocdn.net/dn/lzSaV/btrQz6W2PRt/AT1DPM6aDPXRs1r6FqSIy0/img.png)

> **Actions**

-   createTodo 메서드에서 actions을 호출(**dispatch**)
-   todoTitle까지 함께 전달하기

![](https://k.kakaocdn.net/dn/8NiIt/btrQw2gvTxI/IoHT9aeJiWbg3VVRKpXF3K/img.png)

**※ actions에는 보통 비동기 관련 작업이 진행 되지만 현재 별도의 비동기 관련 작업이 불필요하기 때문에 입력 받은 todo 제목(todoTitle)을 todo 객체(todoItem)로 만드는 과정을 Actions에서 작성할 예정**

-   createTodo에서 보낸 데이터를 수신 후 todoItem object를 생성

![](https://k.kakaocdn.net/dn/HR4m1/btrQAwnMQbP/62DFKRpOvZNYgVnNRZwQj1/img.png)

> **Mutations**

-   CREATE_TODO mutations메서드에 todoItem를 전달하며 호출(**commit**)

![](https://k.kakaocdn.net/dn/cCQVZl/btrQCiCMXZJ/7UPRgXFyFxzPQYkaDAzgFk/img.png)

-   mutations에서 state의 todos에 접근해 배열에 요소를 추가

![](https://k.kakaocdn.net/dn/qiTMl/btrQuNKQ6Ee/ksIAnpn1s4tcjJJUvfQhS0/img.png)

-   Todos의 기존 dummy 데이터를 삭제 후 빈 배열로 수정

![](https://k.kakaocdn.net/dn/NEsZp/btrQC7ntnMj/3I6aF8jDCOHkedj2EjOVk0/img.png)

> **공백 문자가 입력되지 않도록 처리하기**

-   **v-modle.trim** **&** **if (this.todoTitle)**
    -   좌우 공백 삭제
    -   빈 문자열이 아닐 경우만 작성

![](https://k.kakaocdn.net/dn/b96tOX/btrQDcIZQVx/KyCDWPjixjyahq7PpcCOp0/img.png)

![](https://k.kakaocdn.net/dn/brtKKH/btrQAxfYsJR/7JWYi4GaW2UGqDXgqFZOHK/img.png)

> **중간 정리**

-   Vue 컴포넌트의 method에서 **dispatch()**를 사용해 actions 메서드를 호출
-   Actions에 정의된 함수는 **commit()** 을 사용해 mutations를 호출
-   Mutations에 정의된 함수가 최종적으로 state를 변경

---

### **4. Delete Todo**

> **TodoListItem**

-   TodoListItem 컴포넌트에 삭제 버튼 및 deleteTodo 메서드 작성

![](https://k.kakaocdn.net/dn/u8zta/btrQCUBQw6c/VRTQDbRkw64bLZh37GZLJK/img.png)

> **Actions**

-   deleteTodo 메서드에서 deleteTodo actions 메서드 호출 (**dispatch**)
-   삭제되는 todo를 함께 전달

![](https://k.kakaocdn.net/dn/GLEwX/btrQxbkd2rF/sXuki0WbGoHCkzipgfF0yK/img.png)

-   deleteTodo actions 메서드에서 DELETE_TODO mutations 메서드 호출 (**commit**)

![](https://k.kakaocdn.net/dn/beoaxs/btrQC804N7g/xfxUO9Sq3oM0UXwlDWe5Bk/img.png)

> **Mutations**

-   DELETE_TODO 메서드 작성

![](https://k.kakaocdn.net/dn/pBKLe/btrQDktoDyw/usXPJ8EjpBIPj78KKYKdok/img.png)

-   전달된 todoItem에 해당하는 todo 삭제
-   작성 후 삭제 테스트

![](https://k.kakaocdn.net/dn/KcAUI/btrQywu011u/m9TGgHenXWiYs3pAcHNGK0/img.png)

---

### **5. Update Todo**

> **TodoListItem**

-   todo를 클릭하면 완료 표시의 의미로 취소선 스타일을 적용하는 기능 구현
    -   즉 todo의 isCompleted 값 토글하기
-   TodoListItem 컴포넌트에 클릭 이벤트를 추가 후 관련 actions 메서드 호출

![](https://k.kakaocdn.net/dn/dR8ieU/btrQvOwauQ0/N0gcyNAR83J0Y2L6i389Nk/img.png)

> **Actions**

-   **updateTodoStatus 메서드 작성**
-   관련 mutations 메서드 호출

![](https://k.kakaocdn.net/dn/BI561/btrQD95ZkM5/BK9dT42dk0poNvFhtg7XNk/img.png)

> **Mutations**

-   **UPDATE_TODO_STATUS** 메서드 작성

![](https://k.kakaocdn.net/dn/oj4A7/btrQyXeUT0d/DviyKL4bMKUFgccVvaKJEK/img.png)

-   map 메서드를 활용해 선택된 todo의 isCompleted를 반대로 변경 후 기존 배열 업데이트

![](https://k.kakaocdn.net/dn/CMts5/btrQDvO6tsM/koyR9ITh7PVpkm32bk1yBK/img.png)

> **취소선 스타일링**

-   CSS 작성

![](https://k.kakaocdn.net/dn/cBr0VA/btrQDwUOf4Y/ePHXpqmeBc4kO3IP0KgG2K/img.png)

-   v-bind를 활용해 isCompleted 값에 따라 css 클래스가 토글 방식으로 적용되도록 작성하기

![](https://k.kakaocdn.net/dn/xRkbw/btrQvZdiLmx/nOf5osGniim5LszcSHdgg1/img.png)
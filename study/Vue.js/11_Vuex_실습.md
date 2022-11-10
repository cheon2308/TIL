
**Object method shorthand**

-   이제부터는 객체 메서드 축양형을 사용할 것 !

![](https://k.kakaocdn.net/dn/l52ZU/btrQBMbZodP/TLpaOsKLmEdLkT0V4kgw9K/img.png)

#### **목차**

1.  state
2.  getters
3.  mutations
4.  actions

---

### **1. state**

> **state**

-   중앙에서 관리하는 모든 상태 정보
-   **$store.state**로 접근 가능
-   store의 state에 message 데이터 정의

![](https://k.kakaocdn.net/dn/cUdriP/btrQsENwZAb/KeArBDzYaG7Q8dQOevOBN0/img.png)

-   component에서 state 사용

![](https://k.kakaocdn.net/dn/cuNS08/btrQvPgwDf8/RceGxd0fNNNbDL8GaJlZU1/img.png)

-   **$store.state**로 바로 접근하기 보다 **computed**에 정의 후 접근하는 것을 권장

![](https://k.kakaocdn.net/dn/lB5UM/btrQChJIzMs/n6vED6532OfY1W2uCrxU3k/img.png)

-   Vue 개발자 도구에서의 Vuex
-   관리 화면을 Vuex로 변경 후 관리 되고 있는 state 확인 가능

---

### **2. actions**

-   state를 변경할 수 있는 **mutations 호출**
-   component에서 **dispatch()**에 의해 호출됨
-   **dispatch(A, B)**
    -   **A :** 호출하고자 하는 actions 함수
    -   **B :** 넘겨주는 데이터(payload)
-   actions에 정의된 changeMessage 함수에 데이터 전달하기
-   component에서 actions는 **dispatch()**에 의해 호출 됨

![](https://k.kakaocdn.net/dn/dXYnDI/btrQsC3hSbo/CjI001McyncwlMbPhFHtbK/img.png)

-   actions의 첫 번째 인자는 **context**
    -   **context**는 store의 전반적인 속성을 모두 가지고 있으므로 context.state와 context.getters를 통해 mutations를 호출하는 것이 모두 가능
    -   **dispatch()**를 사용해 다른 actions도 호출할 수 있음
    -   **단, actions에서 state를 직접 조작하는 것은 삼가야 함**
-   actions의 두 번째 인자는 **payload**
    -   넘겨준 데이터를 받아서 사용

![](https://k.kakaocdn.net/dn/bLZXvR/btrQr6wGmib/ROhjlCGXKlUWK8f2XuFjk0/img.png)

---

### **3. mutations**

-   "actions에서 **commit()**을 통해 mutations 호출하기"
-   mutations는 state를 변경하는 유일한 방법
-   component 또는 actions에서 **commit()**에 의해 호출 됨

-   **commit(A,B)**  
    -   **A :** 호출하고자 하는 mutations 함수
    -   **B :** payload

![](https://k.kakaocdn.net/dn/FFDzp/btrQz53Wkel/KSTklyzR4sC3g5GSmill1k/img.png)

-   mutations는 state를 변경하는 유일한 방법
-   첫 번째 인자 **state**
-   두 번째 인자 **payload**

![](https://k.kakaocdn.net/dn/lBotQ/btrQrGd1dLp/OhVAQvm8mkv2l20M5Ded2K/img.png)

---

### **4. getters**

"getters 사용해 보기"

-   **getters는 state를 활용한 새로운 변수**
-   getters 함수의 
    -   첫 번째 인자는 **state**
    -   두 번째 인자는 **getters**

![](https://k.kakaocdn.net/dn/b77UQs/btrQr7h1By2/rfYMnmYoQczhvnAkttyG8K/img.png)

-   getters의 다른 함수 사용

![](https://k.kakaocdn.net/dn/HBWpH/btrQr1IZyaV/wj56thk2rA2mUCUgp926f0/img.png)

"getters 출력하기"

-   getters 역시 state와 마찬가지로 computed에 정의해서 사용하는 것을 권장

![](https://k.kakaocdn.net/dn/blBqrw/btrQrGyiVHh/uJ5iDEksGIHOGHcUVHOKL1/img.png)

![](https://k.kakaocdn.net/dn/r6BdO/btrQz5XbrjN/K22f5tVl9Hf5pjC71ZSgK1/img.png)
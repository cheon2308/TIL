
#### **목차**

1.  State Management
2.  Vuex 

---

### **1. State Management**

![](https://k.kakaocdn.net/dn/UGFg8/btrQsD17CRO/bZqCw908QvcKNdJZbA8kjk/img.png)

-   상태(State)란 ?
    -   **현재에 대한 정보(data)**
-   나의 상태가 어때? 라는 질문에 할 수 있는 대답들
    -   배가 고파
    -   졸려 등등..

따라서 Web Application에서의 상태는 **현재 App이 가지고 있는 Data로 표현**할 수 있음!

-   우리는 여러 개의 **component를 조합해서 하나의 App**을 만들고 있음
-   각 component는 **독립적**이기 때문에 **각각의 상태(data)**를 가짐
-   하지만 결국 이러한 component들이 모여서 하나의 App을 구성할 예정
-   즉, **여러 개의 component가 같은 상태(data)를 유지할 필요**가 있음
    -   상태 관리(State Management) 필요!

> **Pass Props & Emit Event**

-   지금까지는 props와 event를 이용해서 상태 관리를 하고 있음
-   각 컴포넌트는 독립적으로 데이터를 관리
-   **같은 데이터를 공유**하고 있으므로, **각 컴포넌트가 동일한 상태를 유지**하고 있음
-   데이터의 흐름을 직관적으로 파악 가능

![](https://k.kakaocdn.net/dn/bTd8hD/btrQsFlfz5S/D5iCDrgv53IurLeARxQsl0/img.png)

-   그러나 component의 중첩이 깊어지면 데이터 전달이 쉽지 않음
    -   무조건 한 단계씩 이동해야 하므로!
-   공통의 상태를 유지해야 하는 component가 많아지면 데이터 전달 구조가 복잡해짐

> **Centralized Store**

-   **중앙 저장소(store)에 데이터를 모아서 상태 관리**
-   각 component는 중앙 저장소의 데이터를 사용
-   component의 **계층에 상관없이 중앙 저장소에 접근**해서 데이터를 얻거나 변경할 수 있음
-   **중앙 저장소의 데이터가 변경**되면 각각의 component는 **해당 데이터의 변화에 반응하여 새로 변경된 데이터를 반영**함
-   규모가 크거나 컴포넌트 중첩이 깊은 프로젝트의 관리가 매우 편리

![](https://k.kakaocdn.net/dn/bYfQm8/btrQuIojWfW/6UGT7EWHlYGS6JSOVXSBbK/img.png)

---

### **2. Vuex**

-   "state management pattern + Library" for vue.js (상태 관리 패턴 + 라이브러리)
-   **중앙 저장소를 통해 상태 관리**를 할 수 있도록 하는 라이브러리
-   데이터가 예측 가능한 방식으로만 변경 될 수 있도록하는 **규칙을 설정하며, Vue의 반응성을 효율적으로 사용하는 상태 관리 기능**을 제공
-   Vue의 공식 도구로써 다양한 기능을 제공

> **Project with vuex**

![](https://k.kakaocdn.net/dn/LWNiT/btrQyvoexdV/sIp1QUldsYefkHZAuoy70K/img.png)

-   **src / store / index.js** 가 생성됨
-   vuex의 핵심 컨셉 4가지
    1.  **state**
    2.  **getters**
    3.  **mutations**
    4.  **actions**

![](https://k.kakaocdn.net/dn/dMwspe/btrQr2nAIZf/UhRRB7pCBPucAGpVxkb071/img.png)

-   Vue와 Vuex 인스턴스 비교

![](https://k.kakaocdn.net/dn/cBZuy1/btrQywm9KB2/iL7Lv7Kju4GkEu2ZRYFKF0/img.png)

> **1. State**

-   vue 인스턴스의 **data**에 해당
-   **중앙에서 관리하는 모든 상태 정보**
-   개별 component는 state에서 데이터를 가져와서 사용
    -   개별 component가 관리하던 data를 중앙 저장소(Vuex Store의 state)에서 관리하게 됨
-   state의 데이터가 변화하면 해당 데이터를 사용(공유)하는 component도 자동으로 다시 렌더링
-   **$store.state**로 state 데이터에 접근

> **2. Mutations**

-   **실제로 state를 변경하는 유일한 방법**
-   vue 인스턴스의 methods에 해당하지만 Mutations에서 호출되는 핸들러(handler) 함수는 반드시 **동기적**이어야 함
    -   비동기 로직으로 mutations를 사용해서 state를 변경하는 경우, state의 변화의 시기를 특정할 수 없기 때문
-   첫 번째 인자로 **state**를 받으며, component혹은 Actions에서 **commit()** 메서드로 호출됨

**※ mutation, action에서 호출되는 함수를 handler 함수라고 함**  

> **3. Actions**

-   mutations와 비슷하지만 **비동기** 작업을 포함할 수 있다는 차이가 있음
-   state를 직접 변경하지 않고 **commit()** 메서드로 **mutations를 호출**해서 state를 변경함
-   **context 객체**를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근할 수 있음 (== **즉 state를 직접 변경할 수 있지만 하지 않아야 함**)
-   component에서 **dispatch()** 메서드에 의해 호출됨

> **Mutations & Actions**

-   vue component의 methods 역할이 vuex에서는 아래와 같이 분화됨
-   **Mutations**
    -   state를 변경
-   **Actions**
    -   state 변경을 제외한 나머지 로직

![](https://k.kakaocdn.net/dn/BJmtU/btrQr64vcVC/WVV1CgTKMzSggYAdSisSy0/img.png)

> **4. Getters**

-   vue 인스턴스의 **computed**에 해당
-   **state를 활용하여 계산된 값을 얻고자 할 때 사용**
-   state의 원본 데이터를 건들지 않고 계산된 값을 얻을 수 있음
-   computed와 마찬가지로 getters의 결과는 **캐시(cache)** 되며, 종속된 값이 변경된 경우에만 재계산됨
-   getters에서 계산된 값은 state에 영향을 미치지 않음
-   첫번째 인자로 **state,** 두번째 인자로 **getter**를 받음

**※ 모든 데이터를 Vuex에서 관리해야 할까?**

-   Vuex를 사용한다고 해서 모든 데이터를 state에 넣어야 하는 것은 아님
-   Vuex에서도 여전히 pass props, emit event를 사용하여 상태를 관리할 수 잇음
-   개발 환경에 따라 적절하게 사용하는 것이 필요함

> **정리**

-   **state**  
    -   중앙에서 관리하는 **모든 상태 정보**
-   **mutations**
    -   **state를 변경**하기 위한 methods
-   **actions**
    -   **비동기 작업이 포함될 수 있는 (외부 API 와의 소통** **등)** methods
    -   state를 변경하는 것 외의 모든 로직 진행
-   **getters**
    -   state를 활용해 **계산한 새로운 변수 값**
-   component에서 데이터를 조작하기 위한 데이터의 흐름
    -   component => (actions) => mutations => state
-   component에서 데이터를 사용하기 위한 데이터의 흐름
    -   state => (getters) => component
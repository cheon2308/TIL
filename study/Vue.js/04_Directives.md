
#### **목차**

1.  기본 구성
2.  v-접두사
3.  Vue computed

---

### **1. 기본 구성**

-   v-접두사가 있는 특수 속성에는 값을 할당 할 수 있음
    -   값에는 JS 표현식을 작성 할 수 있음
-   directive의 역할은 **표현식의 값**이 **변경**될 때 **반응적**으로 DOM에 적용하는 것

![](https://k.kakaocdn.net/dn/OLjF7/btrP0HcPhYj/kCi8yuKIcRcuCwESaxwgv0/img.png)

-   **` : `** 을 통해 **전달인자**를 받을 수 있음
-   **` . `** 으로 표시되는 **특수 접미사 -** directive를 특별한 방법으로 바인딩 해야 함

> **새 Vue instance 생성**

-   각각의 instance들은 연결된 DOM element에만 영향을 미침
-   연결되지 않은 DOM이 Vue의 영향을 받지 않았던 것과 동일한 상황

![](https://k.kakaocdn.net/dn/nKoj0/btrP34Ex7KR/2SEWklFgshtCAdl4tS6wE1/img.png)

---

### **2. v-접두사**

> **v-text**

-   Template Interpolation과 함께 가장 기본적인 바인딩 방법
-   **{{ }}**와 동일한 역할
    -   ~~단 정확히 동일한 역할인 것은 아님~~

![](https://k.kakaocdn.net/dn/T1WsS/btrQiibfe0q/X6OLZxtKWg5kOC5w2qQDZ1/img.png)

> **v-html**

-   RAW HTML을 표현할 수 있는 방법
-   단, 사용자가 입력하거나 제공하는 컨텐츠에는 **절대 사용 금지**
    -   XSS 공격 참고

![](https://k.kakaocdn.net/dn/s7M8q/btrQfd29FxL/noqC05wC54fEkUOg5AMkI0/img.png)

> **v-show**

-   표현식에 작성된 값에 따라 **element**를 보여 줄 것인지 결정
    -   boolean 값이 변경 될 때 마다 반응
-   대상 element의 display 속성을 기본 속성과 none으로 toggle
-   요소 자체는 항상 DOM에 렌더링 됨

![](https://k.kakaocdn.net/dn/MMHRW/btrQeOoYnJ8/2QrptD4zKK8pwXdKr4gX01/img.png)

-   바인딩 된 isActive의 값이 false이므로 첫 방문 시 p tag는 보이지 않음
    -   vue dev tools에서 isActive 변경 시 화면에 출력
    -   값을 false로 변경 시 다시 사라짐
-   화면에서만 사라졌을 뿐, DOM에는 존재한다.
    -   display 속성이 변경되었을 뿐

![](https://k.kakaocdn.net/dn/N5w6D/btrQgdO3FAs/Blu58KanTwTzNbyt3rMEDk/img.png)

> **v-if**

-   v-show와 사용 방법은 동일
-   isActive의 값이 변경 될 때 반응
-   단, 값이 false인 경우 **DOM에서 사라짐**

-   **v-if v-esle-if v-else** 형태로 사용

![](https://k.kakaocdn.net/dn/dixQMG/btrQeCWA0ke/ZVNBtV8xXFuMOtXTpuKaX1/img.png)

**※ v-show VS v-if**

-   **v-show** (Expensive initial load, cheap toggle)
    -   표현식 결과와 관계 없이 렌더링 되므로 초기 렌더링에 필요한 비용은 v-if 보다 높을 수 있음
    -   display 속성 변경으로 표현 여부를 판단하므로 **렌더링 후 toggle 비용은 적음**
-   **v-if (**Cheap initial load, expensive toggle)
    -   표현식 결과가 false인 경우 렌더링조차 되지 않으므로 초기 렌더링 비용은 v-show 보다 낮을 수 있음
    -   단, 표현식 값이 자주 변경되는 경우 **잦은 재 렌더링으로 비용이 증가할 수 있음**

> **v-for**

-   **for .. in ..** 형식으로 작성
-   반복한 데이터 타입에 모두 사용 가능
-   index를 함께 출력하고자 한다면 **(char, index)** 형태로 사용 가능

![](https://k.kakaocdn.net/dn/luQuF/btrQeUpanYV/M9KXGyXXM0AUuLY2pewyok/img.png)

-   배열 역시 문자열과 동일하게 사용 가능
-   각 요소가 객체라면 **dot notation**으로 접근 할 수 있음

![](https://k.kakaocdn.net/dn/c8gXWA/btrQgdnZKKM/mcGGzf6pFXsEVHxstjgkKk/img.png)

**※ 참고 - 특수 속성 key**

-   **"v-for 사용 시 반드시 key 속성을 각 요소에 작성"**
-   주로 **v-for directive** 작성 시 사용
-   vue 화면 구성 시 이전과 달라진 점을 확인하는 용도로 활용
    -   따라서 key가 중복되어서는 안됨
-   각 요소가 고유한 값을 가지고 있다면 생략 할 수 있음

![](https://k.kakaocdn.net/dn/pG09N/btrQgcP9x7h/NijfxCQ3e4YK2KswoP6hP0/img.png)

-   객체 순회 시 value가 할당되어 출력
-   2번째 변수 할당 시 key 출력 가능

![](https://k.kakaocdn.net/dn/JP2Ku/btrQgdnZQhq/fDNdBPZt0idkJzhNk6dBMk/img.png)

> **v-on**

-   **` : `** 을 통해 전달받은 인자를 확인
-   값으로 JS 표현식 작성
-   addEventListener의 첫 번째 인자와 동일한 값들로 구성
-   대기하고 있던 이벤트가 발생하면 할당된 표현식 실행

![](https://k.kakaocdn.net/dn/O7uSE/btrQgMDG9b9/Mwflcea8kvjnCSL48nlE00/img.png)

-   method를 통한 **data 조작**도 가능
-   method에 인자를 넘기는 방법은 일반 함수를 호출할 때와 동일한 방식
-   **` : `** 을 통해 전달된 인자에 따라 특별한 modifiers (수식어)가 있을 수 있음
    -   ex) **v-on : keyup.enter** 등
    -   vue2 가이드 > api > v-on 파트 참고
-   **` @ `** shortcut 제공
    -   ex) **@keyup.click**

> **v-bind**

-   HTML 기본 속성에 Vue data를 연결
-   class의 경우 다양한 형태로 연결 가능
    -   **조건부 바인딩**
        -   **{ 'class Name' : '조건 표현식' }**
        -   삼항 연산자도 가능
    -   **다중 바인딩**
        -   **[ 'JS 표현식', 'JS 표현식', ...]**

![](https://k.kakaocdn.net/dn/CjKM0/btrQeqIUZma/CMSQqf9wWXQABxg33rSav1/img.png)

-   Vue data의 변화에 반응하여 DOM에 반영하므로 상황에 따라 유동적 할당 가능
-   **` : `** shortcut 제공
    -   ex) **: class 등**
    -   v-for에서 사용하였던 :key는 v-bind의 shortcut을 활용한 것

> **v-model**

-   Vue instance와 DOM의 **양방향 바인딩**
-   Vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용

![](https://k.kakaocdn.net/dn/bmkpwy/btrQgMRfJLo/OHEJA3CU4zNZy7VBzJk5r1/img.png)

---

### **3. Vue advanced**

> **computed**

-   Vue instance가 가진 options 중 하나
-   computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출하여 계산
    -   계산 결과가 변하기 전까지 함수를 재호출하는 것이 아닌 **계산된 값을 반환**

![](https://k.kakaocdn.net/dn/skKX3/btrQfJ9ehig/tXQG0YAC1J5slRkWSyfVc1/img.png)

**※ methods VS computed**

-   **methods**  
    -   호출 될 때마다 함수를 실행
    -   같은 결과여도 매번 새롭게 계산
    -   axios와 같은 비동기 요청인 경우 methods 사용
-   **computed**
    -   함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
    -   종속 대상이 변하지 않으면 항상 **저장(캐싱)**된 값을 반환

메서드가 3번 호출될 때 1번 호출된 computed!!

![](https://k.kakaocdn.net/dn/tTtof/btrQiiptXGR/Z5Tsd4Df9DFxmUt4BYEvKk/img.png)

> **watch**

-   특정 데이터의 변화를 감지하는 기능
    1.  watch 객체를 정의
    2.  감시할 대상 data를 지정
    3.  data가 변할 시 실행 할 함수를 정의
-   첫 번째 인자는 변동 전 data
-   두 번째 인자는 변동 후 data
-   디버깅 용도로 많이 사용한다.

![](https://k.kakaocdn.net/dn/dvauBm/btrQgM4MTCY/KUqDGJ1Q4BkYt2NTkSmDA1/img.png)

-   실행 함수를 Vue method로 대체 가능
    1.  감시 대상 data의 이름으로 객체 생성
    2.  실행하고자 하는 method를 handler에 문자열 형태로 할당
-   Array, Object의 내부 요소 변경을 감지를 위해서는 **deep** 속성 추가 필요

> **filters**

-   텍스트 형식화를 적용할 수 있는 필터
-   interpolation 혹은 v-bind를 이용할 때 사용 가능
-   필터는 자바스크립트 표현식 마지막에 **` | ` (파이프)**와 함께 추가되어야 함
-   이어서 사용(**chaining**) 가능
-   **파이프 앞 쪽의 대상이 필터함수의 인자로 들어간다.**

![](https://k.kakaocdn.net/dn/erOUbs/btrQfFeGaB5/CsNg0eKZ4ZXNO0xovXlf51/img.png)
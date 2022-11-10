
#### **목차**

1.  Data in components
2.  Pass Props

---

### **1. Data in components**

-   우리는 정적 웹페이지가 아닌, 동적 웹페이지를 만들고 있음
    -   즉, 웹페이지에서 다뤄야 할 데이터가 등장
    -   User data, 게시글 data, 등등...
-   한 페이지 내에서 같은 데이터를 공유 해야함
    -   하지만 페이지들은 component로 구분이 되어있음
-   MyComponent에 정의된 data를 MyChild에 사용하려면 어떻게 해야 할까?

![](https://k.kakaocdn.net/dn/byudZV/btrQktRRHne/hNIsC54YHogNRMxYdRvQAk/img.png)

-   MyChild에도 똑같은 data를 정의
    -   MyComponent의 data와 MyChild의 데이터가 동일한 data가 맞는가?
    -   MyComponent의 data가 변경된다면 MyChild도 같이 변경이 될까?
    -   아니다. 각 Component는 독립적이므로 서로 다른 data를 갖게 될 것
    -   그렇다면 완전히 **동일한 data**를 **서로 다른 Component**에서 보여주려면 어떻게 해야 할까?
-   필요한 컴포넌트들끼리 데이터를 주고받으면 될까?
    -   데이터의 흐름 파악 힘듦
    -   개발 속도 저하
    -   유지보수 난이도 증가

![](https://k.kakaocdn.net/dn/yooci/btrQf4Te7UK/OOjPkxtXgIpcau1SAB1bzk/img.png)

-   컴포넌트는 부모-자식 관계를 가지고 있으므로, 부모-자식 관계만 데이터를 주고받게 하자!
    -   데이터의 흐름을 파악하기 용이
    -   유지 보수하기 쉬워짐

![](https://k.kakaocdn.net/dn/byOlZx/btrQkF5zuey/huLrfi8kh3wJvsLA1ZWnKk/img.png)

> **pass props & emit event**

-   부모 => 자식으로의 데이터의 흐름
    -   pass **props**의 방식
-   자식 => 부모로의 데이터의 흐름
    -   **emit** event의 방식

![](https://k.kakaocdn.net/dn/cyAiVk/btrQksSZ5rB/MZawWfJGDaYLdY92H2hrW0/img.png)

---

### **2. Pass Props**

-   요소의 **속성(property)을 사용**하여 데이터 전달
-   props는 부모(상위) 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
-   자식(하위) 컴포넌트는 **props 옵션을 사용**하여 **수신하는 props를 명시적으로 선언**해야 함

> **props in HelloWorld**

-   사실, 우리의 Vue app은 이미 props를 사용하고 있었다!
-   Vue CLI를 설치할 때 만들어 주었던 App.vue의 HelloWorld 컴포넌트를 살펴보면 **msg**라는 **property**가 작성되어 있음

![](https://k.kakaocdn.net/dn/648oJ/btrQgLlICTb/M36bKw1oDik242aI7fm8ZK/img.png)

-   HelloWorld.vue에서 **msg**를 사용한 것을 확인할 수 있음
-   App.vue에서 property로 넘긴 msg가 출력되는 것을 확인할 수 있음

![](https://k.kakaocdn.net/dn/defATs/btrQgFy1yum/Fmr7kQClypUxswzmDVWKgk/img.png)

**※ 정리**

-   App.vue의 **<HelloWorld/>** 요소에 **msg="~"** 라는 property를 설정하였고, 하위 컴포넌트인 HelloWorld는 자신에게 부여된 msg property를 template에서 **{{ msg }}**의 형태로 사용한 것

> **props in HelloWorld 실습**

-   msg property의 value를 바꾸면 화면에 보이는 문장이 달라짐

![](https://k.kakaocdn.net/dn/cMEW3I/btrQfE8qITI/hwg2OWpuOA0mhQxMk7ZiWK/img.png)

![](https://k.kakaocdn.net/dn/b9OdKe/btrQh5Yw0uA/LeltIIv59LsiG2shcTLnz0/img.png)

> **Pass Props**

-   이렇게 부모 => 자식으로의 data 전달 방식을 **pass props**라고 함
-   정적인 데이터를 전달하는 경우 static props라고 명시하기도 함
-   요소에 속성을 작성하듯이 사용 가능하여, **prop-data-name="value"** 의 형태로 데이터를 전달
    -   이 때 속성의 키 값은 kebab-case를 사용
-   Prop 명시
-   데이터를 받는 쪽, 즉 **하위 컴포넌트에서도 props에 대해 명시적으로 작성** 해주어야 함
-   전달받은 props를 **type과 함께 명시**
-   컴포넌트를 문서화할 뿐만 아니라, **잘못된 타입이 전달**하는 경우 브라우저의 자바스크립트 콘솔에서 **사용자에게 경고**
-   https://v2.vuejs.org/v2/fuide/components-props.html#Prop-Validation

![](https://k.kakaocdn.net/dn/rWrdj/btrQktRUzrT/ihtrzeLDN5foJtkFu5myoK/img.png)

> **MyComponent to MyChild**

![](https://k.kakaocdn.net/dn/E144b/btrQh4k4guT/oilQZ4Nl2mW5S7za98xGIK/img.png)

![](https://k.kakaocdn.net/dn/diWlxB/btrQjnSb3SR/6VWQHBp62d6eoWCKe4V6E0/img.png)

![](https://k.kakaocdn.net/dn/oTI8X/btrQkBCctCX/vTNLl7u7f2qPa5Z6Xz65x0/img.png)

> **Pass Props convention**

-   부모에서 넘겨주는 props
    -   **kebab-case (HTML 속성명은 대소문자를 구분하지 않기 때문)**
-   자식에서 받는 props
    -   **camelCase**
-   부모 템플릿(html)에서 kebab-case로 넘긴 변수를 자식의 스크립트(vue)에서 자동으로 camelCase로 변환하여 인식함

> **Dynamic props**

-   변수를 props로 전달할 수 있음
-   v-bind directive를 사용해 **데이터를 동적으로 바인딩**
-   **부모 컴포넌트의 데이터가 업데이트** 되면 **자식 컴포넌트로 전달되는 데이터 또한 업데이트** 됨

![](https://k.kakaocdn.net/dn/rF7hB/btrQiiX0TG3/7mnG9FXVtrrKBDBK5W8kck/img.png)

> **컴포넌트의 data 함수**

-   각 vue 인스턴스는 같은 **data 객체를 공유**하므로 **새로운 data 객체를 반환(return)**하여 사용해야 함

![](https://k.kakaocdn.net/dn/UFXxH/btrQgd3U1si/HyZUgIpywwNJOMfJqYc8kk/img.png)

-   https://v2.vuejs.org/v2/guide/components.html#data-Must-Be-a-Function

> **Pass Props**

-   **:dynamic-props="dynamicProps"** 는 앞의 key값(**dynamic-props)**이란 이름으로 뒤의 " " 안에 오는 데이터 (**dynamicProps)**를 전달하겠다는 뜻
-   즉 **:my-props="dynamicProps"**로 데이터를 넘긴다면, 자식 컴포넌트에서 **myProps**로 데이터를 받아야 함

![](https://k.kakaocdn.net/dn/bjZfXE/btrQkv3ggej/63CtCKSgbKfWyUCoSIi3m1/img.png)

-   v-bind로 묶여있는 **"  "** 안의 구문은 javascript의 구문으로 볼 수 있음
    -   따라서 **dynamicProps** 라고 하는 변수에 대한 data를 전달할 수 있는 것
-   그렇다면, 숫자를 props로 전달하기 위해서 다음 두 방법 중 어떤게 맞을까?

![](https://k.kakaocdn.net/dn/L3TeK/btrQj6vU3Bg/f9MKHqTlhRO5VMA5Whg211/img.png)

1.  번 방식의 경우 **static props**로 **string**으로써의 "1"을 전달
2.  번 방식의 경우 **dynamic props**로 **숫자**로써의 1을 전달

> **단방향 데이터 흐름**

-   모든 props는 부모에서 자식으로 즉 **아래로 단방향 바인딩**을 형성
-   부모 속성이 업데이트되면 자식으로 흐르지만 **반대 방향은 아님**
    -   부모 컴포넌트가 업데이트될 때마다 자식 컴포넌트의 모든 prop들이 최신 값으로 새로고침 됨
-   목적
    -   하위 컴포넌트가 **실수로 상위 컴포넌트 상태를 변경**하여 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 **방지**
-   하위 컴포넌트에서 prop를 변경하려고 시도해서는 안되며 그렇게 하면 Vue는 콘솔에서 경고를 출력함
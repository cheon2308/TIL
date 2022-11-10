
#### **목차**

1.  Component
2.  SFC
3.  Vue component
4.  실습

---

### **1. Component**

-   **UI를 독립적이고 재사용 가능한 조각**들로 나눈 것
    -   즉, 기능별로 분화한 코드 조각
-   CS에서는 다시 사용할 수 있는 **범용성**을 위해 개발된 **소프트웨어 구성 요소**를 의미
-   하나의 app을 구성할 때 **중첩된 컴포넌트들의 tree로 구성하는 것이 보편적**임
    -   Web 시간에 배운 HTML 요소들의 중첩을 떠올려 보자!
        -   Body tag를 root node로 하는 tree의 구조이다.
        -   마찬가지로, Vue에서는 src/App.vue를 root node로 하는 tree의 구조를 가짐
-   컴포넌트는 유지보수를 쉽게 만들어 줄 뿐만 아니라 재사용성의 측면에서도 매우 강력한 기능을 제공

![](https://k.kakaocdn.net/dn/cjuZVR/btrQe0RhI9Q/8ck2KwwLGg5HOAgYu6JeVK/img.png)

-   우리가 사용하는 웹 서비스는 여러 개의 컴포넌트로 이루어져 있음
-   하나의 컴포넌트를 만들어두면 반복되는 UI를 쉽게 처리할 수 있음

![](https://k.kakaocdn.net/dn/dq9EjD/btrQkWZ7Q96/iuBXi0julE08Nh1jiijOs0/img.png)

> **Django에서의 예시**

-   우리는 base.html과 index.html을 분리하여 작성하였지만, 하나의 화면으로 볼 수 있다.
    -   즉, 한 화면은 **여러 개의 컴포넌트로 구성**될 수 있음
-   base.html을 변경하면 이를 extends하는 **모든 화면에 영향**을 미침
    -   유지 보수를 쉽게 해줌
-   index.html에서 for문을 통해 여러 게시글들을 하나의 형식에 맞추어서 출력해줌
    -   형식을 재사용하고 있었음
    -   즉, 우리는 너무 자연스럽게 컴포넌트 기반으로 개발을 진행하고 있었다!

![](https://k.kakaocdn.net/dn/ymfCJ/btrQkYjlrWR/4y92AEsIh3gEs7wKwqPmJk/img.png)

> **Component based architecture 특징**

-   관리가 용이
    -   유지/보수 비용 감소
-   재사용성
-   확장 가능
-   캡슐화
-   독립적

---

### **2. SFC**

> **component in Vue**

-   그렇다면 Vue에서 말하는 component란 무엇일까?
    -   이름이 있는 재사용 가능한 Vue instance
-   그렇다면 Vue instance란?
    -   앞서 수업에서 사용한 **new Vue()**로 만든 인스턴스

> **SFC (Single File Component)**

-   하나의 **.vue** 파일이 하나의 **Vue instance**이고, 하나의 **컴포넌트**이다.
    -   즉, Single File Component
-   Vue instance에서는 **HTML, CSS, JavaScript** 코드를 한 번에 관리
    -   이 **Vue instance를 기능 단위로 작성하는 것이 핵심!**
-   컴포넌트 기반 개발의 핵심 기능

> **정리**

-   HTML, CSS, 그리고 JavaScript를 .vue 라는 확장자를 가진 파일 안에서 관리하며 개발
-   이 파일을 Vue instance, 또는 Vue component라고 하며, 기능 단위로 작성
-   Vue CLI가 Vue를 Component based하게 사용하도록 도와줌

---

### **3. Vue component**

> **구조**

-   **템플릿(HTML)**
    -   HTML의 body 부분
    -   눈으로 보여지는 요소 작성
    -   다른 컴포넌트를 HTML 요소처럼 추가 가능

-   **스크립트(JavaScript)**  
    -   JavaScript 코드가 작서오디는 곳
    -   컴포넌트 정보, 데이터, 메서드 등 vue 인스턴스를 구성하는 대부분이 작성 됨

-   **스타일(CSS)**  
    -   CSS가 작성되며 컴포넌트의 스타일을 담당

![](https://k.kakaocdn.net/dn/deh4lp/btrQkXShZty/fkzf7tisotOk3kJ6Qzxya0/img.png)

> **구조 정리**

-   컴포넌트들이 tree 구조를 이루어 하나의 페이지를 만듦
-   root에 해당하는 최상단의 component가 **App.vue**
-   이 App.vue를 index.html과 연결
-   결국 index.html 파일 하나만들 rendering
    -   이게 바로 SPA

![](https://k.kakaocdn.net/dn/cpgA7C/btrQgE7LMtW/izXjDaxLzEXVjdBekabkM1/img.png)

---

### **4. 실습**

> **현재 구조**

-   Vue CLI를 실행하면 이미 HelloWorld.vue라는 컴포넌트가 생성되어 있고 App.vue에 등록되어 사용되고 있음
    -   npm run serve 명령어를 진행 했을 때 나온 화면의 대부분이 HelloWorld.vue

![](https://k.kakaocdn.net/dn/bvqsXp/btrQjkVm6Tz/skQJhQDc5R0mqgDZBuFk1k/img.png)

![](https://k.kakaocdn.net/dn/qtK19/btrQkYX0MZz/8TAuRJhZ9kAQwkeIt9GgJK/img.png)

> **MyComponent.vue**

1.  src/components/ 안에 생성
2.  script에 이름 등록
3.  template에 요소 추가

**※ 주의) templates 안에는 반드시 하나의 요소만 추가 가능**

-   비어 있어도 안됨
-   해당 요소 안에 추가 요소를 작성해야 함

![](https://k.kakaocdn.net/dn/dk0Yvn/btrQkBPBR19/ehQNDR0pPKlaBKIuUd9rc1/img.png)

> **component 등록 3단계**

1.  불러오기
2.  등록하기
3.  보여주기

![](https://k.kakaocdn.net/dn/cievat/btrQf3z3GJb/DhJGzjzRDzlz75WbK9oCA1/img.png)

-   **불러오기**
    -   **import {instance name} from {위치}**
    -   instance name은 instance 생성 시 작성한 name
    -   **@**는 src의 shortcut
    -   **.vue** 생략 가능

![](https://k.kakaocdn.net/dn/dOJKAL/btrQgLlCVWp/aUcJwfVKORg2vMB2KZVrqk/img.png)

-   **등록하기**

![](https://k.kakaocdn.net/dn/zhWot/btrQgL643EJ/q9VLVxA81Y37VvvMuzVR7k/img.png)

-   **보여주기**  
    -   닫는 태그만 있는 요소처럼 사용

![](https://k.kakaocdn.net/dn/brmWJN/btrQf3z37bS/yy8DVAYIJDkneO40ffSlkk/img.png)

-   등록후 현재 컴포넌트 구조

![](https://k.kakaocdn.net/dn/zepNp/btrQkYqcmu3/j4OIryzr4dJmAhH7DuUNR0/img.png)

> **자식 컴포넌트 작성**

-   이제 MyComponent의 자식 컴포넌트를 만들어보자
-   자식 관계를 표현하기 위해 기존 MyComponent에 **간단한 border**를 추가

![](https://k.kakaocdn.net/dn/qCfTJ/btrQfLmc3Ub/dPKfOoZ9S0bfVcnhJaMPl0/img.png)

![](https://k.kakaocdn.net/dn/qfYpn/btrQjlmtvaJ/JuA1XYn5akP8TCJFUNtLRk/img.png)

-   src/components/ 안에 **MyChild.vue** 생성

![](https://k.kakaocdn.net/dn/chGk9D/btrQkYDJtKt/bpoR0KexW7gsurcroXbff1/img.png)

-   MyComponent에 MyChild 등록

![](https://k.kakaocdn.net/dn/b2lLEY/btrQf307dJi/3fJ2p2k2Dlz12Zvy3wThW1/img.png)

![](https://k.kakaocdn.net/dn/cR4zWx/btrQktqMJa7/nDc761cqIFquosTzS1SQi0/img.png)

-   component의 재사용성

![](https://k.kakaocdn.net/dn/cP3K9W/btrQigZ2kSU/LvOJhWP1ZXRwFOoSfK78y1/img.png)

![](https://k.kakaocdn.net/dn/kOFHJ/btrQh5xmsGP/4h1kpKtiKyFvKjD1vrHAJ1/img.png)
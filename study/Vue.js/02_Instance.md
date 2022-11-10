
#### **목차**

1.  MVVM Pattern
2.  Instance
3.  el
4.  data

---

### **1. MVVM Pattern**

-   소프트웨어 아키텍처 패턴의 일종
-   마크업 언어로 구현하는 그래픽 사용자 인터페이스(**view**)의 개발을 Back-end(**model**)로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함

![](https://k.kakaocdn.net/dn/mRsw8/btrP2pJlAwn/LKuBBac5nYGIIXZTK5uv8k/img.png)

![](https://k.kakaocdn.net/dn/zJSUo/btrP35QBQKm/sK4Lh1tms1X69Hxym4n9SK/img.png)

-   **View** = 우리 눈에 보이는 부분 = DOM
-   **Model** = 실제 데이터 = JSON
-   **View Model** (Vue)
    -   View를 위한 Model
    -   View와 연결(binding)되어 Action을 주고 받음
    -   Model이 변경되면 View Modle도 변경되고 바인딩된 View도 변경됨
    -   View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨

> **정리**

-   View는 Model을 몰라요, Model도 View를 몰라요 (독립성 증가, 적은 의존성)
    -   DOM은 Data를 몰라요, Data도 DOM을 몰라요

---

### **2. Vue instance**

1.  Vue CDN 가져오기
2.  **new** 연산자를 사용한 생성자 함수 호출
    -   vue instance 생성
3.  인스턴스 출력 및 확인

![](https://k.kakaocdn.net/dn/bfe3yX/btrP2a6xqn7/8eGYPgHm94wYzBrayqSjE0/img.png)

-   Vue instance === 1개의 객체
-   아주 많은 속성과 메서드를 이미 가지고 있고, 이러한 기능들을 사용하는 것

![](https://k.kakaocdn.net/dn/sj2r1/btrP35QEi0A/FjCIUUYO4yoDuOwfh2n7W1/img.png)

**※ 참고 - 생성자 함수**

-   JS에서 객체를 하나 생성한다고 한다면?
    -   하나의 객체를 선언하여 생성
-   동일한 형태의 객체를 또 만든다면?
    -   또 다른 객체를 선언하여 생성

![](https://k.kakaocdn.net/dn/dJdaAl/btrPXsUqnzD/xRQaaL6KHcIIuazNC6ZRA1/img.png)

-   동일한 구조의 객체를 여러 개 만들고 싶다면?
-   생성자 함수는 특별한 함수를 의미하는 것이 아님
-   **new** 연산자로 사용하는 함수

![](https://k.kakaocdn.net/dn/bJVM2j/btrP3nq1Anf/S2zkACBIauJgGwcNafw8iK/img.png)

-   함수 이름은 **반드시 대문자**로 시작
-   생성자 함수를 사용할 때는 반드시 **new 연산자**를 사용

---

### **3. el (element)**

-   Vue instance와 DOM을 mount(연결)하는 옵션
    -   View와 Model을 연결하는 역할
    -   HTML id 혹은 class와 마운트 가능
-   Vue instance와 **연결되지 않은 DOM 외부는 Vue의 영향을 받지 않음**
    -   Vue 속성 및 메서드 사용 불가

> **작성 및 확인**

1.  새로운 Vue instance 생성
2.  생성자 함수 첫번째 인자로 **Object** 작성
3.  el 옵션에 **#app** 작성 = DOM 연결
4.  인스턴스 출력

![](https://k.kakaocdn.net/dn/wUUwF/btrPU1CPEsY/jFKHB4BdJGQbZ4ZWt8qFT1/img.png)

![](https://k.kakaocdn.net/dn/dmSK4t/btrP3kgNx1J/7ZQVlzotOVWbG6dc0FIf70/img.png)

-   Vue와 연결되지 않은 div 생성
    -   두 div 모두에 {{ message }} 작성
    -   결과 확인
-   message 속성이 정의 되지 않았다는 경고와 {{ message }} 가 그대로 출력되는 차이

![](https://k.kakaocdn.net/dn/AR3Sj/btrP36Wmd7R/rPFESlPN0vdpEMqqL0dKp1/img.png)

![](https://k.kakaocdn.net/dn/970E5/btrPXtFMr4S/0YRqTG6M2tcz7SlkBsi1k0/img.png)

---

### **4. data**

-   Vue instance의 **데이터 객체** 혹은 **인스턴스 속성**
-   데이터 객체는 반드시 기본 객체 **{ }(Object)** 여야 함
-   객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
-   정의된 속성은 **interpolation {{ }}** 을 통해 view에 렌더링 가능함

-   Vue instance에 **data 객체** 추가
-   data 객체에 message 값 추가
-   결과 확인
-   추가된 객체의 각 값들은 **this.message** 형태로 접근 가능

![](https://k.kakaocdn.net/dn/bvgE3q/btrPYDVJ56E/sEMmt68s4GrK2shSjwKol0/img.png)

![](https://k.kakaocdn.net/dn/wFbpS/btrP0hdSHWI/g6Y0YlRWkH6Pf12U2xDjc0/img.png)

> **methods**

-   Vue instance의 **method**들을 정의하는 곳
-   **methods** 객체 정의
    -   객체 내 **print method** 정의
    -   print method 실행 시 Vue instance의 data 내 message 출력
-   콘솔창에서 app.print() 실행

![](https://k.kakaocdn.net/dn/3fXBz/btrP320LXAd/m2WrbbGUoUYU2khvCjyQbk/img.png)

![](https://k.kakaocdn.net/dn/bePa3m/btrP3Chattm/8zEnZC1ajk3sk2ZG8CzrmK/img.png)

-   method를 호출하여 data 변경 가능
    -   객체 내 **bye method 정의**
    -   print method 실행 시 Vue instance의 data 내 message 변경
-   콘솔창에서 **app.bye()** 실행
    -   DOM에 바로 변경된 결과 반영
    -   Vue의 강력한 반응성(reactivity)

![](https://k.kakaocdn.net/dn/mFJ7u/btrP3joGVxM/4G0ROiSv5hYNKJUlJCmxZK/img.png)

![](https://k.kakaocdn.net/dn/Q5Nvf/btrP19GEUrZ/14BKzlyQQEYG0KKvyMyKwK/img.png)

![](https://k.kakaocdn.net/dn/JNRmc/btrP3kVrl40/EqbNcYaWJssC8d69wEE4aK/img.png)

**※ 주의 - methods with Arrow Function**

-   메서드를 정의 할 때, Arrow Function을 사용하면 안 됨
-   Arrow Function의 this는 함수가 선언될 때 상위 스코프를 가리킴
-   즉 this가 상위 객체 window를 가리킴
-   호출은 문제 없이 가능하나 this로 Vue의 data를 변경하지 못함

![](https://k.kakaocdn.net/dn/IEM2s/btrP3myWsSa/QezZInN8XRdbkkcEDufh41/img.png)

![](https://k.kakaocdn.net/dn/cwcLHE/btrPYD9jJmC/5ecKhwnJYxoJambxQlrYnK/img.png)

### **1. this?**

> **this**

-   어떠한 object를 가리키는 키워드
    -   (**java에서의 this**와 **python에서의 self**는 인스턴스 **자기자신**을 가리킴)
-   JS의 함수는 호출될 때 this를 암묵적으로 전달 받음
-   JS에서의 this는 일반적인 프로그래밍 언어에서의 this와 조금 다르게 동작
-   JS는 해당 **함수 호출 방식**에 따라 this에 바인딩 되는 객체가 달라짐
-   즉, 함수를 선언할 때 this에 객체가 결정되는 것이 아니고, 함수를 호출할 때 **함수가 어떻게 호출 되었는지에 따라 동적으로 결정**됨

---

### **2. this INDEX**

> **전역 문맥에서의 this**

-   브라우저의 전역 객체인 **window**를 가리킴
-   전역객체는 모든 객체의 **유일한 최상위 객체**를 의미

![](https://k.kakaocdn.net/dn/cfTcTH/btrPsZYx8sC/UnkGCJ3kBmaU422IkKGxRK/img.png)

> **함수 문맥에서의 this**

-   함수의 this 키워드는 다른 언어와 조금 다르게 동작
    -   this의 값은 **함수를 호출한 방법에 의해 결정**됨
    -   함수 내부에서 this의 값을 함수를 호출한 방법에 의해 좌우됨

  **1. 단순 호출**

-   전역 객체를 가리킴
-   전역은 브라우저에서는 window, Node.js는 **global**을 의미함 

![](https://k.kakaocdn.net/dn/oNYGn/btrPrrOLgo3/cgA22GTeBUBQbModfEzZk1/img.png)

  **2. Method (Function in Object, 객체의 메서드로서)**

-   메서드로 선언하고 호출한다면, 객체의 메서드이므로 해당 객체가 바인딩 

![](https://k.kakaocdn.net/dn/S5nNx/btrPtwBzgOA/rtGyFxDCx3oN2uspnd2QK0/img.png)

  **3. Nested (화살표 함수)**

-   forEach의 콜백 함수에서의 this가 메서드의 객체를 가리키지 못하고 전역 객체 window를 가리킴
-   **단순 호출 방식**으로 사용되었기 때문
-   이를 해결하기 위해 **"화살표 함수 사용"**
-   이전에 일반 function 키워드와 달리 메서드의 객체를 잘 가리킴
-   화살표 함수에서 this는 자신을 감싼 정적 범위
-   자동으로 한 단계 상위의 scope의 context를 바인딩

![](https://k.kakaocdn.net/dn/dl5QVm/btrPrq982fP/YBaibKkOgPegP7HPGpTOKK/img.png)

> **화살표 함수**

-   화살표 함수는 호출의 위치와 상관없이 **상위 스코프**를 가리킴 (Lexical scope this)
-   **Lexical scope**  
    -   함수를 어디서 호출하는지가 아니라 **어디에 선언**하였는지에 따라 결정
    -   Static scope 라고도 하며 대부분의 프로그래밍 언어세어 따르는 방식
-   따라서, 함수 내의 함수 상황에서 화살표 함수를 쓰는 것을 권장

> **this와 addEventListener**

-   **하지만**
    -   addEventListener에서의 콜백 함수는 특별하게 function 키워드의 경우 **addEventListener**를 호출한 대상을 (event.target) 뜻함
    -   반면 화살표 함수의 경우 상위 스코프를 지칭하기 때문에 window 객체가 바인딩 됨
    -   결론
        -   "addEventListener의 콜백 함수는 function 키워드를 사용하기"

![](https://k.kakaocdn.net/dn/b8Ak96/btrPpXtBKz4/wGQgx1v2D2g35ei99N0cb0/img.png)

**※ this가 호출되는 순간에 결정되는 것 (런타임)** 

-   장점
    -   함수 (메서드)를 하나만 만들어서 여러 객체에서 재사용할 수 있다.
-   단점
    -   위와 같은 유연함이 실수로 이어질 수 있다는 것은 단점
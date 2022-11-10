
### **목차**

1.  Lifecycle Hooks
2.  created, mounted, updated
3.  특징

---

### **1. Lifecycle Hooks**

-   각 Vue 인스턴스는 생성과 소멸의 과정 중 **단계별 초기화 과정**을 거침
    -   Vue 인스턴스가 생성된 경우, 인스턴스를 DOM에 마운트하는 경우, 데이터가 변경되어 DOM를 업데이트하는 경우 등
-   각 단계가 **트리거가 되어 특정 로직을 실행**할 수 있음
-   이를 **Lifecycle Hooks**이라고 함
-   아래 **빨간 부분**들이 Lifecycle Hooks

![](https://k.kakaocdn.net/dn/b8eGHb/btrQrHDZgtr/AmRLNedZ8LtTJyMLe592M0/img.png)

![](https://k.kakaocdn.net/dn/c8XL3B/btrQuIBUG2B/NMXOp5xJYK9QtqnnjTlTk1/img.png)

> **Lifecycle Hooks 간단히 알아보기**

-   ChildComponents.vue에 작성해주기
-   mounted 까지가 Lifecycle Hook 중 1개

![](https://k.kakaocdn.net/dn/DuHsV/btrQxbYt2cM/nI7m3JbmQS4AqR3gbW8x20/img.png)

![](https://k.kakaocdn.net/dn/etAXOX/btrQDc2XDKr/kPyPK2WqjVqaFyAG8xuyV0/img.png)

-   change value 버튼 클릭스 2개의 값이 log에 더 들어온다.
-   Lifecycle Hook 중 1개

![](https://k.kakaocdn.net/dn/O1vLV/btrQC8TUYNl/eZux98N06MAocTCgPQ9Y7K/img.png)

![](https://k.kakaocdn.net/dn/cyfjdj/btrQvYE6DgR/fSAXRANITAC7sAXCKIMMO0/img.png)

-   toggle 버튼을 통해 삭제할 수 있다.
-   Lifecycle Hook 중 1개

![](https://k.kakaocdn.net/dn/dX6nsI/btrQtRzJNFG/915s3wEg9swKE0VBeegak1/img.png)

---

### **2.** **created, mounted, updated**

> **created**

-   Vue instance가 **생성된 후 호출**됨
-   data, computed 등의 설정이 완료된 상태
-   서버에서 받은 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적합
-   **단, mount 되지 않아 요소에 접근할 수 없음 -> DOM에 대한 조작 xxx** 
-   버튼을 누르면 강아지 사진을 보여주었던 앞선 예를 -> 버튼을 누르지 않아도 첫 실행 시 기본 사진이 출력되도록 하고 싶다면?
    -   => **created 함수에 강아지 사진을 가져오는 함수를 추가**
    -   **method 안에 추가 xxx**

![](https://k.kakaocdn.net/dn/UHpQ0/btrQAwOB2pq/xrKqNayexknBHUF4zBBMsK/img.png)

> **mounted**

-   Vue instance가 요소에 mount된 후 호출됨
-   **mount된 요소를 조작**할 수 있음
-   -> toggle 버튼이 멍멍으로 바뀜

![](https://k.kakaocdn.net/dn/Kz2MK/btrQyvvMh6l/nKQMFlY9Kqez9lLMafmxe1/img.png)

-   **created**의 경우, mount 되기 전이기 때문에 **DOM**에 접근할 수 없으므로 동작하지 않음
-   mounted는 주석 처리

![](https://k.kakaocdn.net/dn/bn8SFr/btrQz54GsB5/eSGTWuI8jHnSKHKaM6eS20/img.png)

> **updated**

-   데이터가 변경되어 DOM에 변화를 줄 때 호출 됨

![](https://k.kakaocdn.net/dn/bJUD33/btrQtTdjGt7/PK0Jr3DfbTH5Q6sJs15E3k/img.png)

![](https://k.kakaocdn.net/dn/bscFZZ/btrQCh4LpiL/7cYgvI7bz9GWi8tdq8UHgK/img.png)

---

### **3. Lifecycle Hooks 특징**

-   instance마다 각각의 Lifecycle을 가지고 있음

![](https://k.kakaocdn.net/dn/1v96R/btrQw2tT0oR/ZItpmbQ1i6KH1Ixcxi0KPk/img.png)

dog component

-   Lifecycle Hooks는 컴포넌트별로 정의할 수 있음
-   현재 해당 프로젝트는
-   **App.vue 생성 => ChildComponent 생성 => ChildComponent 부착 => App.vue 부착 => ChildComponent 업데이트 순으로 동작한 것**

![](https://k.kakaocdn.net/dn/sSl0P/btrQuJhlGzX/oOU1bWEXa0QbHVpMBEX5H0/img.png)

-   부모 컴포넌트의 mounted hook이 실행 되었다고 해서 자식이 mount 된 것이 아니고,
-   부모 컴포넌트가 updated hook이 실행 되었다고 해서 자식이 updated 된 것이 아님
    -   부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않은 것
-   **instance마다 각각의 Lifecycle을 가지고 있기 때문**
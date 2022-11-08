
### **1. DOM**

> **개요**

-   브라우저에서의 JavaScript
    -   웹 페이지에서 복잡한 기능을 구현하는 스크립트 언어
    -   가만히 정적인 정보만 보여주는 것이 아닌 **주기적으로 갱신**되거나, **사용자와 상호 작용이 가능**하거나, **애니메이션이 적용된 그래픽** 등에 관여
-   참고 - **스크립트 언어**
    -   **응용 소프트웨어를 제어하는 컴퓨터 프로그래밍 언어**

> **Browser APIs**

-   웹 브라우저에 내장된 API로, 현재 컴퓨터 환경에 관한 데이터를 제공하거나 여러 가지 유용하고 복잡한 일을 수행
-   종류
    1.  **DOM**
    2.  **Geolocation API**
    3.  **WebGL 등**

> **DOM**

-   **"문서 객체 모델 (Document Object Model)"**
-   문서의 구조화된 표현을 제공하며 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공
    -   문서 구조, 스타일, 내용 등을 변경할 수 있게 도움
    -   HTML 컨텐츠를 추가, 제거, 변경하고, 동적으로 페이지에 스타일을 추가하는 등 HTML/CSS를 조작할 수 있음
-   문서가 구조화되어 있으며 **각 요소는 객체(object)**로 취급
-   단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
-   DOM은 문서를 **논리 트리**로 표현
-   DOM 메서드를 사용하면 프로그래밍적으로 트리에 접근할 수 있고 이를 통해 **문서의 구조, 스타일, 컨텐츠를 변경**할 수 있음

![](https://k.kakaocdn.net/dn/dANDbf/btrPsB4fj6P/Dqk2b8aWTp0KcSutu7OKj0/img.png)

-   웹 페이지는 일종의 문서(document)
-   이 문서는 웹 브라우저를 통해 그 내용이 해석되어 웹 브라우저 화면에 나타나거나 HTML 코드 자체로 나타나기도 함
-   DOM은 **동일한 문서를 표현**하고, **저장**하고, **조작**하는 방법을 제공
-   DOM은 **웹 페이지의 객체 지향 표현**이며, JavaScript와 같은 스크립트 언어를 이용해 DOM을 수정할 수 있음

> **DOM에 접근하기**

-   모든 웹 브라우저는 스크립트 언어가 접근할 수 있는 웹페이지를 만들기 위해 DOM을 항상 사용함
-   "DOM의 주요 객체"들을 활용하여 **문서를 조작**하거나 **특정 요소**들을 얻을 수 있음

> **DOM의 주요 객체**

-   **window**
-   **document**
-   navigator, location, history, screen 등

> **window object**

-   DOM을 표현하는 창
-   가장 최상위 객체 (작성 시 생략 가능)
-   탭 기능이 있는 브라우저에서는 각각의 탭을 각각의 window 객체로 나타냄

![](https://k.kakaocdn.net/dn/Vg4sI/btrPjGTzd8Y/Sodhr8KgvNixfO5dkcok3K/img.png)

**※ 예시**

-   새 탭 열기

![](https://k.kakaocdn.net/dn/Gl6zb/btrPlGFLk3j/3eS0vvu7taMayOAwrzjOEK/img.png)

-   경고 대화 상자 표시

![](https://k.kakaocdn.net/dn/YtZUo/btrPp4TqhcM/gTXt89fS1d7LZL2k49oUqk/img.png)

-   인쇄 대화 상자 표시

![](https://k.kakaocdn.net/dn/czwkIR/btrPthEej2N/jJ9yrvLXMup1ratwfsiqCK/img.png)

> **document object**

-   브라우저가 불러온 웹 페이지
-   페이지 컨텐츠의 진입점 역할을 하며, <body> 등과 같은 수많은 다른 요소들을 포함하고 있음

![](https://k.kakaocdn.net/dn/FvxUA/btrPrm7nWIw/W3Mh5vnlNWWDrX1Q0w2h81/img.png)

-   document.title

![](https://k.kakaocdn.net/dn/Nss78/btrPp4TrgJu/qKWg5KJztBWQdhBbSREfn0/img.png)

-   **참고** - document는 window의 **속성**이다 ( window.document )
-   **참고 - 파싱 (Parsing)**
    -   구문 분석, 해석
    -   브라우저가 문자열을 해석하여 DOM Tree로 만드는 과정

![](https://k.kakaocdn.net/dn/lXvRp/btrPs3TJ9et/qkxUNRLZDDzgS31FCKn3b1/img.png)

---

### **2.  DOM 조작**

> **선택 관련 메서드**

-   document.**querySelector**(selector)
    -   제공한 선택자와 일치하는 element 한 개 선택
    -   제공한 CSS selector를 만족하는 첫 번째 element 객체를 반환 (없다면 null 반환)
-   document.**querySelectorAll**(selector)
    -   제공한 선택자와 일치하는 여러 element를 선택
    -   매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음
    -   제공한 CSS selector를 만족하는 NodeList를 반환

![](https://k.kakaocdn.net/dn/bfRIlh/btrPmEuiHut/bncF96ZaRi4OfK9A5xORAK/img.png)

![](https://k.kakaocdn.net/dn/bZd6rY/btrPox2Gr0M/MtsrXo8CqvFIf1RoE5ImfK/img.png)

![](https://k.kakaocdn.net/dn/QXUoU/btrPkpYGNz1/KgBiP31mg3Eul4OJI8s451/img.png)

**※ 참고 - NodeList**

-   **index**로만 각 항목에 접근 가능
-   배열의 forEach 메서드 및 다양한 배열 메서드 사용 가능
-   querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 **실시간으로 반영하지 않음**

> **조작 관련 메서드 (생성)**

-   document**.createElement**(tagName)
    -   작성한 tagName의 HTML 요소를 생성하여 반환

> **조작 관련 메서드 (입력)**

-   **Node.innerText**
    -   **Node 객체**와 그 **자손의 텍스트 컨텐츠(DOMString)**를 표현 (해당 요소 내부의 raw text)
    -   사람이 읽을 수 있는 요소만 남김
    -   즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현

> **조작 관련 메서드 (추가)**

-   Node**.appendChild()**
    -   한 Node를 **특정 부모 Node의 자식 NodeList 중 마지막 자식**으로 삽입
    -   한 번에 **오직 하나**의 Node만 추가할 수 있음
    -   추가된 **Node 객체를 반환**
    -   만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 현재 위치에서 새로운 위치로 이동

> **조작 관련 메서드 (삭제)**

-   **Node.removeChild()**  
    -   DOM에서 자식 Node를 제거
    -   제거된 Node를 반환

![](https://k.kakaocdn.net/dn/LBE9g/btrPlH5T6Wu/FWFrbmT7qlMJ0Zi15KIKA0/img.png)

태그 생성 후 화면에 표시해주기

![](https://k.kakaocdn.net/dn/rMb0y/btrPtwagdkq/X3WpSEejLjojNcIXu65WbK/img.png)

> **조작 관련 메서드 (속성 조회 및 설정)**

-   Element**.getAttribute**(attributeName)
    -   해당 요소의 지정된 값(문자열)을 반환
    -   인자(attributeName)는 값을 얻고자 하는 속성의 이름
-   Element**.setAttribute**(name, value)
    -   지정된 요소의 값을 설정
    -   속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가

![](https://k.kakaocdn.net/dn/bL5nIE/btrPmFfFMfi/b2S2moANWAz1EzFGlYNrL0/img.png)

![](https://k.kakaocdn.net/dn/bPMG7g/btrPrqvkV10/U5lmQvWGhTezqQufPI1yL1/img.png)

![](https://k.kakaocdn.net/dn/bSdbQi/btrPrr14YrB/PHc8So3Tak4ltEIIVzOgt1/img.png)

-   메서드는 공홈 참고하기 -> mdn classList
-   **toggle**의 경우 삭제가 아닌 추가!

### **1. Event**

-   **Event**란 프로그래밍하고 있는 시스템에서 일어나는 **사건(action) 혹은 발생(occurrence)**인데, 우리가 원한다면 그것들에 **어떠한 방식으로 응답할 수 있도록 시스템이 말해주는 것**
    -   예를 들어 사용자가 웹 페이지의 버튼을 클릭한다면 우리는 클릭이라는 사건에 대한 결과를 응답받기를 원할 수 있음
-   클릭 말고도 웹에서는 각양각색의 Event가 존재
    -   키보드 키 입력, 브라우저 닫기, 데이터 제출, 텍스트 복사 등

> **Event object**

-   네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
-   Event 발생
    -   마우스를 클릭하거나 키보드를 누르는 등 사용자 행동으로 발생할 수도 있고
    -   **특정 메서드를 호출**하여 프로그래밍적으로도 만들어 낼 수 있음
-   DOM 요소는 Event를 받고 ("**수신**")
-   받은 Event를 **"처리"**할 수 있음
    -   Event 처리는 주로 **addEventListener()**라는 **Event 처리기 (Event handler)**를 사용해 다양한 html 요소에 **"부착"**하게 됨

> **Event handler - addEventListener()**

**"대상에 특정 Event가 발생하면, 할 일을 등록하자"**

**EventTarget.addEventListener(type, listener)**

-   **EventTarget.addEventListener(type, listener[, options])**
    -   지정한 Event가 대상에 전달될 때마다 호출할 함수를 설정
    -   Event를 지원하는 모든 객체(Element, Document, Window 등)를 대상(EventTarget)으로 지정 가능
    -   **type**
        -   반응 할 Event 유형을 나타내는 대소문자 구분 문자열
        -   대표 이벤트
        -   **input, click, submit ...**
        -   [https://developer.mozilla.org/en-US/docs/Web/Events](https://developer.mozilla.org/en-US/docs/Web/Events)
    -    **listener**
        -   지정된 타입의 Event를 수신할 객체
        -   JavaScript function 객체(콜백 함수)여야 함
        -   콜백 함수는 발생한 Event의 데이터를 가진 Event 기반 객체를 **유일한 매개변수**로 받음

**※ input**

![](https://k.kakaocdn.net/dn/d1VeOx/btrPthEtRTH/OOG8RiqekUxIvazsPZxi81/img.png)

![](https://k.kakaocdn.net/dn/bcGbEC/btrPs3Nb7fs/kqVfBW36aQ9XJSFnZ06Ok1/img.png)

**※ button**

![](https://k.kakaocdn.net/dn/bofDWz/btrPtIPkv1F/LdkhcVGYsklFyom6qO2Cmk/img.png)

![](https://k.kakaocdn.net/dn/AVrgL/btrPp4sFvOT/Ld9hTlEy0rB7JRjrhvjhZ1/img.png)

**※ 같이 적용해보기**

  **- 클릭시 blue로 변경**

![](https://k.kakaocdn.net/dn/bJlN4D/btrPsBQ2km7/0yvDiYPBKyyVfLKkTOpgrK/img.png)

![](https://k.kakaocdn.net/dn/db2I5G/btrPoQ9fByk/RXFUOnkgJTr4YHXSwrIKrk/img.png)

![](https://k.kakaocdn.net/dn/dLStEw/btrPlbF5I2e/4zKKfdB1j4tLvJsudzNOb1/img.png)

---

### **2. Event 취소**

> **event.preventDefault()**

-   현재 Event의 기본 동작을 중단
-   HTML 요소의 기본 동작을 작동하지 않게 막음
-   HTML 요소의 기본 동작 예시
    -   **a 태그** : 클릭 시 특정 주소로 이동
    -   **form 태그** : form 데이터 전송

**※ preventDefault 예시**

**- 웹 페이지 내용을 복사하지 못하도록 하기**

![](https://k.kakaocdn.net/dn/1GkC8/btrPox9DM6y/LLcGX71M4QG8fazHaMvfZ1/img.png)

![](https://k.kakaocdn.net/dn/OJw2R/btrPsAdwQ73/4yFJ2Ef2QJAsMaSKPvgGyK/img.png)

---

### **3. Event 종합**

**※ 참고 - lodash**

-   모듈성, 성능 및 추가 기능을 제공하는 **JavaScript 유틸리티 라이브러리**
-   array, object 등 자료 구조를 다룰 때 사용하는 유용하고 간편한 유틸리티 함수들을 제공
-   함수 예
    -   reverse, sortBy, range, random ...
    -   https://lodash.com/ 

```
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
```

> **랜덤 번호 6개 추출하여 공에 넣어주기**

```
<style>
    /* 스타일은 수정하지 않습니다. */
    .ball {
      width: 10rem;
      height: 10rem;
      margin: .5rem;
      border-radius: 50%;
      text-align: center;
      line-height: 10rem;
      font-size: xx-large;
      font-weight: bold;
      color: white;
    }
    .ball-container {
      display: flex;
    }
  </style>
</head>
<body>
  <h1>로또 추천 번호</h1>
  <button id="lotto-btn">행운 번호 받기</button>
  <div id="result"></div>

  <!-- lodash 이용하는 src -->
  <script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>  
  <script>
    const btn = document.querySelector('#lotto-btn')
    btn.addEventListener('click', function (event) {
      
      // 공이 들어갈 컨테이너 생성
      const ballContainer = document.createElement('div')
      ballContainer.classList.add('ball-container')

      // 랜덤한 숫자 6개를 만들기
      // lodash의 메서드
      let numbers = _.sampleSize(_.range(1, 46), 6)
      // 정렬 해주기
      numbers = _.sortBy(numbers)
      console.log(numbers)

      // 공 만들기
      numbers.forEach((number) => {
        const ball = document.createElement('div')
        ball.innerText = number
        ball.classList.add('ball')
        ball.style.backgroundColor = 'crimson'
        ballContainer.appendChild(ball)
      })
      // 공 컨테이너는 결과 영역의 자식으로 넣기
      const resultDiv = document.querySelector('#result')
      resultDiv.appendChild(ballContainer)
    })
  </script>
</body>
```

![](https://k.kakaocdn.net/dn/cK7Y1n/btrPtjoPHqJ/e3k21iGzITl7Vsl1IAuk5k/img.png)

> **ToDo 리스트 만들기**

```
<body>
  <form action="#">
    <input type="text" class="inputData">
    <input type="submit" value="Add">
  </form>
  <ul></ul>

  <script>
    const formTag = document.querySelector('form')

    formTag.addEventListener('submit', function (event){
      event.preventDefault()
      
      // . 은 클래스 선택자
      const inputTag = document.querySelector('.inputData')
      const data = inputTag.value
      console.log(data)

      // 데이터가 있다면 진행하는 조건문
      if (data.trim()) {
        const liTag = document.createElement('li')
        liTag.innerText = data

        const ulTag = document.querySelector('ul')
        ulTag.appendChild(liTag)
        event.target.reset()
      } else {
        alert('내용을 입력하세요!')
      }
    })
  </script>
</body>
</html>
```

![](https://k.kakaocdn.net/dn/dgU1Uk/btrPla8ihQc/tpr6Qz1YcVHiJxLmkkRyxk/img.png)

콜백 함수로 만들어주기

```
<script>
    const formTag = document.querySelector('form')

    const addTodo = function (event){
      event.preventDefault()
      
      // . 은 클래스 선택자
      const inputTag = document.querySelector('.inputData')
      const data = inputTag.value
      console.log(data)

      // 데이터가 있다면 진행하는 조건문
      if (data.trim()) {
        const liTag = document.createElement('li')
        liTag.innerText = data

        const ulTag = document.querySelector('ul')
        ulTag.appendChild(liTag)
        event.target.reset()
      } else {
        alert('내용을 입력하세요!')
      }

    }
    formTag.addEventListener('submit', addTodo)
  </script>
```
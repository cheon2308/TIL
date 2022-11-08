
### **1. AJAX**

-   **비동기 통신**을 이용하면 화면 전체를 새로고침 하지 않아도 서버로 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 가능
-   이러한 '**비동기 통신 웹 개발 기술**'을 Asynchronous JavaScript And XML(AJAX)라 한다.
-   **AJAX의 특징**
    1.  페이지 새로고침 없이 서버에 요청
    2.  서버로부터 응답(데이터)을 받아 작업을 수행
-   이러한 비동기 웹 통신을 위한 라이브러리 중 하나가 **Axios**

---

### **2. 비동기 적용하기**

비동기 적용을 위한 준비사항 2가지

-   M:N 구현한 Django 프로젝트 준비 
-   가상 환경 생성 및 활성화, 패키지 설치

> **팔로우(follow)**

-   각 템플릿에서 script코드를 작성하기 위한 **block tag 영역** base.html에 작성해주기

![](https://k.kakaocdn.net/dn/bBk1Y2/btrPHyezpMU/5gPnQcCVEgoEYrqb6WCQ2K/img.png)

-   axios CDN 작성

![](https://k.kakaocdn.net/dn/9dACw/btrPE5qOMfe/XOIz800Z77VZdCTWxstYAk/img.png)

-   form 요소 선택을 위해 id 속성 지정 및 선택
-   불필요해진 action과 method 속성은 삭제 (요청은 axios로 대체되기 때문)
-   form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소

![](https://k.kakaocdn.net/dn/b9gV6T/btrPEk2XJnh/VaLtUzNZqokNNE9Hspu10K/img.png)

-   axios 요청 준비

![](https://k.kakaocdn.net/dn/beKvNV/btrPFCu2EMn/Aapkju5gPBDt7MHjumxrR0/img.png)

---

#### **2-1. POST 요청 보내기**

현재 axios로 POST 요청을 보내기 위해 필요한 것

1.  **url에 작성할 user pk는 어떻게 작성해야 할까?**
2.  csrftoken은 어떻게 보내야 할까?

> **url에 작성할 user pk 가져오기 (HTML -> JavaScript)**

![](https://k.kakaocdn.net/dn/F5wBU/btrPEpDi2Qu/4uZng32e6juyM0zQQhjIZ1/img.png)

![](https://k.kakaocdn.net/dn/cv8Omq/btrPDlnV28p/ij6DfIidDHakFqYi1IgLf0/img.png)

-   url 작성 마치기

![](https://k.kakaocdn.net/dn/qPMlO/btrPGOojXXB/NJAIevGFormJfOrsKJ04Ik/img.png)

> **data-* attributes**

-   사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환 할 수 있는 방법
-   모든사용자 지정 데이터는 dataset 속성을 통해 사용할 수 있음
-   https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes/data-*

```
<div data-my-id="my-data"></div>
<script>
  const myId = event.target.dataset.myId
</script>
```

-   예를 들어, **data-test-value** 라는 이름의 특성을 지정했다면 JavaScript에서는 **element.dataset.testValue**로 접근할 수 있음
-   속성명 작성 시 **주의사항**
    -   대소문자 여부에 상관없이 xml로 시작하면 안 됨
    -   세미콜론을 포함해서는 안 됨
    -   대문자를 포함해서는 안 됨

> **csrftoken 보내기**

-   먼저 hidden 타입으로 숨겨져 있는 csrf 값을 가진 input 태그를 선택해야 함
-   https://docs.djangoproject.com/en/3.2/ref/csrf/

![](https://k.kakaocdn.net/dn/bcVzGT/btrPDHxvoze/EgK9OVxmMvbClHkAyw83M1/img.png)

![](https://k.kakaocdn.net/dn/7gWii/btrPEDBmmL5/MFvMUx6qHs6aWkc95ql0kK/img.png)

-   AJAX로 csrftoken을 보내는 방법
-   https://docs.djangoproject.com/en/3.2/ref/csrf/#setting-the-token-on-the-ajax-request

![](https://k.kakaocdn.net/dn/nBv3D/btrPDkvGfcB/yRMSCWnA45T4yka40oC9V0/img.png)

-   팔로우 버튼을 토글하기 위해서는 현재 팔로우가 된 상태인지 여부 확인이 필요
-   axios 요청을 통해 받는 response 객체를 활용해 view 함수를 통해서 팔로우 여부를 파악 할 수 있는 변수를 담아 JSON 타입으로 응답하기

![](https://k.kakaocdn.net/dn/bnDzMV/btrPDfaomdH/cnrLviD4gXCbXZ6G3rhjkK/img.png)

![](https://k.kakaocdn.net/dn/r5ue3/btrPFxUVSi3/gMfJuAw75McPtbKDyalmTK/img.png)

-   vidw 함수에서 응답한 is_followed를 사용해 버튼 토글하기

![](https://k.kakaocdn.net/dn/SqsTY/btrPDeP6SGs/iODqt4Q5HSkDkFMcWbqIz0/img.png)

**※ 참고 - XHR**

-   "XMLHttpRequest"
-   AJAX 요청을 생성하는 JavaScript API
-   XHR의 메서드로 브라우저와 서버 간 네트워크 요청을 전송할 수 있음
-   **Axios**는 손쉽게 XHR을 보내고 응답 결과를 Promise 객체로 반환해주는 라이브러리

---

#### **2-2. 팔로워 & 팔로잉 수 비동기 적용**

-   해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성

![](https://k.kakaocdn.net/dn/cueUZo/btrPEkaVezi/bHpYNTv2SJ4XH4uWq6JixK/img.png)

-   직전에 작성한 span 태그를 각각 선택

![](https://k.kakaocdn.net/dn/cSCPY8/btrPGOBTbDE/4gyqhniElo7ZF4cskswoSk/img.png)

-   팔로워, 팔로잉 이원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달

![](https://k.kakaocdn.net/dn/cTCNxX/btrPFZwVY9g/Rg78GFKqbK2CGoL65yzAQ0/img.png)

-   view 함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경하기 in **.then()**

![](https://k.kakaocdn.net/dn/T9ijI/btrPDzMSAIQ/cmCDMqoGxmQRP7kXcB8811/img.png)

> **최종 코드**

![](https://k.kakaocdn.net/dn/bta8CJ/btrPHx7R4yr/gmQkSpwFSak1zknDIjpCIK/img.png)

![](https://k.kakaocdn.net/dn/bBIdXc/btrPEodmfCv/LquVH50RoGeft1cMANdb3K/img.png)

![](https://k.kakaocdn.net/dn/PIndC/btrPFDgquTx/Ijc4ofgKMIEQkvNCkJOVC0/img.png)

---

#### **2-3. 좋아요 (like)**

-   좋아요 비동기 적용은 "팔로우와 동일한 흐름 + **forEach() & querySelectorAll()**"
    -   index 페이지 각 게시글에 좋아요 버튼이 있기 때문

![](https://k.kakaocdn.net/dn/dzkXTT/btrPDA58gNf/ugKcvZaLZCUZ9k3HP4DO81/img.png)

![](https://k.kakaocdn.net/dn/dmFWRf/btrPEjiIZuj/nVIOHT741QkZyKDVJXjRVK/img.png)

![](https://k.kakaocdn.net/dn/dG0UKE/btrPGQfp25K/Q00yooVkkk8L1lVtbebtv0/img.png)
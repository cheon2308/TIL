
> **Axios**

-   JavaScript의 HTTP 웹 통신을 위한 라이브러리
-   확장 가능하나 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능을 제공
-   node 환경은 npm을 이용해서 설치 후 사용할 수 있고, browser 환경은 CDN을 이용해서 사용할 수 잇음
    1.  https://axios-http.com/kr/docs/intro
    2.  https://github.com/axios/axios

> **기본 구조**

![](https://k.kakaocdn.net/dn/4efwY/btrPGdO6tg3/gCUAnRfGCl4WSfyZCdetk0/img.png)

-   get, post 등 여러 method 사용가능
-   **then**을 이용해서 성공하면 수행할 로직을 작성
-   **catch**를 이용해서 실패하면 수행할 로직을 작성

> **고양이 사진 가져오기**

-   The Cat API (https://api.thecatapi.com/v1/images/search)
    -   이미지를 요청해서 가져오는 작업을 비동기로 처리
-   **response** **구조**

![](https://k.kakaocdn.net/dn/b2VQo6/btrPCCXJWcA/jJkYtYATk0Abmxq9IXgE41/img.png)

-   Axios로 요청해보기 (비동기)

![](https://k.kakaocdn.net/dn/VUJln/btrPFXZRy2x/4d4Dc76p1r7imKJvGDiwRK/img.png)

![](https://k.kakaocdn.net/dn/qAtDZ/btrPED19KiD/CKFBrqE8C55w3XB93e4sAk/img.png)

> **파이썬과 비교**

-   동기식인 파이썬의 경우 첫번째 print가 출력되고 이미지를 가져오는 처리를 기다렸다가 다음 print가 출력되는 반면
-   **비동기식 코드**는 **바로 처리가 가능한 작업(console.log)은 바로 처리**하고, 오래 걸리는 작업인 이미지를 요청하고 가져오는 일은 **요청을 보내 놓고** 기다리지 않고 다음 코드로 **진행 후 완료가 된 시점에 결과 출력이 진행**됨

> **고양이 사진 가져오기 (완성)**

-   Flow
    1.  버튼을 누르면
    2.  고양이 이미지를 요청하고
    3.  요청이 처리되어 응답이 오면
    4.  처리된 response에 있는 url을 img 태그에 넣어 보여주기

![](https://k.kakaocdn.net/dn/TGHo9/btrPE6iJyv9/G6jMgMb1e0JbQEmSI8Cpk0/img.png)

![](https://k.kakaocdn.net/dn/es94Gt/btrPCD3se9c/uB9S794btT3yQf2h6iMgA0/img.png)

-   버튼을 누르면 console.log가 먼저 출력되고 이미지 요청 보낸다.
-   버튼을 여러 번 누르면 먼저 로딩되는 이미지부터 나오는 것을 볼 수 있다.
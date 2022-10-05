내가 원하는 그림, 이미지, 글 등을 집어넣는데 크기가 조절이 안되고 위치를 옮기지 못한다면 어떨까?

굉장히 불편할 것이다! 이런 불편함 들을 해결하기 위하여 이번 글에서는 크기, 색상 등을 손쉽게 바꾸는 방법을 알아보자.

> **크기 단위**

-   px (픽셀)
    -   모니터 해상도의 한 화소인 '픽셀' 기준
    -   픽셀의 크기는 변하지 않기 때문에 고정적인 단위
-   %
    -   백분율 단위
    -   가변적인 레이아웃에서 자주 사용
-   em
    -   (바로 위, 부모 요소에 대한) 상속의 영향을 받음
    -   배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
-   rem
    -   (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
    -   최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

![](https://blog.kakaocdn.net/dn/FExsx/btrI2xt90lv/iOjwF6TXWhUNKX9wTi7HJ1/img.png)

직접 해보며 비교해보자! 특히 **em과 rem의 차이**를 잘 알아두면 사용할 때 편하다.

> 일반적으로 기본 **HTML의 경우 16px**, 아무 설정 안 된 **기본 크기는 36px** 이다  
> 따라서, 2em의 경우 72px, 2rem의 경우 32px이 될 것이다.

무엇보다 모바일과 데스크톱으로 보는 화면의 크기가 같다면 정말 불편할 것이다. 이런 불편함을 해소해주기 위하여 **viewport**라는 크기 개념을 꼭 짚고 넘어가야 한다.

-   웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
-   디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
-   vw, vh, vmin, vmax

![](https://blog.kakaocdn.net/dn/d6aH3O/btrI6q1R3X9/c9nrGVE2tAPzkLYw2vWzu1/img.png)

위의 코드를 실행시킨 후 px과 vw의 차이를 찾아보자. 바로 찾을 수 있을 것이다.

바로 **브라우저의 크기에 영향을 받는 유/무의 차이**이다!! 절대적인과 상대적인의 개념이라 보면 된다. 어렵지 않으니 각 요소들이 필요한 경우에 잘 사용하면 된다.

> 색상 단위

-   **색상 키워드 (background-color: red;)**
    -   대소문자를 구분하지 않음
    -   red, blue, black과 같은 특정 색을 직접 글자로 나타냄
-   **RGB 색상 (background-color: rgb(0, 255, 0);)**
    -   16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
-   **HSL 색상 (background-color: hsl(0, 100%, 50%);)**
    -   색상, 채도, 명도를 통해 색을 표현하는 방식
    -   hsla의 경우 alpha는 투명도

![](https://blog.kakaocdn.net/dn/bZSccw/btrI1VPMSEb/rXq7l9EOL1hFTPJeUKg1r1/img.png)

같은 검은색 이어도 이렇게 다양하게 표현이 된다!

> 문서를 표현하기 위한 다양한 단위

-   텍스트
    -   서체(font-style), 서체 스타일(font-style, font-weight 등)
    -   자간(letter-spacing), 단어 간격(word-spacing), 행간(line-height) 등
-   컬러, 배경(background-image, background-color)
-   기타 HTML 태그별 스타일링
    -   목록(li), 표(table)

자세한 건 추후에 하나씩 실습을 통해 알아
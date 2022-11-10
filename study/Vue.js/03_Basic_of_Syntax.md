
> **Template Syntax**

-   Vue 2 guide > template syntax 참고
-   **렌더링 된** **DOM**을 기본 Vue instance의 data에 **선언적으로 바인딩**할 수 있는 **HTML 기반 template syntax**를 사용
    -   렌더링 된 DOM - 브라우저에 의해 보기 좋게 그려질 HTML 코드
    -   HTML 기반 template syntax - HTML 코드에 직접 작성할 수 있는 문법 제공
    -   선언적으로 바인딩 - Vue instance와 DOM을 연결

> **Template Interpolation**

-   가장 기본적인 바인딩(연결) 방법
-   중괄호 2개로 표기
-   DTL과 동일한 형태로 작성
-   Template interpolation 방법은 HTML을 **일반 텍스트**로 표현

![](https://k.kakaocdn.net/dn/vKHIn/btrP3zZj38b/Bj0aoEh427ddL1csa1KbXK/img.png)

![](https://k.kakaocdn.net/dn/cRUeTf/btrP3ARrbmF/KFlVTm0kmLpg9bz126ER91/img.png)

> **RAW HTML**

-   **v-html** directive을 사용하여 data와 바인딩
-   directive - HTML 기반 template syntax
-   HTML의 기본 속성이 아닌 Vue가 제공하는 특수 속성의 값으로 data를 작성
-   **※ 참고 - 표현식 형태로 작성가능**

![](https://k.kakaocdn.net/dn/byvvbD/btrP3yzolxR/1QJvV44BcywBuelnIQwBkk/img.png)

![](https://k.kakaocdn.net/dn/taWEW/btrP3ChqyII/fP4pLf4aGTfM5hkB2pKyCK/img.png)

![](https://k.kakaocdn.net/dn/xHcso/btrP3699swS/fE7MfHqjle9ybsB5B67dkK/img.png)
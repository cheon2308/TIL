이번 시간부터는 **표현**을 하기위한 CSS에 대해 배워볼 것인데 개인적으로는 글을 읽으며 **실습**을 하는 것을 추천한다!

> Cascading Style Sheets = CSS

![](https://blog.kakaocdn.net/dn/cq5Zq8/btrI6rNdWGx/7jad8tqkjkdONtJYmLRgI1/img.png)

우리가 자주 사용하는 Naver의 경우 CSS가 없다면 보기가 정말 불편하고 이용하고 싶은 마음이 뚝 떨어진다. CSS를 배우지 않았지만 얼마나 중요한 것인지 알 수 있다.

이처럼 CSS는 **_스타일을 지정하기 위한 언어_**이다.

-   선택자를 통해 스타일을 지정할 HTML 요소를 선택
-   중괄호 안에서는 속성의 값, 하나의 쌍으로 이루어진 선언을 진행
-   각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
    -   속성 (Property) : 어떤 스타일 기능을 변경할지 결정
    -   값 (Value) : 어떻게 스타일 기능을 변경할지 의미

![](https://blog.kakaocdn.net/dn/xLblx/btrI0fBjoBu/AKkkFnFvfagUlK9dyQj131/img.png)

css 구문 예시

대충 어떻게 생겼는지 알아두기만 하고 본격적으로 사용하는 방법에 대해 알아보자!!

#### - CSS를 어떻게 정의 해줄까?

**1. 인라인**

> 해당 태그에 직접 style 속성을 활용한다.

![](https://blog.kakaocdn.net/dn/VpOyP/btrI7Mjh2xs/0CzKPkyBDqnrbo5j30eBXK/img.png)

**2. 내부 참조**

>``` <head>``` 태그 내에 <style>에 지정

![](https://blog.kakaocdn.net/dn/VGm9F/btrI3ucDKyL/N9kzcqgl6OAriCmtnx3Ju0/img.png)

**3. 외부 참조**

>    외부 CSS 파일을 <head> 내 <link>를 통해 불러오기

![](https://blog.kakaocdn.net/dn/cdAN77/btrI1ji3r7B/MKjy7lKF6Spzz6QUp9sfm1/img.png)

위 3가지를 봤을 때 어떤 방법이 제일 좋은 것 같은가?

-   인라인 방법의 경우 실수가 잦아질 수 있다 (내부에 직접 존재하므로 중복도 있을 것이고, 찾기가 어려워서)
-   내부 참조의 경우 ```<style>``` 태그에 정의해주므로 코드가 너무 길어지는 단점이 있다.
-   이미 눈치 챘을 수도 있지만 외부 참조의 방식을 가장 많이 이용한다!

CSS를 본격적으로 배우기 전에 인터넷 창에서 **F12를 누르면 개발자 도구**가 튀어 나온다. 이를 활용해서 사용된 CSS를 확인해보자.

![](https://blog.kakaocdn.net/dn/LGeD3/btrI6r7yuUr/r3kVst8eUDQOGYVyaVKamk/img.png)
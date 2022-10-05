지금까지 HTML로 뼈대를 세우고 CSS로 기본 스타일을 지정해주는 방법을 알아봤다.

그럼 과연 우리가 보고 있는 이 웹 페이지들은 어떻게 구성되어 있는 것일까?

그전에 **CSS 원칙** 하나만 알아보고 가자.

> 모든 요소는 **네모**이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다.

여기서 네모가 뭘까? 바로 오늘 우리가 알아볼 **Box model**을 이르는 말이다.

**모든 HTML의 요소는 BOX 형태로 되어있고 하나의 BOX는 네 부분으로 이루어져 있다!**

오늘 배울게 얼마나 중요한 것인지 와닿을 것이다.

> Box model 구성

![](https://blog.kakaocdn.net/dn/bFZbwf/btrI6dVNZvT/vUkpsxeyW8pQre09BYO25k/img.png)

각각의 영역들의 크기를 따로 설정해 줄 수도 있다!

![](https://blog.kakaocdn.net/dn/QLMQe/btrI3tyqDOu/ode6WSjDqWWk0qZDk80Nt1/img.png)

margin 폭 설정

![](https://blog.kakaocdn.net/dn/JMnLe/btrI6qVwf84/yiDQIrekyG86cxK0njDIK1/img.png)

margin-padding 폭 설정

첫 번째 그림과 같이 top, right 같은 세부 방향을 설정해주지 않고 margin: 10px;라고 선언한다면 상하좌우 모두 같은 값을 가지게 된다!

![](https://blog.kakaocdn.net/dn/c8NI00/btrI2qawzaj/RbKL78YCFM4jfXziOsvogK/img.png)

border 설정

border의 경우 네모박스의 테두리를 이르는 말이다. 헷갈리지 말자!

물론 친절한 CSS는 상하, 좌우끼리 같은 값을 가질 수 있게 **shorthand**라는 짧은 표현을 사용할 수 있다!

![](https://blog.kakaocdn.net/dn/te3HC/btrI6d9mE5a/E34ieuk1i9YI7KuZi62gLk/img.png)

vscode에서 직접 실행해보고 눈으로 확인해보자!

![](https://blog.kakaocdn.net/dn/znMum/btrI1V3MwDg/kMGfgTXKAqH9FI6rTjx1fK/img.png)

여기서 보라색으로 표현된 부분이 content-box이다. 

과연 우리가 보는 content-box의 크기는 설정한 대로 100px 일까? **NoNo**

![](https://blog.kakaocdn.net/dn/6WpYd/btrI7Lyj7WZ/3yzyxFgnlo3ExDaX1dP7q0/img.png)

개발자 도구로 확인해보면 142px이 나오는걸 볼 수 있다. **Why?**

1.  기본적으로 모든 요소의 box-sizing은 content-box이다.
    -   padding을 제외한 순수 contents 영역만을 box로 지정한다. 즉 보라색 박스 안의 **content-box라는 글자가 하나의 박스로 지정**되어있다.
2.  다만 우리가 생각하는 것은 border까지의 너비, 즉 보라색 네모 자체의 너비를 100px로 보는 것을 원한다.  
    -   이런 경우 box-sizing을 border-box로 설정해주면 된다!

이번 시간엔 HTML의 요소를 구성하고 있는 Box model에 대해 알아보았다.

Box model의 구성 영역 크기를 바꿔주면서 각 내용들을 눈에 잘 들어오게 해 볼 수 있다.

무엇보다 실습을 통해서 직접! 눈으로 보는 것이 HTML/CSS에서는 제일 중요한 것 같다. 

다음 글에서는 **Display와 Position을 통하여 Box를 내가 원하는 곳에 위치**시켜보자!
지난 시간에 네모 박스의 크기 조절 방법을 배웠다면 이번에는 그 박스들의 위치를 지정해줄 것이다.

우선 HTML 시간에 잠깐 지나갔던 **인라인/블록 요소**라는 것이 기억나는가? 괜찮다. 이번에 다시 배우면 된다.

이전 글과 마찬가지로 CSS원칙 2번째를 알아보고 가자!

1.  모든 요소는 네모이고, 좌측 상단에 배치
2.  **Display에 따라 크기와 배치가 달라진다.**

여기 나오는 Display의 대표 종류가 **block**과 **inline**이다!

-   **display: blcok**
    -   줄 바꿈이 일어나는 요소
    -   화면 크기 전체의 가로 폭을 차지한다.
    -   블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음.
    -   대표적인 요소 - div/ ul,ol,li / p / hr / form 등
-   **display: inline**
    -   줄 바꿈이 일어나지 않는 행의 일부 요소
    -   content 너비만큼 가로 폭을 차지한다.
    -   width, height, margin-top, margin-bottom을 지정할 수 없다.
    -   상하 여백은 line-height로 지정한다.
    -   대표 요소 - span / a / img / input, label / b, em, i, strong 등

![](https://blog.kakaocdn.net/dn/nHtVJ/btrIZ6Ydd41/wvNvtx4T0p2IWC3kUKxW7k/img.png)

블록이 가지는 일반적인 너비

![](https://blog.kakaocdn.net/dn/bwb3fq/btrI8SqlgeY/jGnt5hobdCF2DW6bmIInZ1/img.png)

inline이 가지는 일반적인 너비

만약! 블록이 너비를 가질 수 없다면 자동으로 margin이 부여 된다. 대충 inline과 block의 차이를 알아보았다면, 정렬하는 방법에 대해 배워보자.

![](https://blog.kakaocdn.net/dn/kBcG5/btrI2YrT0BF/Pr6YrEEtD65KRyuLBiruYk/img.png)

이 외에도 여러가지가 있지만 2개만 간단히 더 알아보고 넘어가자

-   **display: inline-block**
    -   block과 inline 레벨 요소의 특징을 모두 가짐
    -   inline처럼 한 줄에 표시할 수 있고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
-   **display: none**
    -   해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
    -   이와 비슷한 **visibility: hidden**은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.

위의 4가지 말고도 다양한 디스플레이는 [https://developer.mozilla.org/ko/docs/Web/CSS/display](https://developer.mozilla.org/ko/docs/Web/CSS/display)

 [display - CSS: Cascading Style Sheets | MDN

display CSS 속성은 요소를 블록과 인라인 요소 중 어느 쪽으로 처리할지와 함께, 플로우, 그리드, 플렉스처럼 자식 요소를 배치할 때 사용할 레이아웃을 설정합니다. display 속성은, 형식적으로는

developer.mozilla.org](https://developer.mozilla.org/ko/docs/Web/CSS/display)

![](https://blog.kakaocdn.net/dn/lzoxz/btrI6seILaL/5MkMkkwPEWgnnReU9yRj20/img.png)

직접 코드를 눈으로 보고 어떤 점이 다른지 확인해보자!!

그럼 이제 이 박스들을 화면 어디에 위치시킬지 결정하는 **Position**에 대해 배워보자!

> Position

먼저 간단히 특징과 종류에 대해 알아보자.

-   문서 상에서 요소의 위치를 지정
-   static: 모든 태그의 기본 값(기준 위치)
    -   일반적 요소의 배치 순서에 따름(좌측 상단)
    -   부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
-   아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
    1.  **relative : 상대 위치**
        -   자기 자신의 static 위치를 기준으로 이동 (normal flow 유지) - normal flow란 css원칙대로 움직이는 것!
        -   레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)
    2.  **absolute : 절대 위치**
        -   요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
        -   static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 브라우저 화면 기준으로 이동)
    3.  **fixed : 고정 위치**
        -   요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
        -   부모 요소와 관계없이 viewport를 기준으로 이동 - 스크롤 시에도 항상 같은 곳에 위치
    4.  **sticky: 스크롤에 따라 static -> fixed로 변경**
        -   속성을 적용한 박스는 평소에 문서 안에서 position: static 상태와 같이 일반적인 흐름에 따르지만 스크롤 위치가 임계점에 이르면 position: fixed와 같이 박스를 화면에 고정할 수 있는 속성

글로만 보면 이해가 되지 않을 테니 지금부터 하나씩 쳐보면서 비교해보자!!

![](https://blog.kakaocdn.net/dn/yfTmU/btrIYC389DS/rbqXeSXbie8NFroAkmU2l1/img.png)

static의 경우 부모 요소가 없다면 css 원칙에 따라 좌측 상단에 먼저 생성된다.

![](https://blog.kakaocdn.net/dn/KrvEF/btrI1WBBIrP/aBEW2mWRULk8fkKKglvfnK/img.png)

relative의 경우 기존 위치에 대비하여 움직이지만 실제 위치는 그대로이고 눈에 보이는 위치만 옮겨진다!

![](https://blog.kakaocdn.net/dn/A0Q25/btrI2cRLnFJ/IbsO8YcmK57RFRHCwncgjK/img.png)

absolute의 경우 부모/조상 요소 기준으로 위치하는데 실제 위치가 옮겨진다!

![](https://blog.kakaocdn.net/dn/bt5RTN/btrI6rUqQNH/hOV21m4MuC0TpeSHfnaFyK/img.png)

fixed의 경우 bottom: 0; right:0;에 의해 오른쪽 아래로 붙게 된다.

여기서 궁금한 점! **Relative**와 **Absolute**가 동일하게 움직이는 것 같은데 과연 무슨 차이가 있을까?!

![](https://blog.kakaocdn.net/dn/1BTm3/btrI3trHFNv/g898DkOQkZAaws7CnB26Pk/img.png)

위의 코드를 실행해보고 먼저 생각해보자!

![](https://blog.kakaocdn.net/dn/dvOT8o/btrI6qH010U/ko1hmXJ3oiR9JqXoLCxykk/img.png)

왼쪽이 바로 absolute, 오른쪽이 relative이다. 어떤 차이가 있는지 알겠는가?

-   **relative**의 경우 실제 위치가 그대로 이기 때문에 normal flow에 따라 형의 왼쪽에 동생이 온다.
-   **absolute**는 실제 위치가 옮겨지기 때문에 normal flow에서 벗어나 다시 좌측 상단으로 동생이 오게 된다.

마지막으로 CSS 원칙 3번째를 알아보고 끝내자!!

1.  모든 요소는 네모이고, 좌측 상단에 배치
2.  **Display에 따라 크기와 배치가 달라진다.**
3.  **position으로 위치의 기준을 변경**
    -   relative : 본인 원래 위치
    -   absolut: 특정 부모의 위치
    -   fixed: 화면의 위치
    -   sticky: 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경

이번 시간엔 **Display와 Position을 이용하여 요소를 이동, 변경시키는 방법**을 배웠다!!

다음 시간엔 **float라는 것을 통해 layout 변경**하는 것을 알아보자
> CSS Layout technique 종류

-   Display
-   Position
-   float
-   Flex box
-   Grid
-   기타

---

이전 글들 또는 신문 기사와 같이 이미지를 감싸는 글자들을 많이 보았을 것이다. 또는 이미지가 왼쪽, 오른쪽으로 배치가 되어 있는 것을 보았을 것이다. 이때 사용하는 것이 바로 **Float**이다.

-   박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인요소들이 주변을 wrapping 하도록 함
-   요소가 Normal flow를 벗어나도록 함

![](https://blog.kakaocdn.net/dn/bKnhZ6/btrI1OJNhHE/rKX6sZAkIpff1rvBaiakvK/img.png)

-   속성
    -   none: 기본 값
    -   left: 요소를 왼쪽으로 띄움
    -   right: 요소를 오른쪽으로 띄움

딱히 어려운 것이 없어보이니 float는 이 정도만 이해하고 넘어가자!

---

이제는 **Flex box**라고 하는 조금 더 간편하게 정렬할 수 있는 것을 알아보자.

우선 **Flex box**란 행과 열의 형태로 아이템들을 배치하는 1차원 레이아웃 모델이다

main axis(메인 축), cross axix(교차 축)을 가지고 있으며 Flex container(부모 요소), Flex item(자식 요소)로 구성되어 있다.

아래 그림을 보면 더 이해가 잘될 것이다.

![](https://blog.kakaocdn.net/dn/bntu3S/btrJaW0sNLL/mXJmIRK3s0RBnHs5uRjcN0/img.png)

flex box 구성

-   여기서 **flex-direction은 row**이다.

문득 궁금한게 이전에 배웠던 technique들을 가지고도 충분히 정렬할 수 있는데 왜 flex box를 배우는 걸까?

이전에 배웠던 Normal Flow를 벗어나는 수단은 **'Float** 또는 **Position'**을 이용할 수 있었다.

나만 그런가 모르겠지만 위 2개를 이용했을 때 수동 값 부여 없이 수직정렬, 아이템 간격 동일 배치가 정말 어렵게 느껴졌다. 수동 값으로 맞춰주면 다른 거와 부딪힐 때도 있고 삐뚤삐뚤하고..

이런 어려움을 해결하기 위하여 사용하는 것이 **Flexible Box Layout**!!!

**flex box**를 시작하며 속성들에 대해 그림과 같이 배워보자!

-   부모 요소인 **flex-container**는 **display 속성을 flex 혹은 inline-flex**로 지정해주면 된다.
    
    ```
    .flex-container {
    display: flex
    }
    ```
    
-   배치 설정  
    -   flex-direction 
    -   flex-wrap
-   공간 나누기
    -   justify-content (main-axis)
    -   align-content (cross-axis)
-   정렬
    -   align-items (모든 아이템을 cross axis 기준)
    -   align-self (개별 아이템)

> **Flex-direction과 Flex-warp**

![](https://blog.kakaocdn.net/dn/bPJuf9/btrI7L6e4e1/0MaMzHSyYKXsgbO6aRyvWk/img.png)

![](https://blog.kakaocdn.net/dn/cxibsO/btrI2YyIATr/nYpmt1yKkioxZhtoZSo9kk/img.png)

-   **flex**-**direction**의 경우 **Main** **axis** 기준 방향을 설정
-   **flex**-**warp**은 한 줄에 모든 요소를 다 담을 것인지 결정
-   **flex**-**flow**를 이용하여 **shorthand**로 표현 가능하다.
    -   flex-direction과 flex-wrap에 대한 설정 값을 차례로 작성
    -   ex) flex-flow: row nowrap;

> **justify-content와 align-content**

![](https://blog.kakaocdn.net/dn/BhIF5/btrI2YlbtCr/1eVLAs5AmgyF3t1M4o7HO0/img.png)

justify content

![](https://blog.kakaocdn.net/dn/v6Fnb/btrI3teeuEo/RiDsh8ma7khguna7IowF2k/img.png)

align-content

-   **justify**의 경우는 **main axis**기준, **align**은 **cross axis** 기준이다.
-   **start:** 아이템들을 axis 시작점으로
-   **end:** axis 끝 쪽으로
-   **center:** axis 중앙으로
-   **space-between**: 아이템 사이의 간격을 균일하게 분배
-   **space-around**: 아이템을 둘러싼 영역을 균일하게 분배 (가질 수 있는 영역을 반으로 나눠서 양쪽에)
-   **space-evenly**: 전체 영역에서 아이템 간 간격을 균일하게 분배

> align-items와 align-self

![](https://blog.kakaocdn.net/dn/QPY5g/btrI6qnJkx7/Wqryjjz3Pgh1LWgCk2wPAK/img.png)

items

![](https://blog.kakaocdn.net/dn/8WrgM/btrJaWMXrCH/JecGbugsknXRGJHJExR4H1/img.png)

self

-   **align-items & align-self** 모두 **cross axis**를 **중심**으로 한다
-   **stretch:** 컨테이너를 가득 채움
-   **baseline:** 텍스트 baseline에 기준선을 맞춤

-   기타 속성
    -   **flex-grow:** 남은 영역을 아이템에 분배
    -   **order**: 배치 순서
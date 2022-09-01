![](https://blog.kakaocdn.net/dn/chQjd8/btrI2pP3uTC/bIWkCkt94Ge00JZVgcFeR1/img.png)

> 선택자의 종류에 대해 간단하게 알아보고 뒤에서 상세하게 다뤄보자

1. 기본 선택자

-   전체 선택자, 요소 선택자
-   클래스 선택자, 아이디 선택자, 속성 선택자

2. 결합자(Combinators)

-   자손 결합자, 자식 결합자
-   일반 형제 결합자, 인접 형제 결합자

3. 의사 클래스/요소 (Pseudo Class)

-   링크, 동적 의사 클래스
-   구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

![](https://blog.kakaocdn.net/dn/b0XWBn/btrI4UIVjHp/KwKPnt9lHyFejQw2BRmeZK/img.png)

vscode에서 쳐보며 어떻게 동작하는지 눈으로 확인해보자!

-   **전체 선택자**는 *****을 이용하여 HTML의 모든 텍스트에 적용
-   **요소 선택자**는 **직접 HTML 태그를 선택**하여 그 태그에만 적용
-   **아이디(id) 선택자**는 **#문자**로 시작하며, 해당 아이디가 적용된 항목을 선택하여 적용

> 일반적으로 하나의 문서에 1번만 사용하며, 여러 번 사용보다는 단일 id를 사용하는 것을 권장

그렇다면 전체 선택자로 빨강색의 텍스트를 지정해준 후 요소 선택자로 파랑색의 텍스트를 지정해준다면 어떤 색깔로 출력이 될까?

이런 중복을 회피하기 위하여 친절하게도 **CSS 우선순위(cacading order)**를 만들어 놨다!

**1. 중요도(Importance)** - 사용시 무조건 1순위로 적용되기 때문에 주의해서 사용하자

> !important

**2. 우선 순위 (Specificity)**

> 인라인 > id > class, 속성, pseudo-class > 요소, pseudo element  
>   
> 즉, 좁을 수록 강하다고 생각하면 된다!

**3. CSS 파일 로딩 순서**

이해가 잘 안될 수도 있다. 아래의 코드를 통하여 눈으로 확인해보자!!

![](https://blog.kakaocdn.net/dn/cuBunX/btrI20iw48C/SxYsanXHEwvqYT5bkAoee1/img.png)

> 결합자 (Combinators)

-   자손 결합자 (공백)
    -   selectorA 하위의 모든 selectorB 요소
-   자식 결합자 (>)
    -   selectorA 바로 아래의 selectorB 요소
-   일반 형제 결합자 (~)
    -   selectorA의 형제 요소 중 뒤에 위치하는 selectorB의 요소를 모두 선택
-   인접 형제 결합자 (+)
    -   selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB의 요소를 선택

![](https://blog.kakaocdn.net/dn/dM2BC7/btrI6rmbRRX/AFS8BT6jQws90BPCKBFtvk/img.png)

자손 결합자와 자식 결합자

![](https://blog.kakaocdn.net/dn/kBXCP/btrI2YSDno9/gq1KgJDaQdX1003EGuwqYK/img.png)

일반 형제 결합자

![](https://blog.kakaocdn.net/dn/cFuqy9/btrI7MQ9WzS/uj6pfT1okUzevn8LYsgho0/img.png)

인접 형제 결합자

마지막으로 **상속**에 대해서 알아보자. 여러 언어에서도 쓰이는 개념이지만 쉽게 말하면 한 번의 정의를 통해 아래 요소들에게 능력을 물려주는 것이다.

-   속성(프로퍼티) 중에는 **상속이 되는 것**과 **되지 않는 것**이 있다.
    -   상속 되는 것 - Text 관련 요소 (font, color, text-align), opacity, visibility 등
    -   상속 되지 않는 것 - Box model 관련 요소 (width, height, margin, padding, border 등), position 관련 요소 (posiotion, top/right/left/bottom) 등

![](https://blog.kakaocdn.net/dn/blGChJ/btrI3ysfjd4/rHltkSoQeHwkfCqvRzpDKK/img.png)

이 코드를 실행시켜 본다면 color는 상속이 되어 **테스트**로 나타나지만 border는 상속이 되지 않아 주변에 테두리가 생기지 않는 것을 눈으로 볼 수 있다.
# Bootstrap


### CDN - Content Delivery(Distribution) Network

-   컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템.
-   개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)
-   외부 서버를 활용함으로써 본인 서버의 부하가 적어짐

## $ 기본 원리

#### 1. spacing (Margin and padding)

> {property}{sides}-{size}  
> m t - 3

```
<div class="mt-3 ms-5">bootstrap-spacing</div>
```

-   property
    -   m - for classes that set margin
    -   p - for classes that set padding
-   sides
    -   t - for classes that set **margin-top** or **padding-top**
    -   b - for classes that set **margin-bottom** or **padding-bottom**
    -   s - (start) for classes that set **margin-left** or **padding-left** in **LTR**, **margin-right of padding-right in RTL**
    -   e - (end) for classes that set **margin-right or padding-right in LTR, margin-left or padding-left in RTL**
    -   x - for classes that set **both -left and -right**
    -   y - for classes that set **both -top and -bottom**
    -   blank - for classes that set a **margin or padding on all 4 sides of the element**
-   size
    -   0 -for classes that eliminate the margint or padding by setting it to 0
        -   .mx 0 = 가로(왼, 오) margin이 0
        -   .py 0 = 위 아래 padding이 0
    -   1 -(by default) for classes that set the **margin** or **padding** to $ spacer * .25
        -   m-1 0.25rem 4px
    -   2 -(by default) for classes that set the **margin** or **padding** to $ spacer * .5
    -   3 -(by default) for classes that set the **margin** or **padding** to $ spacer *
    -   4 -(by default) for classes that set the **margin** or **padding** to $ spacer * 1.5
    -   5 -(by default) for classes that set the **margin** or **padding** to $ spacer * 3
    -   auto - for classes that set the margin to auto
        -   수평 중앙 정렬, 가로 가운데 정렬

> 브라우저 의 root 글꼴 크기는 16px

spacing 종합

![](https://k.kakaocdn.net/dn/zmSUW/btrQBKUti7r/Zpbpa2brstl1JUKhg5Pd5k/img.png)

#### 2. Color

![](https://k.kakaocdn.net/dn/bm6nCE/btrQDbYhDbE/f9Es0uUKEWQmZdOLmRgN0K/img.png)

-   이미 CDN에 기본 저장된 색들로서 CSS파일에서 사용 가능
-   새로 다운받아서 사용할 수도 있다. CSS파일에서 변경 가능

## $ Bootstrap 컴포넌트

#### Components

-   Bootstrap의 다양한 UI 요소를 활용할 수 있음
-   아래 Components 탭 및 검색으로 원하는 UI 요소를 찾을 수 있음
-   기본 제공된 Components를 변환해서 활용

1.  Buttons
    -   클릭 했을 때 어떤 동작이 일어나도록 하는 요소

![](https://k.kakaocdn.net/dn/bbfxai/btrQDk1RMTW/abnpgycA4A3LK83ZlKwRvK/img.png)

2. Dropdowns

-   dropdown, dropdown-menu, dropdown-item 클래스를 활용해 옵션 메뉴를 만들 수 있다.

![](https://k.kakaocdn.net/dn/uobNS/btrQDPHb6KQ/PLL80DmQTr3day5snbjJS1/img.png)

3. Forms > Form controls  
     
   - form-control 클래스를 사용해 `<input>` 및 `<form>` 태그를 스타일링할 수 있습니다.

![](https://k.kakaocdn.net/dn/cSqith/btrQEIVd19x/VkNPh9moIAkOipZUSLhdX0/img.png)

4. Navbar

-   navbar 클래스를 활용하면 네비게이션 바를 제작할 수 있습니다.

![](https://k.kakaocdn.net/dn/ciRpOi/btrQDcXcZhc/EEoJyefKzHDIaADgv3HxL0/img.png)

5. Carousel

-   콘텐츠를 순환시키기 위한 슬라이드쇼

![](https://k.kakaocdn.net/dn/cJRjTY/btrQBLeLH2V/UjHeBukYHToK6opBvJEPj0/img.png)

6. Modal

-   사용자와 상호작용 하기 위해서 사용하며, 긴급 상황을 알리는데 주로 사용
-   현재 열려 있는 페이지 위에 또 다른 레이어를 띄움
-   페이지를 이동하면 자연스럽게 사라짐(제거를 하지 않고도 배경 클릭시 사라짐)

![](https://k.kakaocdn.net/dn/bqPVgz/btrQBLy3ytF/QcPCLgQ8HCuFnFgABkFTGk/img.png)

7. Flexbox in Bootstrap

![](https://k.kakaocdn.net/dn/b58KUF/btrQyXmnDP9/3kNWVZfkCS1TUut8QQ62F1/img.png)

8. Card > Grid Card

-   화면이 작아지면 1줄에 표시되는 카드의 개수가 줄어듬

![](https://k.kakaocdn.net/dn/cMj4yC/btrQFZ99xT8/nFYYkmbjqZna6dT1MZkfsk/img.png)

**Responsive Web**

-   같은 컨텐츠를 보는 각기 다른 디바이스

> Responsive Web Design

-   다양한 화면 크기를 가진 디바이스들이 등장함에 따라 responsive web desing 개념이 등장
-   반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어
-   예시(Media Queries, Flexbox, Bootstrap Grid System, The viewport meta tag)

## $ Grid system

-   요소들의 디자인과 배치에 도움을 주는 시스템
-   기본 요소
    -   column : 실제 컨텐츠를 포함하는 부분
    -   Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
    -   Container : Column들을 담고 있는 공간
-   Bootstarp Grid system은 flexbox로 제작됨
-   containter, rows, column으로 컨텐츠를 배치하고 정렬
-   **12개의 column, 6개의 grid breakpoints**

![](https://k.kakaocdn.net/dn/egxxoI/btrQyXfw0s1/L7stbkHMJtOLNzMe2rh4b0/img.png)

**breakpoints**

![](https://k.kakaocdn.net/dn/3W4VZ/btrQDQ0paNJ/STn5z6wzs9thmPkGKkH71k/img.png)

![](https://k.kakaocdn.net/dn/b6fx9C/btrQC7Pfsg0/pbRluRsfleXtYuYr2w1MK1/img.png)

![](https://k.kakaocdn.net/dn/9iJRy/btrQC9fchcs/xZJOAhl6rYBkddFwatcSm1/img.png)

![](https://k.kakaocdn.net/dn/ce8tkQ/btrQDdu5uT4/xgk54kU0FySXkQaGWGKNpk/img.png)

![](https://k.kakaocdn.net/dn/AVpjg/btrQFZ3oPZU/Dd21HjlkV9sbHlpCH5kflk/img.png)

![](https://k.kakaocdn.net/dn/NCz0r/btrQC9fchCz/w1S5s2PCM8kKv98E5WGTt1/img.png)

![](https://k.kakaocdn.net/dn/bHLQUE/btrQEJGAN07/TeIVIbdK83udpq94KpuwN1/img.png)

![](https://k.kakaocdn.net/dn/bgM12r/btrQC8tSyl5/NkmraJ9oQ9Vjv4kklJZExK/img.png)

![](https://k.kakaocdn.net/dn/UALBD/btrQEre1rDr/Uoj8GVVmgW036TakGpk0R0/img.png)

![](https://k.kakaocdn.net/dn/m0ymR/btrQEqArhEO/kdnH05Fl8vWTCI0LsXEqN1/img.png)

![](https://k.kakaocdn.net/dn/cg6Y6l/btrQC7PfwZc/Lpq8tWNxD9Nqx0khoQ6vW1/img.png)

![](https://k.kakaocdn.net/dn/Hmjm2/btrQEIgEy7i/KiEt1qy4BrIZ8WlQjGzKA1/img.png)

![](https://k.kakaocdn.net/dn/P6YQ7/btrQz7Cnctf/OaPfgrGJNjw21EJNLLVqIK/img.png)

**### 부트스트랩 자세한건 공식 문서 참고!!**
# Bootstrap


CDN - Content Delivery(Distribution) Network

-   컨텐츠(CSS, JS, Image, Text 등)을 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템.
-   개별 end-user의 가까운 서버를 통해 빠르게 전달 가능(지리적 이점)
-   외부 서버를 활용함으로써 본인 서버의 부하가 적어짐



## 기본 원리

1. spacing (Margin and padding)

> {property}{sides}-{size}  
> m t - 3

```html
<div class="mt-3 ms-5">bootstrap-spacing</div>
```

-   property
    
    -   m - for classes that set margin
    -   p - for classes that set padding
-   sides
    
    -   t - for classes that set margin-top or padding-top
    -   b - for classes that set margin-bottom or padding-bottom
    -   s - (start) for classes that set margin-left or padding-left in LTR, margin-right of padding-right in RTL
    -   e - (end) for classes that set margin-right or padding-right in LTR, margin-left or padding-left in RTL
    -   x - for classes that set both _-left and_ -right
    -   y - for classes that set both _-top and_ -bottom
    -   blank - for classes that set a margin or padding on all 4 sides of the element
-   size
    
    -   0 -for classes that eliminate the margint or padding by setting it to 0
        -   .mx 0 = 가로(왼, 오) margin이 0
        -   .py 0 = 위 아래 padding이 0
    -   1 -(by default) for classes that set the **margin** or **padding** to $ spacer * .25
        -   > m-1 0.25rem 4px
            
    -   2 -(by default) for classes that set the **margin** or **padding** to $ spacer * .5
    -   3 -(by default) for classes that set the **margin** or **padding** to $ spacer *
    -   4 -(by default) for classes that set the **margin** or **padding** to $ spacer * 1.5
    -   5 -(by default) for classes that set the **margin** or **padding** to $ spacer * 3
    -   auto - for classes that set the margin to auto
        -   수평 중앙 정렬, 가로 가운데 정렬

> 브라우저 의 root 글꼴 크기는 16px

##### 

spacing 종합

![화면 캡처 2022-08-03 171256.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/aacdf548a64e3f68731843e00e918009aac4c3be.png?1661988901875)

#### 

2. Color

![화면 캡처 2022-08-03 171604.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/88b52b6e6e60e79fae8d2f4a06253ebacbea2e7b.png?1661988901875)

-   이미 CDN에 기본 저장된 색들로서 CSS파일에서 사용 가능
-   새로 다운받아서 사용할 수도 있다. CSS파일에서 변경 가능

## 

Bootstrap 컴포넌트

#### 

Components

-   Bootstrap의 다양한 UI 요소를 활용할 수 있음
    
-   아래 Components 탭 및 검색으로 원하는 UI 요소를 찾을 수 있음
    
-   기본 제공된 Components를 변환해서 활용
    

1.  Buttons
    
    -   클릭 했을 때 어떤 동작이 일어나도록 하는 요소
        
        ![화면 캡처 2022-08-03 171950.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/1bb36d4973e7088090c45863fa562cbcea8b4489.png?1661988901813)
        
2.  Dropdowns
    
    -   dropdown, dropdown-menu, dropdown-item 클래스를 활용해 옵션 메뉴를 만들 수 있다.
        
        ![화면 캡처 2022-08-03 172039.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/f2b876ee385a0b17112333ed94a4e63b0f8f07af.png?1661988901906)
        
3.  Forms > Form controls
    
    -   form-control 클래스를 사용해  및
        
        태그를 스타일링할 수 있습니다.
        
        ![화면 캡처 2022-08-03 172132.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/e699511a6736d3e028cf5655ef9f6cd8db9be52c.png?1661988901891)
        
4.  Navbar
    
    -   navbar 클래스를 활용하면 네비게이션 바를 제작할 수 있습니다.
        
        ![화면 캡처 2022-08-03 172210.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/0a7e3fea65124a06e1923d599cb98718a911a3e2.png?1661988901813)
        
5.  Carousel
    
    -   콘텐츠를 순환시키기 위한 슬라이드쇼
        
        ![화면 캡처 2022-08-03 172238.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/ddd39c5821bf837d9ea6125242a81bff088a1972.png?1661988901891)
        
6.  Modal
    
    -   사용자와 상호작용 하기 위해서 사용하며, 긴극ㅂ 상황을 알리는데 주로 사용
        
    -   현재 열려 있는 페이지 위에 또 다른 레이어를 띄움
        
    -   페이지를 이동하면 자연스럽게 사라짐(제거를 하지 않고도 배경 클릭시 사라짐)
        
        ![화면 캡처 2022-08-03 172330.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/bd96fe5fa4831478b6fd5a9433eeb20973ff5811.png?1661988901891)
        
7.  Flexbox in Bootstrap
    
    ![화면 캡처 2022-08-03 172355.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/52d8103f8a9ca949fa1cb5717a2eb2d21f07b00c.png?1661988901844)
    
8.  Card > Grid Card
    
    -   화면이 작아지면 1줄에 표시되는 카드의 개수가 줄어듬
        
        ![화면 캡처 2022-08-03 172552.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/e3812efe9d773b3879b09fb7e6965e1b490de6b0.png?1661988901891)
        

###### 

Responsive Web

-   같은 컨텐츠를 보는 각기 다른 디바이스
    
    > Responsive Web Design
    
-   다양한 화면 크기를 가진 디바이스들이 등장함에 따라 responsive web desing 개념이 등장
    
-   반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어
    
-   예시(Media Queries, Flexbox, Bootstrap Grid System, The viewport meta tag)
    

## 

Grid system

-   요소들의 디자인과 배치에 도움을 주는 시스템
    
-   기본 요소
    
    -   column : 실제 컨텐츠를 포함하는 부분
    -   Gutter : 칼럼과 칼럼 사이의 공간 (사이 간격)
    -   Container : Column들을 담고 있는 공간
-   Bootstarp Grid system은 flexbox로 제작됨
    
-   containter, rows, column으로 컨텐츠를 배치하고 정렬
    
-   **12개의 column, 6개의 grid breakpoints** 1
    
    ![화면 캡처 2022-08-03 173042.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/3e7df16e8987f1beadee81f9a3a6bc57116bc85b.png?1661988901828)
    

##### 

breakpoints

![화면 캡처 2022-08-03 173128.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/62f558ccefb11377961f59d75ccb858dda68d867.png?1661988901860)

![화면 캡처 2022-08-03 173141.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/bf2937ec939e65f1ebe9428c52421cefb11d65e8.png?1661988901891)

![화면 캡처 2022-08-03 173149.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/fd087c58a8b1568446078243ac64be2e309f1bc9.png?1661988901906)

![화면 캡처 2022-08-03 173159.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/0a71259a53bdc01684760fefa2724082e2d230ce.png?1661988901797)

![화면 캡처 2022-08-03 173219.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/9b66b54478c7c88f7510bc754d7724be698c06a2.png?1661988901875)

![화면 캡처 2022-08-03 173229.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/d2a2708d90abba54381c6851e07d7b7b3c4b24af.png?1661988901891)

![화면 캡처 2022-08-03 173246.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/129ffe9d46bc2552b7960cbfce24d86449b58e09.png?1661988901813)

![화면 캡처 2022-08-03 173400.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/73f1b0d2259f4f46b1c05f185947adf64680a7aa.png?1661988901860)

![화면 캡처 2022-08-03 173410.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/4e1520744d347156409b912de60f48baeb37d607.png?1661988901828)

![화면 캡처 2022-08-03 173419.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/40f1503365044e5b0a978abe7cc43cb709c8ff7a.png?1661988901828)

![화면 캡처 2022-08-03 173429.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/a5f26dde9813dd0527676e5973f26834773b799c.png?1661988901875)

![화면 캡처 2022-08-03 173437.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/1a90e33695aba324429f7c21bac5e6ddd08cfc09.png?1661988901813)

![화면 캡처 2022-08-03 173446.png](app://local/C:/Users/SSAFY/Desktop/TIL/study/web_class_assets/8d1de6560db9085ca99c79f0e6b163d9e693992f.png?1661988901875)
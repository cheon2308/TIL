Article과 User의 M:N 관계 설정을 통한 좋아요 기능을 구현해보자

#### **목차**

1.  LIKE - 모델 관계 설정
2.  LIKE 구현

---

### **1. LIKE**

> **모델 관계 설정**

-   ManyToManyField 작성

![](https://blog.kakaocdn.net/dn/oqsNU/btrOrTdPtNb/yDsTxgSfBKEPTj1WlV8MM1/img.png)

-   migration 진행 후 에러 확인

![](https://blog.kakaocdn.net/dn/mZ2My/btrOs4eRA6Q/UxxCSNaq8u1JHoqkKXs8Ok/img.png)

-   like_users 필드 생성 시 자동으로 역참조에는 **.article_set** 매니저가 생성됨
-   그러나 이전 N:1(Article-User) 관계에서 이미 해당 매니저를 사용중
    1.  **user.article_set.all()** -> 해당 유저가 작성한 모든 게시글 조회
    2.  **user가 작성한 글들(user.article_set)**과 **user가 좋아요를 누른 글(user.article_set)**을 구분할 수 없게 됨
-   user와 관계된 ForeignKey 혹은 ManyToManyField 중 하나에 related_name을 작성해야 함
-   ManyToManyField에 related_name 작성 후 Migration

![](https://blog.kakaocdn.net/dn/ILKfb/btrOsaGpc5v/CKAI2uleJZava9K2TLv96k/img.png)

![](https://blog.kakaocdn.net/dn/cCAEYe/btrOtHX1gEg/KGFTniG3ZwRK0FqqLk1d3K/img.png)

-   User - Article간 사용 가능한 related manager 정리
    1.  **article.user**  
        -   게시글을 작성한 유저 - N:1
    2.  **user.article_set**  
        -   유저가 작성한 게시글(역참조) - N:1
    3.  **article.like_users**
        -   게시글을 좋아요한 유저 - M:N
    4.  **user.like_articles**  
        -   유저가 좋아요한 게시글(역참조) - M:N

---

### **2. LIKE 구현**

-   url 및 view 함수 작성

![](https://blog.kakaocdn.net/dn/b5sGyH/btrOrfnSFa7/KBNccAglCk9t4eAwMK1cq1/img.png)

> **.exists()**

-   QuerySet에 결과가 포함되어 있으면 True를 반환하고 그렇지 않으면 False를 반환
-   특히 큰 QuerySet에 있는 특정 개체의 존재와 관련된 검색에 유용

-   index 템플릿에서 각 게시글에 좋아요 버튼 출력하기

![](https://blog.kakaocdn.net/dn/dKCZb0/btrOreifUGq/TrneoTDgZlsAtZHRqN29h0/img.png)

-   데코레이터 및 is_authenticated 추가

![](https://blog.kakaocdn.net/dn/bhgULX/btrOpS8ledD/IAlqI8TXutr63uRikw6Ce0/img.png)
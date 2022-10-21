Comment(N) 모델과 User(1) 모델 간 관계 설정을 해보자!

"0개 이상의 댓글은 1개의 회원에 의해 작성될 수 있음"

#### **목차**

1.  모델 관계 설정
2.  CREATE
3.  READ
4.  DELETE
5.  인증된 사용자에 대한 접근 제한하기

---

### **1. 모델 관계 설정**

> **Comment와 User간 모델 관계 설정**

![](https://blog.kakaocdn.net/dn/Lzd3Z/btrOrR04dm5/8vedvIUCeHydxra45g7Xyk/img.png)

-   Comment 모델에 User 모델을 참조하는 외래 키 작성

![](https://blog.kakaocdn.net/dn/8vIsu/btrOq2WiBG6/04Kl69hfwKPCaceNqLASa1/img.png)

-   앞에서 USER - ARTICLE 모델 관계 설정 때와 마찬가지로 기존에 존재하던 테이블에 새로운 컬럼이 추가되어야 하는 상황이기 때문에 migrations 파일이 곧바로 만들어지지 않고 일련의 과정 필요

![](https://blog.kakaocdn.net/dn/cxv53H/btrOrRNztn5/uIwJGZVBHdnkuM4AnHz5Q0/img.png)

-   첫 번째 화면
    -   기본적으로 모든 컬럼은 NOT NULL 제약조건이 있기 때문에 데이터가 없이는 새로 추가되는 외래 키 필드 user_id가 생성되지 않음
    -   그래서 기본 값을 어떻게 작성할 것인지 선택해야 함
    -   1을 입력하고 Enter 진행 (다음 화면에서 직접 기본 값 입력)

![](https://blog.kakaocdn.net/dn/GLdWG/btrOpR2nevM/Raw45FNu8LUkgQ6u9Awuo0/img.png)

-   두 번째 화면
    -   comment의 user_id에 어떤 데이터를 넣을 것인지 직접 입력해야 함
    -   마찬가지로 1 입력하고 Enter 진행
    -   그러면 기존에 작성된 댓글이 있다면 모두 1번 회원이 작성한 것으로 처리됨
-   이후 migrate 진행하고 테이블 스키마 변경 및 확인

![](https://blog.kakaocdn.net/dn/ngjbO/btrOqUxfBGt/E0JOOFBIKFBkvgVnFXkhCK/img.png)

---

### **2. CREATE**

-   인증된 회원의 댓글 작성 구현하기
-   작성하기 전 로그인을 먼저 진행한 상태로 진행

> **CommentForm**

![](https://blog.kakaocdn.net/dn/w6iy4/btrOnLauxZW/bEvqjvDRx0Kk8AClIWnwkk/img.png)

-   이전에서도 보았듯이 CommentForm 출력을 확인해보면 create 템플릿에서 불필요한 필드(user)가 출력됨
-   user 필드에 작성해야 하는 user 객체는 view 함수의 request 객체를 활용해야 함

![](https://blog.kakaocdn.net/dn/b3D0Mq/btrOqEIrHsS/sbS1TdMmvEgJEltaPgDp0K/img.png)

> **외래 키 데이터 누락**

-   댓글 작성 시 NOT NULL constraint failed: articles_comment.user_id 에러 발생

![](https://blog.kakaocdn.net/dn/csRfFO/btrOpSfVoap/jcMxuZH4ilhjYOlkHec931/img.png)

-   "NOT NULL 제약 조건이 실패했다. articles_comment 테이블의 user_id 컬럼에서"
-   댓글 작성 시 외래 키에 저장되어야 할 작성자 정보가 누락되었기 때문

-   댓글 작성 시 작성자 정보가 함께 저장될 수 있도록 save의 commit 옵션을 활용

![](https://blog.kakaocdn.net/dn/vo84o/btrOrSTfBqY/7qHtqn4fKwFfPhi4xsXO3k/img.png)

---

### **3. READ**

> **댓글 작성자 출력  
> **

-   detail 템플릿에서 각 게시글의 작성자 출력

![](https://blog.kakaocdn.net/dn/kwF8V/btrOqjket5T/KT8AmMIuh2kpUtXBgOrxy1/img.png)

---

### **4. DELETE**

> **댓글 삭제 시 작성자 확인**

-   이제 댓글에는 작성자 정보가 함께 들어있기 때문에 현재 삭제를 요청하려는 사람과 댓글을 작성한 사람을 비교하여 본인의 댓글만 삭제할 수 있도록 함

![](https://blog.kakaocdn.net/dn/cjAe6Y/btrOrdcg7gT/3WBesJJwTMDc4bsTG96f1K/img.png)

-   추가로 해당 댓글의 작성자가 아니라면, 삭제 버튼을 출력하지 않도록 함

![](https://blog.kakaocdn.net/dn/Yhy4I/btrOo6S052M/NQFqaFJ2dKQPvbTgxu6QAK/img.png)

---

### **5. 인증된 사용자에 대한 접근 제한하기**

-   is_authenticated와 View decorator를 활용하여 코드 정리하기

> **인증된 사용자인 경우만 댓글 작성 및 삭제하기**

![](https://blog.kakaocdn.net/dn/boA1uO/btrOo6leDcG/c9yHF2ud50k40Gwjz8ECsK/img.png)

![](https://blog.kakaocdn.net/dn/ckANo8/btrOq1JVGpk/7yTZt3Dg7Fat26FTBTcv3k/img.png)

> **비인증 사용자는 CommentForm을 볼 수 없도록 하기**

![](https://blog.kakaocdn.net/dn/bjxBK9/btrOqFm3EBK/0qTBQXFNEPB7GxcWm0Rafk/img.png)
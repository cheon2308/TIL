### ### Comment-Article

1:N 관계의 모델을 Django를 통해 실습을 해보며 이해해보자!

#### **목차**

1.  Django Relationship fields 종류
2.  Comment Model
3.  관계 모델 참조
4.  Comment 구현
5.  Comment 추가사항

---

### **1. Django Relationship fields 종류**

1.  OneToOneField()
    -   A one-to-one relationship
2.  ForeignKey()
    -   A many-to-one relationship
3.  ManyToManyField()
    -   A many-to-many relationship

OneToOneField()에 대해서는 저번에 알아보았고, ManyToManyField()에 대해서는 다음에 알아보자.

이번엔 ForignKey()에 대해 알아보고 댓글 기능으로 넘어갈 것!

> **ForeignKey(to, on_delete, **options)**

-   A many-to-one relationship을 담당하는 Django의 모델 필드 클래스
-   Django 모델에서 관계형 데이터베이스의 **외래 키 속성**을 담당
-   2개의 필수 위치 인자가 필요
    1.  참조하는 **model class**
    2.  **on_delete** 옵션
-   https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey

---

### **2. Comment Model**

> **정의**

![](https://blog.kakaocdn.net/dn/bn0NFE/btrOozUNKq0/WBT2UnzYXMDFgIOppKyoi1/img.png)

-   외래 키 필드는 ForeignKey 클래스를 작성하는 위치와 관계없이 **필드의 마지막**에 작성됨
-   ForeignKey() 클래스의 인스턴스 이름은 참조하는 모델 클래스 이름의 단수형(소문자)으로 작성하는 것을 권장 (이유는 이어지는 모델 참조에서 확인 예정)

> **ForeignKey arguments - on_delete** 

-   외래 키가 참조하는 객체가 사라졌을 때, 외래 키를 가진 객체를 어떻게 처리할지를 정의
-   **데이터 무결성**을 위해서 매우 중요한 설정
-   on_delete 옵션 값
    1.  **CASCADE** : 부모 객체(참조된 객체)가 삭제됐을 때 이를 참조하는 객체도 삭제
    2.  PROTECT, SET_NULL, SET_DEFAULT... 등 여러 옵션 값들이 존재

**※ 참고 - 데이터 무결성 (Data Integrity)**

-   데이터의 정확성과 일관성을 유지하고 보증하는 것
-   데이터베이스나 RDBMS의 중요한 기능
-   무결성 제한의 유형
    1.  개체 무결성 (Entity integrity)
    2.  참조 무결성 (Referential integrity)
    3.  범위 무결성 (Domain integrity)

**※ 중요**

-   models.py에서 모델에 대한 수정사항이 발생했기 때문에 migration 과정 진행해주어야 한다.
-   migrate 후 Comment 모델 클래스로 인해 생성된 테이블 확인

![](https://blog.kakaocdn.net/dn/IEFxA/btrOqLAayWi/iovMaJ9I0to1UWYvfL9bu1/img.png)

-   ForeignKey 모델 필드로 인해 작성된 컬럼의 이름이 **article_id**인 것을 확인
-   만약 ForeignKey 인스턴스를 article이 아닌 abcd로 생성했다면 abcd_id로 만들어짐
    -   이처럼 명시적인 모델 관계 파악을 위해 참조하는 클래스 이름의 소문자(단수형)로 작성하는 것이 권장되었던 이유

---

### **3. 관계 모델 참조**

> **Related manager**

-   Related manager는 N:1 혹은 M:N 관계에서 사용 가능한 문맥(context)
-   Django는 모델 간 N:1 혹은 M:N 관계가 설정되면 **역참조 할** 때에 사용할 수 있는 manager를 생성
    -   우리가 이전에 모델 생성 시 **objects**라는 매니저를 통해 queryset api를 사용했던 것처럼 related manager를 통해 queryset api를 사용할 수 있게 됨
-   https://docs.djangoproject.com/en/3.2/ref/models/relations/

> **역참조**

-   나를 참조하는 테이블(나를 외래 키로 지정한)을 참조하는 것
-   즉, 본인을 외래 키로 참조 중인 다른 테이블에 접근하는 것
-   N:1 관계에서는 1이 N을 참조하는 상황
    -   즉, 외래 키를 가지지 않은 1이 외래 키를 가진 N을 참조

> **article.comment_set.method()**

-   Article 모델이 Comment 모델을 참조(역참조) 할 때 사용하는 매니저
-   **article.comment** 형식으로는 댓글 객체를 참조할 수 없음
    -   실제로 Article 클래스에는 Comment와의 어떠한 관계도 작성되어 있지 않음
-   대신 Django가 역참조 할 수 있는 **comment_set** manager를 자동으로 생성해 **article.comment_set** 형태로 댓글 객체를 참조할 수 있음
    -   N:1 관계에서 생성되는 Related manager의 이름은 참조하는 "모델명_set" 이름 규칙으로 만들어짐
-   반면 참조 상황(Comment -> Article)에서는 실제 ForeignKey 클래스로 작성한 인스턴스가 Comment 클래스의 클래스 변수이기 때문에 comment.article 형태로 작성 가능

> **ForeignKey arguments - related_name**

![](https://blog.kakaocdn.net/dn/AUfM0/btrOqA6KKjE/F2iJDcYwMyM0xbOqzLgik1/img.png)

-   ForeignKey 클래스의 선택 옵션
-   역참조 시 사용하는 매니저 이름(model_set manager)을 변경할 수 있음
-   작성 후, migration 과정이 필요
-   선택 옵션이지만 상황에 따라 반드시 작성해야 하는 경우가 생기기도 하는데 이는 추후 자연스럽게 만나볼 예정
-   작성 후 다시 원래 코드로 복구
    -   위와 같이 변경하면 기존 article.comment_set은 더 이상 사용할 수 없고, **article.comments로 대체**됨

> **admin site 등록**

-   새로 작성한 Comment 모델을 admin site에 등록하기

![](https://blog.kakaocdn.net/dn/v4bml/btrOnrW157z/VYPvfcYCQU6aCs1LjokrJk/img.png)

---

### **4. Comment 구현**

> **Create**

-   사용자로부터 댓글 데이터를 입력받기 위한 CommentForm 작성

![](https://blog.kakaocdn.net/dn/cgyQbO/btrOq3tPcNu/qeRdfKUCHeKtFsTKgumD30/img.png)

-   detail 페이지에서 CommentForm 출력 (view 함수)
    -   기존에 ArticleForm 클래스의 인스턴스명을 form으로 작성했기 때문에 헷갈리지 않도록 comment_form으로 작성

![](https://blog.kakaocdn.net/dn/bDbvym/btrOqKBkF4A/FApQNeHs5wt0qL4EfbpayK/img.png)

-   detail.html에서 CommentForm 출력 (템플릿)

![](https://blog.kakaocdn.net/dn/cXZUzR/btrOoyVWbl7/R6MvDRPBHhbk9ajpZZR2yk/img.png)

-   detail 페이지에 출력된 CommentForm을 살펴보면 다음과 같이 출력됨
-   실 서비스에서는 댓글 작성 시 어떤 게시글에 작성하는지 직접 게시글 번호를 선택하지 않음
-   다음과 같이 출력되는 이유는 Comment 클래스의 **외래 키 필드 article 또한 데이터 입력이 필요**하기 때문에 출력되고 있는 것
-   하지만, 외래 키 필드는 **사용자의 입력으로 받는 것이 아니라 view함수 내에서 받아 별도로 처리되어 저장**되어야 함

![](https://blog.kakaocdn.net/dn/drbOPQ/btrOrcKSLw2/luzekY1FKdTyHGfoncw9hK/img.png)

-   외래 키 필드를 출력에서 제외해주기

![](https://blog.kakaocdn.net/dn/cV7ENc/btrOreWcnsL/iLcw1Hsc4AXRs53VhfsEy0/img.png)

-   detail 페이지의 url을 살펴보면 <int:pk>처럼 url에 해당 게시글의 pk 값이 사용되고 있음
-   댓글의 외래 키 데이터에 필요한 정보가 바로 게시글의 pk 값
-   이전에 학습했던 url을 통해 변수를 넘기는 **variable routing**을 사용하여 출력에서 제외된 외래 키 데이터를 받아 올 수 있다.

![](https://blog.kakaocdn.net/dn/bHtn3e/btrOrQgv0Re/xVYZK4syYnCklzr5drEpM0/img.png)

![](https://blog.kakaocdn.net/dn/cRcVxE/btrOqKuzpkK/NKmjnc7HMcspzwWAI5jAM0/img.png)

![](https://blog.kakaocdn.net/dn/4QqGq/btrOqBdBvIy/Yt0n8QauaCJhnqPV3mvKC0/img.png)

-   작성을 다하고 보면 article 객체 저장이 이루어질 타이밍이 보이지 않는다.
-   그래서 **save() 메서드**는 데이터베이스에 저장하기 전에 객체에 대한 추가적인 작업을 진행할 수 있도록 인스턴스만을 반환해주는 옵션 값을 제공
-   save 메서드의 commit 옵션을 사용해 DB에 저장되기 전 article 객체 저장하기

![](https://blog.kakaocdn.net/dn/cSGhKs/btrOrehFDVb/8JRRtDDNQDjWgvytR5tr00/img.png)

**#**  **The save() method**

-   **save(commit=False)**  
    -   "Create, but don't save the new instance."
    -   아직 데이터베이스에 저장되지 않은 인스턴스를 반환
    -   저장하기 전에 객체에 대한 사용자 지정 처리를 수행할 때 유용하게 사용
-   [https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/#the-save-method)

> **READ**

-   작성한 댓글 목록 출력하기
-   특정 article에 있는 모든 댓글을 가져온 후 context에 추가

![](https://blog.kakaocdn.net/dn/ccAXg8/btrOqMMItY0/P65RUolIBzwoccvBHxLbok/img.png)

-   detail 템플릿에서 댓글 목록 출력하기

![](https://blog.kakaocdn.net/dn/cPyUID/btrOq2BND8n/UqlZKTvNUTSzPbGFbIAyyK/img.png)

> **Delete**

-   댓글 삭제 구현하기 (url, view)

![](https://blog.kakaocdn.net/dn/CDgXo/btrOo66g9DG/PewexlqVdljEku06rBADF0/img.png)

![](https://blog.kakaocdn.net/dn/bhIPcC/btrOmVYAvgP/s4jAhwnBSjvm0rpGMYauO0/img.png)

-   댓글을 삭제할 수 있는 버튼을 각각의 댓글 옆에 출력될 수 있도록 함

![](https://blog.kakaocdn.net/dn/bPl01Z/btrOnc0eJPp/gEKScJskWO8TP6qgCWeiak/img.png)

**※ 댓글 수정 지금 구현하지 않는 이유**

-   일반적으로 수정 페이지 이동 없이 현재 페이지가 유지된 상태로 수정한다.
-   따라서 JavaScript의 영역이기 때문에 JavaScript를 학습한 후 별도로 진행

---

### **5. Comment 추가 사항**

1.  댓글 개수 출력하기
    1.  DTL filter - **length** 사용
    2.  Queryset API - **count()** 사용
2.  댓글이 없는 경우 대체 콘텐츠 출력하기

![](https://blog.kakaocdn.net/dn/blrQPr/btrOpTMu1BS/2KfkiKTuRXj2USVV9LhhrK/img.png)

![](https://blog.kakaocdn.net/dn/bU8f9y/btrOqU4WDAZ/2AaTt8JwGca1Tts2WSfkPk/img.png)

-   detail 템플릿에 작성하기

![](https://blog.kakaocdn.net/dn/P174C/btrOo6ZwALA/AnTJky7I25TbgVrgfkcnMk/img.png)

-   댓글이 없는 경우 대체 컨텐츠 출력하기
-   DTL **for empty** 활용

![](https://blog.kakaocdn.net/dn/whpIk/btrOmWb99NE/6kOt6xJXW1CKCLijGJsYC1/img.png)
#### **목차**

1.  사전 준비
2.  ModelSerializer
3.  Build RESTful API - Article

---

### **1. 사전 준비**

-   Postman 설치
    -   https://www.postman.com/downloads/
-   Postman
    -   API를 구축하고 사용하기 위한 플랫폼
    -   API를 빠르게 만들 수 있는 여러 도구 및 기능을 제공

![](https://blog.kakaocdn.net/dn/sTD61/btrO9PIrud7/xJXTifFkASJaaRBFIGY1w1/img.png)

-   DRF 설치, 등록 및 패키지 목록 업데이트

```
pip install djangorestframework
pip freeze > requirements.txt
```

---

### **2. ModelSerializer**

> **ModelSerializer 작성**

-   articles/serializers.py 생성
    -   serializers.py의 위치나 파일명은 자유롭게 작성 가능
-   ModelSeiralizer 작성

![](https://blog.kakaocdn.net/dn/cO7ZQe/btrO9Bjr3Xd/lqPkoOyjqH9PkC21hGyrL0/img.png)

-   ModelSerializer 클래스는 모델 필드에 해당하는 필드가 있는 Serializer 클래스를 자동으로 만들 수 있는 shortcut을 제공
    1.  Model 정보에 맞춰 자동으로 필드를 생성
    2.  serializer에 대한 유효성 검사기를 자동으로 생성
    3.  **.create()** 및 **.update()**의 간단한 기본 구현이 포함됨

> **ModelSerializer의 'many' option**

-   단일 객체 인스턴스 대신 QuerySet 또는 객체 목록을 serialize 하려면 many=True를 작성해야 함

![](https://blog.kakaocdn.net/dn/EaVUX/btrOGnAmXPr/lGNVD4cqVo87HLnxT17y70/img.png)

---

### **3. Build RESTful API - Article**

> **URL과 HTTP requests methods 설계**

![](https://blog.kakaocdn.net/dn/6Qpl0/btrO92m58YS/BfgHkiDiRcuj8juns53FZ1/img.png)

> **GET - List**

-   게시글 데이터 목록 조회하기
-   DRF에서 **api_view 데코레이터** 작성은 필수

![](https://blog.kakaocdn.net/dn/bffFN1/btrO78PHDoD/RuowWWMCPSGtWdKcUs4cKk/img.png)

![](https://blog.kakaocdn.net/dn/casjRA/btrO90bYSNo/fgbT3wixP1BcD7koJz8Kt0/img.png)

![](https://blog.kakaocdn.net/dn/ek6Qga/btrPaJgyacc/XoPrsGqbYx5w0E08Z8VxTK/img.png)

> **'api_view' decorator**

-   DRF view 함수가 응답해야 하는 HTTP 메서드 목록을 받음
-   기본적으로 **GET 메서드만 허용**되며 다른 메서드 요청에 대해서는 **405 Method Not Allowed**로 응답

> **GET - detail**

-   단일 게시글 데이터 조회하기
-   각 데이터의 상세 정보를 제공하는 ArticleSerializer 정의

![](https://blog.kakaocdn.net/dn/cMSh7h/btrO9zzcT7r/pZGJKcV8gAfEi0o7CZJwOK/img.png)

-   url 및 view 함수 작성

![](https://blog.kakaocdn.net/dn/cEOiSD/btrO9BcJzEx/a9phcHmcU1kufYKQBwnzB0/img.png)

> **POST**

-   게시글 데이터 생성하기
-   요청에 대한 데이터 생성이 성공했을 경우는 201 Created 상태 코드를 응답하고 실패했을 경우는 400 Bad request를 응답 
-   요청에 대한 데이터 생성이 성공했을 경우는 201 Created 상태 코드를 응답하고 실패 했을 경우는 400 Bad request를 응답

![](https://blog.kakaocdn.net/dn/baQPqD/btrOQnz0KfG/F4ghb8T7S0Rr0dujjtaaJ0/img.png)

> **Raising an exception on invalid data**

-   "유효하지 않은 데이터에 대해 예외 발생시키기"
-   is_valid()는 유효성 검사 오류가 있는 경우 ValidationError 예외를 발생시키는 선택적 raise_exception 인자를 사용할 수 있음
-   DRF에서 제공하는 기본 예외 처리기에 의해 자동으로 처리되며 기본적으로 HTTP 400 응답을 반환

![](https://blog.kakaocdn.net/dn/bPwoHe/btrO9Z5gC9k/HOdnqxJBtgjm7p60eAkji1/img.png)

> **DELETE**

-   게시글 데이터 삭제하기
-   요청에 대한 데이터 삭제가 성공했을 경우는 **204 No Content** 상태 코드 응답
-   명령을 수행했고 더 이상 제공할 정보가 없는 경우

![](https://blog.kakaocdn.net/dn/pv3Za/btrO79nygOo/FazxsuDupwovJR162esZkk/img.png)

> **PUT**

-   게시글 데이터 수정하기
-   요청에 대한 데이터 수정이 성공했을 경우는 **200 OK** 상태 코드 응답

![](https://blog.kakaocdn.net/dn/bisIiG/btrO6gGuW25/2rf8WwSJo8ywjBaW0CsCg0/img.png)
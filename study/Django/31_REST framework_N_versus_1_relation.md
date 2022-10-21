#### **목차**

1.  사전 준비
2.  N:1 - 역참조 데이터 조회
3.  Django shortcuts functions

---

### **1. 사전 준비**

-   Comment 모델 작성 및 데이터베이스 초기화
-   이후 Migration 진행

![](https://blog.kakaocdn.net/dn/b9Ccum/btrO774mvoE/lX4KfGKyAz3kYn1svKHvwK/img.png)

> **GET - List**

-   댓글 데이터 목록 조회하기
-   Article List와 비교하며 작성해보기

![](https://blog.kakaocdn.net/dn/bn0nNB/btrPaHpDSkK/RZpl7xSHnAK7Wkk8kDozLK/img.png)

![](https://blog.kakaocdn.net/dn/xIHoI/btrOGpkElxi/tT9wHKga5jVw6loq9e7Yo0/img.png)

> **GET - Detail**

-   단일 댓글 데이터 조회하기
-   Article과 달리 같은 serializer 사용하기

![](https://blog.kakaocdn.net/dn/Kpc0h/btrO50kpR90/S6gMsT6XK1W0wnIwkfqzI0/img.png)

> **POST**

![](https://blog.kakaocdn.net/dn/duAQfx/btrPaHiUv4x/UgiGUK6IGHNCBoPPG21HZk/img.png)

> **Passing Additional attirbutes to .save()**

-   **.save()** 메서드는 특정 Serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있음
-   **CommentSerializer**를 통해 Serialize되는 과정에서 Parameter로 넘어온 **article_pk**에 해당하는 article 객체를 추가적인 데이터를 넘겨 저장

![](https://blog.kakaocdn.net/dn/ewmHka/btrO9PPveRi/76T2HgHJpCBY3klrePjoJ0/img.png)

-   POST 응답 확인
-   에러가 발생
    -   CommentSerializer에서 article field 데이터 또한 사용자로부터 입력 받도록 설정되어 있기 때문

![](https://blog.kakaocdn.net/dn/coQ2OV/btrOQtG7SGj/Zjhz7SJza2N202P0V0h61k/img.png)

> **읽기 전용 필드 설정**

-   **read_only_fields**를 사용해 외래 키 필드를 **'읽기 전용 필드'**로 설정
-   읽기 전용 필드는 데이터를 전송하는 시점에 '**해당 필드를 유효성 검사에서 제외시키고 데이터 조회 시에는 출력'**하도록 함

![](https://blog.kakaocdn.net/dn/bKHNyP/btrO93M9xEx/Xt3ga39rHRs3woMsX4KDfK/img.png)

> **DELETE & PUT**

-   댓글 데이터 삭제 및 수정 구현하기

![](https://blog.kakaocdn.net/dn/TWOZS/btrO5eWyeW6/P5mkMhwXoo3srLStXHUvck/img.png)

---

### **2. N:1 - 역참조 데이터 조회**

> **특정 게시글에 작성된 댓글 목록 출력하기**

-   기존 필드 **override** - Article Detail
    -   "게시글 조회 시 해당 게시글의 댓글 목록까지 함께 출력하기"
    -   Serializer는 기존  필드를 override 하거나 추가적인 필드를 구성할 수 있음
-   **PrimaryKeyRelatedField()**

![](https://blog.kakaocdn.net/dn/bh0Kip/btrOQxQjxcY/ZBw8pAwlV7iudWu8CIRV31/img.png)

-   modles.py에서 **related_name**을 통해 이름 변경 가능
-   역참조 시 생성되는 **comment_set**을 override 할 수 있음

![](https://blog.kakaocdn.net/dn/ZymaL/btrO9PB0gUZ/XjZ4lE5V7kDs5aSjNaDwt1/img.png)

-   **Nested relationships**

![](https://blog.kakaocdn.net/dn/btYmv2/btrPaLMhzJS/MWFPwi9sT15mGj4A3jYXg0/img.png)

-   모델 관계 상으로 참조 된 대상은 참조하는 대상의 표현에 포함되거나 중첩(nested) 될 수 있음
-   이러한 중첩된 관계를 serializers를 필드로 사용하여 표현 할 수 있음
-   두 클래스의 상/하 위치를 변경해야 함

> **특정 게시글에 작성된 댓글의 개수 출력하기**

-   새로운 필드 추가 - Article Detail
    -   게시글 조회 시 해당 게시글의 댓글 개수까지 함께 출력하기

![](https://blog.kakaocdn.net/dn/r0SF7/btrO90DlkSd/VIQSr6cSBons78fMcUUTIk/img.png)

-   **source**
    -   serializers field's argument
    -   필드를 채우는 데 사용할 속성의 이름
    -   점 표기법(dotted notation)을 사용하여 속성을 탐색 할 수 있음

**※ [주의] 읽기 전용 필드 지정 이슈**

-   특정 필드를 override 혹은 추가한 경우 **read_only_fields**가 동작하지 않으니 주의

![](https://blog.kakaocdn.net/dn/cSMpY1/btrO92U4drh/tvZf8TkF1gBKHHI3GZFVgK/img.png)

---

### **3. Django shortcuts functions**

> **get_object_or_404()**

-   모델 manager objects에서 **get()을 호출**하지만, 해당 객체가 없을 땐 기존 DoesNotExist 예외 대신 Http404를 raise 함

![](https://blog.kakaocdn.net/dn/u3yyj/btrOQCRB33x/I9CNwxXMNGpnbEkSMTKzF0/img.png)

> **get_list_or_404()**

-   모델 manager objects에서 **filter()의 결과를 반환**하고 해당 객체 목록이 없을 땐 Http404를 raise함

![](https://blog.kakaocdn.net/dn/ejBpD5/btrO9PIPdP8/MaKIm5UKo94UZAOSybqla1/img.png)

**※ 사용 이유**

-   클라이언트 입장에서 "서버에 오류가 발생하여 요청을 수행할 수 없다(500)"라는 원인이 정확하지 않은 에러를 마주하기 보다는, 서버가 적절한 예외 처리를 하고 클라이언트에게 올바른 에러를 전달하는 것 또한 중요한 요소
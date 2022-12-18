### **1. 데코레이터(Decorator)**

view 함수를 작성했다면 이번에는 **View decorator**라는 것을 이용하여 단단하게 만들어주자.

-   기존에 작성된 함수에 기능을 추가하고 싶을 때, 해당 함수를 **수정하지 않고 기능을 추가**해주는 함수
-   Django는 다양한 HTTP 기능을 지원하기 위하여 view 함수에 적용할 수 있는 여러 데코레이터를 제공한다.

![](https://blog.kakaocdn.net/dn/m7kJc/btrLwBmZhZw/KYk7DEYkN4gjqEbAdcrjo0/img.png)

예시

위 코드에서 보이듯이 내부 수정이 아닌 `**@hello`**을 통하여 기능 추가를 해준 것을 출력을 통해 확인할 수 있다.


---

### **2. Allowed HTTP methods**

-   **django.views.decorators.http**의 데코레이터를 사용하여 **요청 메서드를 기반으로 접근을 제한할 수 있음**
-   일치하지 않는 메서드 요청이라면 **405 Method Not Allowed를 반환**
-   **405 Method Not Allowed :** 요청 방법이 서버에게 전달 되었으나 사용 불가능한 상태

```PYTHON
# 모듈이므로 사용하기 위하여
from django.views.decorators.http import 'decorator name'
```

> **require_http_methods()**

-   View 함수가 특정한 요청 method만 허용하도록 하는 데코레이터

![](https://blog.kakaocdn.net/dn/c9RvKa/btrLzFot9Ng/RhTWxCB6kxBAH7vASXcHGk/img.png)

허용된 GET, POST가 아닌 경우 거절당한다!

> **require_POST()**

-   View 함수가 **POST 요청 method만 허용**하도록 하는 데코레이터

![](https://blog.kakaocdn.net/dn/152Xg/btrLx2Y1PQZ/fxTk8aLKjV3m7srE1lS9c1/img.png)

POST인 경우에만 **삭제를 진행**하도록 해준다.

확인해보기 위하여 URL로 DELETE 시도 후 서버 로그에서 **405 Error**가 뜨는지 확인하자.

![](https://blog.kakaocdn.net/dn/bn8Jin/btrLugRH9be/ciKdDVqn1kZl9k5DQfooMK/img.png)

> **require_safe()**

-   require_GET이 있지만 Django에서는 require_safe를 사용하는 것을 권장

![](https://blog.kakaocdn.net/dn/bzQ1n8/btrLwIGtHmo/9LB0evKse4MMTdnbA7BNOk/img.png)

#### # 마무리

-   Django Form Class
    -   Django 프로젝트의 주요 유효성 검사 도구
    -   공격 및 데이터 손상에 대한 중요한 방어 수단
    -   유효성 검사에 대해 개발자에게 강력한 편의를 제공
-   View 함수 구조 변화
    -   HTTP requests 처리에 따른 구조 변화
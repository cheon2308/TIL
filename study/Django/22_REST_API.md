
### **1. HTTP 복습**

> **개념**

-   HyperText Transfer Protocol
-   HTML 문서와 같은 리소스(resource, 자원)들을 가져올 수 있도록 하는 프로토콜(규칙, 약속)
-   웹에서 이루어지는 모든 데이터 교환의 기초가 된다.
-   클라이언트와 서버는 아래와 같은 개별적인 메시지 교환에 의해 통신
    -   요청(request)
        -   클라이언트에 의해 전송되는 메시지
    -   응답(response)
        -   서버에서 응답으로 전송되는 메시지

> **특징**

-   **Stateless(무상태)**  
    -   동일한 연결(connection)에서 연속적으로 수행되는 두 요청 사이에 링크가 없음
    -   즉, 응답을 마치고 연결을 끊는 순간 클라이언트와 서버 간의 통신이 끝나며 상태 정보가 유지되지 않음
    -   이를 해결하기 위해 쿠키와 세션을 사용해 서버 상태를 요청과 연결하도록 함

> **HTTP Request Methods**

-   리소스에 대한 행위(수행하고자 하는 동작)를 정의
    -   **리소스 :** HTTP 요청의 대상을 리소스(resource, 자원)라고 함
-   즉, 리소스에 대해 수행할 원하는 작업을 나타내는 메서드 모음을 정의
-   **HTTP verbs** 라고도 함
-   대표 HTTP Request Methods
    1.  **GET**
        -   서버에 리소스의 표현을 요청
        -   GET을 사용하는 요청은 데이터만 검색해야 함
    2.  **POST**
        -   데이터를 지정된 리소스에 제출
        -   서버의 상태를 변경
    3.  **PUT**
        -   요청한 주소의 리소스를 수정
    4.  **DELETE**
        -   지정된 리소스를 삭제

> **HTTP response status codes**

- 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 나타냄

1.  **Informational responses (100-199)**
2.  **Successful responses  (200 - 299)**
    -   200번 
        -   successful response
        -   요청이 성공적으로 되었고 정보는 요청에 따른 응답으로 반환된다.
3.  **Redirection messages (300-399)**
4.   **Client error responses (400-499)**
    -   400번
        -   Bad Request
        -   잘못된 문법으로 인하여 서버가 요청하여 이해할 수 없음을 의미
    -   401번
        -   Unauthorized
        -   http 표준에서는 '미승인'을 명확히하고 있지만, 의미상 이 응답은 '비인증(unauthenticated)'를 의미
        -   클라이언트는 요청한 응답을 받기 위해서는 반드시 스스로를 인증해야 한다.
    -   403번
        -   Forbidden
        -   클라이언트는 컨텐츠에 접근할 권리를 가지고 있지 않습니다.
        -   401과 다른 점은 서버가 클라이언트가 누군지 알고 있다.
    -   404번
        -   Not Found
        -   요청받은 리소스를 찾을 수 없다. 즉, 브라우저에서는 알려지지 않은 URL을 의미한다.
        -   또는 서버들은 인증받지 않은 클라이언트로부터 리소스를 숨기기 위해 이 응답을 403 대신에 전송할 수 있음
5.  **Server error responses(500-599)**
    -   500번대 -> Server error responses
    -   웹 사이트 서버에 문제가 있음을 의미 하지만 서버는 정확한 문제에 대해 더 구체적으로 설명할 수 없음.

---

### **2. URI**

앞서 알아본 Resource를 웹에서 식별하기 위해 사용하는 것이 **URI이다.**

Resource는 HTTP 요청의 대상이며 문서, 사진 또는 기타 어떤 것이든 될 수 있다.

> **URI**

-   Uniform Resource Identifier (통합 자원 식별자)
-   인터넷에서 하나의 리소스를 가리키는 문자열
-   가장 일반적인 URI는 웹 주소로 알려진 **URL**

![](https://blog.kakaocdn.net/dn/bpficu/btrOYevwkDw/xfpAJFQVGscP7KPTkMZjLk/img.png)

-   특정 이름 공간에서 이름으로 리소스를 식별하는 URI는 **URN**

![](https://blog.kakaocdn.net/dn/cUY2CT/btrOULgBL5Z/a9ez6UPwYKbMR1ivUklnk0/img.png)

> **URL**

-   Uniform Resource Locator (통합 자원 위치)
-   웹에서 주어진 리소스의 주소
-   네트워크 상에 리소스가 어디 있는지(주소)를 알려주기 위한 약속
    -   이러한 리소스는 HTML, CSS, 이미지 등이 될 수 있음
-   URL은 다음과 같이 여러 부분으로 구성되며 일부는 필수, 나머지는 선택사항

![](https://blog.kakaocdn.net/dn/bxxRAs/btrOTvEYSMn/4kyNQMWmr0gkDqmGCIaBfk/img.png)

  1. **Scheme ( or protocol)**

-   브라우저가 리소스를 요청하는 데 사용해야 하는 프로토콜
-   URL의 첫 부분은 어떤 규약을 사용하는지 나타내며 기본적으로 웹은 **HTTP(S)*를 요구하며 메일 열기 위한 mailto:, 파일 전송 위한 ftp: 등 다른 프로토콜도 존재

  2. **Authority**

-   Scheme 다음은 패턴 **://*으로 구분된 Authority(권한)이 작성됨
-   Authority는 domain과 port를 모두 포함하며 둘은 **:(콜론)*으로 구분됨
    1.  Domain Name
        -   요청 중인 웹 서버를 나타냄
        -   어떤 웹 서버가 요구되는 지를 가리키며 직접 IP 주소를 사용하는 것도 가능
        -   하지만, 사람이 외우리 쉽게 Domain Name으로 사용
    2.  Port
        -   웹 서버의 리소스에 접근하는 데 사용되는 기술적인 문(Gate)
        -   HTTP 프로토콜의 표준 포트는 다음과 같고 생략 가능 ( 나머지는 불가)
            -   HTTP - 80
            -   HTTPS - 443
        -   Django의 경우 8000(80+00)이 기본 포트로 설정

  3. **Path**

-   웹 서버의 리소스 경로
-   초기에는 실제 파일의 물리적 위치를 나타냈지만, 오늘날은 실제 위치가 아닌 추상화된 형태의 구조 표현
-   예 -> /articles/create/가 실제 articles/create 폴더 안을 나타내는 것은 아니다.

  4. **Parameters**

-   웹 서버에 제공하는 추가적인 데이터
-   파라미터는 '&' 기호로 구분되는 key-value 쌍 목록
-   서버는 리소스를 응답하기 전에 이러한 파라미터를 사용하여 추가 작업을 수행할 수 있음

  5. **Anchor**

-   리소스의 다른 부분에 대한 앵커
-   리소스 내부 일종의 "북마크"를 나타내며 브라우저에 해당 북마크 지점에 있는 콘텐츠를 표시
    -   예를 들어 HTML 문서에서 브라우저는 앵커가 정의한 지점으로 스크롤함
-   fragment identifier(부분 식별자)라고 부르는 '**#**' 이후 부분은 서버에 전송되지 않음
-   **참고 - 하이퍼링크와 비슷한 기능을 하는 인터넷상의 다른 문서와 연결된 문자 혹은 그림**

**※ 참고 - URN**

-   Uniform Resource Name (통합 자원 이름)
-   URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함 (독립적 이름)
-   URL의 단점을 극복하기 위해 등장했으며, 이름만으로 자원을 식별
-   하지만 이름만으로 실제 리소스 찾는 방법은 보편화 XXXX => 현재 대부분 URL을 사용

---

### **3. REST API**

> **API**

-   Application Programming Interface
-   애플리케이션과 프로그래밍으로 소통하는 방법
    -   개발자가 복잡한 기능을 보다 쉽게 만들 수 있도록 프로그래밍 언어로 제공되는 구성
-   **API를 제공하는 애플리케이션**과 다른 **소프트웨어 및 하드웨어 등**의 것들 사이의 **간단한 계약(인터페이스)**라고 볼 수 있음
-   API는 복잡한 코드를 **추상화**하여 대신 사용할 수 있는 몇 가지 더 쉬운 구문 제공
    -   예 -> 집의 가전제품에 전기를 공급한다 가정
    -   그저 가전제품의 플러그를 소켓에 꽂으면 제품 작동
    -   **중요한 것 :** **직접 배선을 하지 않는다는 것**

> **Web API**

-   웹 서버 또는 웹 브라우저를 위한 API
-   현재 웹 개발은 모든 것을 하나부터 열까지 직접 개발하기보다 여러 Open API를 활용하는 추세
-   대표적인 Third Party Open API 서비스 
    -   YOUTUBE
    -   NAVER
    -   Kakao
-   **API**는 **다양한 타입의 데이터를 응답**  
    -   **HTML, XML, JSON 등**

**※ Open API**

-   개발자라면 누구나 사용할 수 있도록 공개된 API
-   개발자에게 사유 응용 소프트웨어나 웹 서비스의 프로그래밍적 권한을 제공

> **REST**

-   Representational State Transfer
-   API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
-   **'소프트웨어 아키텍처 디자인 제약 모음'**
-   REST 원리를 따르는 시스템을 **RESTful 하다고** 부름
-   REST의 기본 아이디어는 리소스 즉 자원
    -   **자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술**

> **REST에서 자원을 정의하고 주소를 지정하는 방법**

1.  자원의 식별 : URI
2.  자원의 행위 : HTTP Method
3.  자원의 표현
    -   자원과 행위를 통해 궁극적 표현되는 결과물
    -   JSON으로 표현된 데이터를 제공

> **JSON**

-   JSON is a lightweight data-interchange format
-   JavaScript의 표기법을 따른 단순 문자열
-   파이썬의 dictionary, 자바스크립트의 object처럼 자료구조로 쉽게 변할 수 있는 **key-value 형태의 구조**
-   사람이 읽고 쓰기 쉽고 기계가 파싱(해석 & 분석)하고 만들어내기 쉽기 때문에 현재 API에서 가장 많이 사용하는 데이터 타입
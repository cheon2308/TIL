장고를 사용하며 기본 문법과 구성에 대해서 공부하였다. 이제는 핵!심!이라고 볼 수 있는 data를 어떻게 주고 받는지에 대해서 알아보자.

---

### 1. Sending and Retrieving form data

-   말 그대로 "데이터를 보내고 가져오기"이다.
-   HTML form element를 통하여 사용자와 애플리케이션 간의 상호작용을 이해하자

> Client & Server architecture

![](https://blog.kakaocdn.net/dn/bibQl9/btrLhO8nQbm/mT8jjXW4WHuhtwiz3Yfbak/img.png)

-   웹은 다음과 같이 가장 기본적으로 클라이언트-서버 아키텍처를 사용한다.
    -   클라이언트(일반적으로 웹 브라우저)가 서버에 요청을 보내고, 서버는 클라이언트의 요청에 응답
-   클라이언트 측에서 HTML form은 HTTP 요청을 서버에 보내는 가장 편리한 방법
-   이를 통해 사용자는 HTTP 요청에서 전달할 정보를 제공할 수 있음

---

### 2. Sending form data(Client)

> **HTML ``<form>`` element**

-   데이터가 전송되는 방법을 정의
-   웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등)을 제공하고, **사용자로부터 할당된 데이터를 서버로 전송하는 역할**을 담당
-   즉 **"데이터를 어디(action)로 어떤 방식(method)으로 보낼지"**
-   HTML form's attributes(핵심 속성)  
    -   action
        1.  입력 데이터가 전송될 URL을 지정
        2.  데이터를 어디로 보낼 것인지 지정하는 것이며 이 값은 반드시 **유효한 URL이어야 함**
        3.  만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
    -   method
        1.  데이터를 어떻게 보낼 것인지 정의
        2.  입력 데이터의 HTTP request methods를 지정
        3.  HTML form 데이터는 오직 2가지 방법으로만 전송 할 수 있는데 바로 **GET 방식**과 **POST 방식**

**아래 이미지의 흐름대로 데이터가 흘러간다는 것을 잊지말고 꼭 지키면서 작성하자. URL ->VIEW->TEMPLATE**

>`` <form>`` element 작성

![](https://blog.kakaocdn.net/dn/bvE8vu/btrLg80CMa2/rldN6OQbXt6RPHY2Y80Ii1/img.png)

![](https://blog.kakaocdn.net/dn/KccnQ/btrLgNoWx4K/CRZHYcOYJpM0xBxI3MMNgk/img.png)

![](https://blog.kakaocdn.net/dn/bccY4u/btrLhfL0TFF/KS3tW8Jk6GS254RoCZ86Z0/img.png)

> **HTML ``<input>`` element**

-   사용자로부터 데이터를 입력 받기 위해 사용
-   "type" 속성에 따라 동작 방식이 달라진다.
    -   input 요소의 동작 방식은 type 특성에 따라 현격히 달라지므로 각각의 type은 별도로 MDN 문서에서 참고하여 사용하도록 하자
    -   type을 지정하지 않을 경우 기본값은 **"text"**
-   HTML input's attribute
    -   name
        1.  form을 통해 데이터를 제출(submit)했을 때 n**ame 속성에 설정된 값을 서버로 전송**하고, **서버는 name 속성에 설정된 값을 통해 사용자가 입력한 데이터 값에 접근**할 수 있음
        2.  주요 용도는 GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑하는것
            -   GET 방식에서는 URL에서 **'****?key=value`&key`=value/****'** 형식으로 데이터를 전달

![](https://blog.kakaocdn.net/dn/crJHnV/btrLg8M6f6h/YCsUCfTrerFBCbk0Sg2khk/img.png)

> **HTTP request methods**

-   HTTP
    -   HTML 문서와 같은 리소스(데이터, 자원)들을 가져올 수 있도록 해주는 프로토콜(규칙, 규약)
-   웹에서 이루어지는 모든 데이터 교환의 기초
-   HTTP는 주어진 리소스가 수행 할 원하는 작업을 나타내는 request methods를 정의
-   자원에 대한 행위(수행하고자 하는 동작)을 정의
-   주어진 리소스(자원)에 수행하길 원하는 행동을 나타냄
-   HTTP Methd 예시
    -   **GET, POST, PUT, DELET**

> **GET**

get을 제외한 나머지는 차근차근 알아보자!

-   서버로부터 정보를 조회하는데 사용
    -   즉, 서버에게 리소스를 요청하기 위해 사용
-   데이터를 가져올 때만 사용해야 함
-   데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
    -   데이터는 URL에 포함되어 서버로 보내진다.
-   GET과 get모두 대소문자 관계없이 동일하게 동작하지만 **명시적 표현**을 위해 대문자 사용을 권장
-   데이터를 입력 후 submit 버튼을 누르고 URL의 변화를 확인하자.

![](https://blog.kakaocdn.net/dn/cpYRPC/btrLiVTgBdK/Kh9GtnxZu3ugvB8DrsdGx0/img.png)

> **Query String Parameters**

-   사용자가 입력 데이터를 전달하는 방법 중 하나로, url 주소에 데이터를 파라미터를 통해 넘기는 것
-   이러한 문자열은 앰퍼샌드(``&``)로 연결된 key=value 쌍으로 구성되며 기본 URL과 물음표(?)로 구분
    -   예시 - http://host:port/pathe?key=value`&key`=value
-   Query String이라고 하며 정해진 주소 이후에 물음표를 쓰는 것으로 시작함을 알림
-   "key=value"로 필요한 파라미터의 값을 적고 "="로 key와 value가 구분됨
-   파라미터가 여러 개일 경우 "``&``"를 붙여 여러 개의 파라미터를 넘길 수 있음
-   but!! 아직 어디로 보내야(action) 할 지는 작성해주지 않았다.

---

### 3. Retrieving the data(Server)

-   "데이터 가져오기(검색하기)"
-   서버는 클라이언트로 받은 key-value 쌍의 목록과 같은 데이터를 받게 됨
-   이러한 목록에 접근하는 방법은 사용하는 특정 프레임워크에 따라 다름
-   우리는 Django 프레임워크에서 어떻게 데이터를 가져올 수 있는지 알아보자
    -   **throw가 보낸 데이터를 catch에서 가져오기**

![](https://blog.kakaocdn.net/dn/didV14/btrLhXqA4zo/mznodOEEidaz91f2BO7Vh1/img.png)

![](https://blog.kakaocdn.net/dn/NEeBM/btrLiapTYTa/vlzVSj0jSJfyo9hjMSvbb0/img.png)

> **action 작성**

catch에서 가져오기 위한 코드를 작성해놨으면 이제 **throw페이지에서 form의 action 부분을 마저 작성 후 데이터를 보내자.**

편의를 위해서 index 페이지에 throw 하이퍼 링크를 작성한다.

![](https://blog.kakaocdn.net/dn/nkhQf/btrLgScELC5/MbOSiKV57wybfZTjVhOBxk/img.png)

> **데이터 가져오기**

-   catch 페이지가 잘 응답되어 출력됨을 확인 할 수 있는데 throw 페이지의 form이 보낸 데이터는 어디에 들어 있는걸까?
    -   catch 페이지의 url확인 
    
    ![](https://blog.kakaocdn.net/dn/mQ9Zp/btrLgPtvtDZ/NKCPJMRnlI6m8KbjWgKCtk/img.png)
    
    -   GET method로 보내고 있기 때문에 데이터를 서버로 전송할 때 Query String Parameters를 통해 전송
    -   즉, 데이터는 URL에 포함되어 서버로 보내진다.
-   그렇다면 우리가 작성해야하는 view 함수에서는 어떻게 해당 데이터에 접근 가능한걸까?
    -   **"모든 요청 데이터는 view 함수의 첫번째 인자 request에 들어있다"**
-   **request 살펴보기 - print, 에러 발생**

![](https://blog.kakaocdn.net/dn/b3H3va/btrLhPM0FRy/we0y4h4Oc6VKKHfEUYlI5K/img.png)

![](https://blog.kakaocdn.net/dn/B4Bz1/btrLk4WuU9c/500XCXLJiYS4VteLH6Xvt0/img.png)

print를 통해 살펴보기

![](https://blog.kakaocdn.net/dn/xSuJW/btrLiWkkt7u/usmU16gPqjv8MYa2UIugYk/img.png)

에러를 강제로 발생시켜 에러 페이지 하단에서 살펴보기

> catch 작성 마무리

![](https://blog.kakaocdn.net/dn/bAFVOV/btrLg71OcrR/kK4Ay4jPcdmeiFfv8ZvNv0/img.png)

![](https://blog.kakaocdn.net/dn/VSDGi/btrLihh5Sey/kwsDkvIVCOckEVeMd0apvK/img.png)

> **Request and Response objects**

-   요청과 응답 객체 흐름
    1.  페이지가 요청되면 Django는 요청에 대한 메타데이터를 포함하는 **HttpRequest object**를 생성
    2.  그리고 해당하는 적절한 view 함수를 로드하고 HttpRequest를 첫번째 인자로 전달
    3.  마지막으로 view 함수는 HttpResponse object를 반환
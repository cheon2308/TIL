이전 글에서 데이터를 url을 통해 요청하고 받는다고 배웠다. url의 작성방법에 대해 자세히 알아보자.

---

### 1. URLs?

-   **목표** : "**Dispatcher(운행 관리원)로서의 URL 이해하기**
-   웹 어플리케이션은 URL을 통한 클라이언트의 요청에서부터 시작함

> **Trailing URL Slashes**

-   Django는 URL 끝에 /가(Trailing slash) 없다면 자동으로 붙여주는 것이 기본 설정
    -   따라서 모든 주소가 '/'로 끝나도록 구성되어있음
    -   **모든 프레임워크가 이렇게 동작하는 것은 아님**
-   Django의 url 설계 철학을 통해 먼저 살펴보면 다음과 같이 설명함
-   "기술적인 측면에서, **foo.com/bar**와 **foo.com/bar/**는 서로 다른 URL이다.
    -   검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 그 둘을 서로 다른 페이지로 봄
    -   따라서 Django는 URL을 정규화하여 검색 엔진 로봇이 혼동하지 않게 해야 함

# URL 정규화

-   정규 URL(=오리지널로 평가되어야 할 URL)을 명시하는 것
-   복수의 페이지에서 같은 콘텐츠가 존재하는 것을 방지하기 위함
-   "Django에서는 trailing slash가 없는 요청에 대해 자동으로 slash를 추가하여 통합된 하나의 콘텐츠로 볼 수 있도록 한다."

> **Variable routing**

**# 필요성** 

-   템플릿의 **많은 부분이 중복**되고, **일부분만 변경**되는 상황에서 비슷한 URL과 템플릿을 계속 만들어야 할까?

**# 정의**

-   URL 주소를 변수로 하용하는 것을 의미
-   URL의 일부를 변수로 지정하여 view 함수의 인자로 넘길 수 있음
-   즉, 변수 값에 따라 하나의 paht()에 여러 페이지를 연결시킬 수 있다.

**# 작성**

-   변수는 "<>"에 정의하며 view 함수의 인자로 할당
-   기본 타입은 string이며 5가지 타입으로 명시할 수 있음

1. str

-   '/'를 제외하고 비어 있지 않은 모든 문자열
-   작성하지 않을 경우 기본 값

2. int

-   0 또는 양의 정수와 매치

3. slug

4. uuid

5. path

![](https://blog.kakaocdn.net/dn/dwUDxg/btrLg0hiR8G/DCBDZqXNgIcpFKHCHuJh80/img.png)

> View 함수 작성

- variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용할 수 있음

- **Routing(라우팅)**이란 어떤 네트워크 안에서 통신 데이터를 보낼 때 최적의 경로를 선택하는 과정

![](https://blog.kakaocdn.net/dn/pkiOL/btrLhIN097J/EvY0KgEl3DXHERgLvsSfK1/img.png)

---

### 2. App URL mapping

-   **목표 :** **앱이 많아졌을 때 urls.py를 각 app에 매핑하는 방법 이해하기**
-   두 번째 app인 pages를 생성 및 등록하고 진행하자
-   app의 view 함수가 많아지면서 사용하는 **path()** 또한 많아지고, app 또한 더 많이 작성되기 때문에 프로젝트의 **urls.py**에서 모두 관리하는 것은 **유지보수**에 좋지 않다.
-   각 app의 view함수를 다른 이름으로 **import 할 수 있음**

![](https://blog.kakaocdn.net/dn/EHcJA/btrLkvmqlcK/EC6cdMW9coekYrKoDta6W1/img.png)

이렇게도 가능하지만 더 좋은 방법을 생각해보자!

-   하나의 프로젝트의 여러 앱이 존재한다면, **각각의 앱 안에 urls.py를 만들고 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁**할 수 있다.
-   **각각의 app 폴더 안에 urls.py를 작성**하고 다음과 같이 수정 진행

![](https://blog.kakaocdn.net/dn/1Fwoq/btrLiVseQXF/o58GkuU3z9JHqUtMQBQ7ok/img.png)

> **Including other URLconfs**

-   urlpattern은 언제든 다른 **URLconf 모듈을 포함(include)** 할 수 있음
    -   **중요!! include 되는 앱의 url.py에 urlpattern이 작성되어 있지 않다면 에러가 발생한다.**
    -   **예를 들어 pages 앱의 urlpatterns(오른쪽 사진)과 같이 빈 리스트라도 작성되어 있어야 함**
-   이제 메인 페이지의 주소를 확인해보면 아래와 같이 바뀌어있을 것이다.
    -   http://127.0.0.1:8000**/index/** 에서 
    -   http://127.0.0.1:8000**/articles/index/ 로 변경**

#### **# include**

-   다른 URLconf (app1/urls.py)들을 참조할 수 있도록 돕는 함수
    -   함수 include()를 만나게 되면 URL의 그 시점까지 일치하는 부분을 잘라내고, 남은 문자열 부분을 후속 처리를 위해 include 된 URLconf로 전달

#### **# url 구조의 변화**

1. 앱의 URL을 project의 urls.py에서 관리

![](https://blog.kakaocdn.net/dn/ZEIc2/btrLgOVMKsM/BDPUVBruwttSjxv9rswMx1/img.png)

2. 복수 개의 앱의 URL을 project의 urls.py에서 관리

![](https://blog.kakaocdn.net/dn/Jw18A/btrLiA2OW8L/zpBwBzFM9MHtKSyU0fhcNk/img.png)

3. 각각의 앱에서 URL을 관리

![](https://blog.kakaocdn.net/dn/c4LXBI/btrLlFh1cjG/i89HNgb33WTeFzQu7T93u0/img.png)

---

### 3. Naming URL patterns

#### # 필요성

-   만약 "index/"의 문자열 주소를 "new-index/"로 바꿔야 한다고 가정
-   그렇다면 "index/" 주소를 사용했던 모든 곳을 찾아서 변경해야 하는 번거로움이 발생한다.

#### # 사용 과정

-   이제는 링크에 URL을 직접 작성하는 것이 아니라 "**path()" 함수의 name 인자를 정의해서 사용**
-   DTL의 Tag 중 하나인 **URL 태그**를 사용해서 **"path()" 함수에 작성한 name을 사용할 수 있음**
-   이를 통해 URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음
-   **Django는 URL에 이름을 지정하는 방법을 제공**함으로써, **view 함수와 템플릿에서 특정 주소를 쉽게 참조**할 수 있도록 도움

![](https://blog.kakaocdn.net/dn/zy6Wi/btrLg7Od3dl/89YiHMbBcW5Ve4QDkBPSB1/img.png)

> **Built-in tag -"url"**

![](https://blog.kakaocdn.net/dn/dlmuiO/btrLhXxosUi/jzZh46wgz13Gj1bUGn3AV0/img.png)

-   주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
-   템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크를 출력하는 방법

#### # 사용하기

![](https://blog.kakaocdn.net/dn/kNQY1/btrLg7goOtm/InswScKzAakUygmujKwII1/img.png)

![](https://blog.kakaocdn.net/dn/bzggJ2/btrLgScHypc/GMYKFoLYcckosmHON3msxk/img.png)

![](https://blog.kakaocdn.net/dn/b8rR3a/btrLmx5fgYu/RP1Ogf40jWbKkcUvUlJlsK/img.png)

-   마지막으로 개발자 도구를 통하여 url태그가 URL 패턴 이름과 일치하는 절대 경로 주소를 반환하는 것을 확인해보기

![](https://blog.kakaocdn.net/dn/cBaPEk/btrLirkFquc/JShKkyILWbrpIKTJuu7guk/img.png)

---

### 4. Django의 설계 철학과 framework 성격

#### # Dry 원칙

-   Don't Repeat Yourself의 약어
-   더 품질 좋은 코드를 작성하기 위해서 알고, 따르면 좋은 소프트웨어 원칙들 중 하나로 **"소스 코드에서 동일한 코드를 반복하지 말자"**라는 의미
-   동일한 코드가 반복된다는 것은 잠재적인 버그의 위협을 증가시키고, 반복되는 코드를 변경해야 하는 경우, 반복되는 모든 코드를 찾아서 수정해야 함
-   이는 프로젝트 규모가 커질수록 **애플리케이션의 유지 보수 비용이 커짐**

#### **# Django의 설계 철학 (Templates System)**

1.  **"표현과 로직(view)을 분리"**  
    -   템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
    -   즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 함
2.  **"중복을 배제"**
    -   대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 갖는다.
    -   Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 함
    -   **템플릿 상속의 기초가 되는 철학**

#### **# Framework의 성격**

-   **독선적(Opinionated)**  
    -   독선적인 프레임워크들은 어떤 특정 작업을 다루는 '올바른 방법'에 대한 분명한 의견을 가지고 있음
    -   대체로 특정 문제 내에서 빠른 개발 방법을 제시
    -   어떤 작업에 대한 올바른 방법이란 보통 잘 알려져 있고 문서화가 잘 되어있기 때문
    -   하지만 주요 상황을 벗어난 문제에 대해서는 그리 유연하지 못한 해결책을 제시할 수 있음
-   **관용적(Unopinionated)**
    -   관용적인 프레임워크들은 구성요소를 한데 붙여서 해결해야 한다거나 심지어 어떤 도구를 써야 한다는 '올바른 방법'에 대한 제약이 거의 없음
    -   이는 개발자들이 특정 작업을 완수하는데 가장 적절한 도구들을 이용할 수 있는 자유도가 높음
    -   하지만 개발자 스스로가 그 도구들을 찾아야 한다는 수고가 필요
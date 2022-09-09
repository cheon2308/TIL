**목표 : 개체를 구분할 수 있는 범위를 나타내는 namespace(이름 공간)에 대한 이해**

#### **목차**

1. URL namespace

2. Template namespace

**# Namespace의 필요성**

-   두번째 app pages의 index 페이지를 작성해보면 어떤 문제가 발생하는지 확인할 수 있다.

![](https://blog.kakaocdn.net/dn/BpzSH/btrLgTbHYp5/2AApskKw8FyrL9REQK2pmK/img.png)

![](https://blog.kakaocdn.net/dn/t9doQ/btrLgYDSSNm/KbDzWyKxKOzHtKZRcp1r01/img.png)

![](https://blog.kakaocdn.net/dn/1cuDI/btrLht4D2kW/TAFNOoYcFACXN1RHEgAoTK/img.png)

![](https://blog.kakaocdn.net/dn/RuwXy/btrLlFWHiAc/negpejrBcNLk7tko4MKw71/img.png)

위와 같이 작성을 하고 확인해보면

1.  articles app index 페이지에 작성한 두번째 앱 index로 이동하는 하이퍼 링크를 클릭 시 현재 페이지로 다시 이동한다.
    -   URL namespace
2.  pages app의 index url (http://127.0.0.1:8000/pages/index/)로 직접 이동해도 articles app의 index 페이지가 출력됨
    -   Template namespace

---

### 1. URL namespace

-   URL name space를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용할 수 있음
-   **app_name** **attribute**를 작성해 URL namespace를 설정
-   아래 이미지와 같이 URL tag를 변경해주면 된다.

![](https://blog.kakaocdn.net/dn/bf6CLJ/btrLhQeblTy/Kk9Sr66BNSxxjmrjwr4nTK/img.png)

![](https://blog.kakaocdn.net/dn/6xIgn/btrLiiH9frf/BzPXNkbTXPeuKrWFu21de0/img.png)

![](https://blog.kakaocdn.net/dn/dkJ2Eu/btrLkabGU5E/j8gR0DJ8kZdp98d4bHxOuk/img.png)

기존 url tag 변경

위와 같이 app_name:url_name 형태로 지정을 해준다면 1번째 문제는 해결할 수 있다. 2번째 문제를 해결하기 위해 다음 namespace를 알아보자

---

### 2. Template namespace

-   Django는 기본적으로 **app_name/templates/** 경로에 있는 templates 파일들만 찾을 수 있으며, **settings.py**의 **INSTALLED_APPS**에 작성한 app  순서로 template을 검색 후 렌더링 한다.
-   바로 아래 속성 값이 해당 경로를 활성화하고 있음.

![](https://blog.kakaocdn.net/dn/cpNYT5/btrLhJGcQUM/VSOcjG9uy9xMbz9vIMKZPK/img.png)

**# 디렉토리 생성을 통한 물리적 이름공간 구분**

-   Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 **app_name/templates/app_name/** 형태로 변경
-   Django templates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만들어 준다.

![](https://blog.kakaocdn.net/dn/Vrf8p/btrLk3wCwuN/neN5kvjoIfUX2pewsyrtP0/img.png)

-   이후 변경된 경로로 해당하는 모든 부분을 수정해주면 된다.

![](https://blog.kakaocdn.net/dn/boI4xP/btrLgNvPwHD/H3OOt3s9jApzLnOccExWJ1/img.png)

**# 반드시 Template namespace를 고려해야 되나?**

-   No! 만약 단입 앱으로만 이루어진 프로젝트라면 상관없음
-   여러 앱이 되었을 떄에도 템플릿 파일 이름이 겹치지 않게 하면 되지만, 앱이 많이지면 대부분은 같은 이름의 템플릿 파일이 존재하기 마련
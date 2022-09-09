#### 1. 가상 환경

파이썬을 사용하다 보면 pip로 패키지를 설치하게 되는데 이 패키지들은 파이썬 설치 폴더(디렉터리)의 Lib/site-packages 안에 저장된다. 그래서 pip로 설치한 패키지는 모든 파이썬 스크립트에서 사용할 수 있게 된다. 평소에는 이런 방식이 큰 문제가 없지만 프로젝트를 여러 개 개발할 때는 패키지의 버전 문제가 발생한다!!

예를 들어 프로젝트 A에서는 패키지 X 1.5를 사용해야 하고, 프로젝트 B에서는 패키지 X 2.0을 사용해야 하는 경우가 생기는데 이 패키지X 1.5와 2.0은 호환이 되지 않는다면 개발하기가 상당히 불편해진다.

![](https://blog.kakaocdn.net/dn/zCgHZ/btrK30BDxg6/Al6jyEhHu0WccYFZmR1eek/img.png)

이런 문제를 해결하기 위해 파이썬에서는 **가상 환경(virtual environment)을 제공**하는데, 가상 환경은 **독립된 공간을 만들어주는 기능**이다. 가상 환경에서 pip로 패키지를 설치하면 가상 환경 폴더(디렉터리)의 Lib/site-packages 안에 패키지를 저장해준다.

즉, 프로젝트 A와 B 각각 가상 환경을 만들어서 프로젝트 A에는 패키지X 1.5를 설치하고, 프로젝트 B에는 패키지X 2.0을 설치할 수 있게 되고 이렇게 하면 파이썬 스크립트를 실행할 때도 현재 가상 환경에 설치된 패키지를 사용하므로 버전 문제가 발생하지 않는다.

특히 가상 환경에는 파이썬 실행 파일(인터프리터) 자체도 포함되므로 각 가상 환경 별로 다른 버전의 파이썬 인터프리터가 들어갈 수 있다. 따라서 스크립트를 실행할 때는 원래 설치된 파이썬 인터프리터가 아닌 가상 환경 안의 파이썬 인터프리터를 사용한다.

---

### 2.. gitignore

가상 환경을 실행하기 전 GIT에 업로드를 하는 입장으로서 **'불필요하거나 올려서는 안 되는 파일'**들을 제외하기 위하여. gitignore파일을 이용할 수 있다.

-   자신이 이용하는 에디터에서. git 폴더가 있는 위치, 즉 보통 최상위 경로에. gitignore 파일을 만들어준다.
-   [https://www.toptal.com/developers/gitignore/](https://www.toptal.com/developers/gitignore/) 사이트에 들어가면 가운데 검색창에 제외할 운영체제, IDE, 프로그래밍 언어들을 검색하고 생성을 누른다.

![](https://blog.kakaocdn.net/dn/bCfjn7/btrK57M24Vu/ObuDDDSYuyrVK7v0ygWPc1/img.png)

-   생성된 문서를. gitignore에 추가해준다.

![](https://blog.kakaocdn.net/dn/bOUVxj/btrK4E534w5/WYscMnSC3Ebkcs86Tphka0/img.png)

이렇게. gitignore까지 생성해주었다면 이제 가상 환경을 실행시켜보자.

---

#### 3. **가상 환경 시작 및 기본 설정**

> 가상환경 실행하기

1.  터미널에서 **python -m venv venv** 명령어를 쳐준다.
    -   가상 환경을 생성해주므로 **'내가 사용할 폴더 내부'**에서 실행시켜주자!
2.  **source venv/Scripts/activate**
    -   생성된 가상환경을 실행시킨다.
    -   강제 종료 시에는 Ctrl + C
3. ``pip install django==3.2.13  
    -   내가 사용할 tool, 언어 등을 가상 환경 내부에서 설치해준다. django를 사용하기 위해 설치해보자
    -   따라서 운영체제에 설치되어 있는 파이썬이나, 동일 pc내의 다른 프로젝트 파일에 영향을 주지 않는다.
4.  **pip freeze > requirements.txt**  
    -   pip freeze명령어는 현재 내 환경에 pip로 설치되어 있는 라이브러리들을 모두 출력해 준다. 따라서 Django 프로젝트처럼 requirements가 필요한 프로젝트를 만들 때 터미널에서 위와 같이 쓰면 된다.
5.  **pip install -r requirements.txt**
    -   ****requirements.txt**** 내부의 패키지들을 설치해준다.

> **프로젝트 설치**

1. **django-admin startproject '프로젝트 이름' .**  
    - 프로젝트 이름에는 '-' 및 사용 중인 키워드 사용 불가  
    - 장고에게 명령, **'프로젝트** **이름'**을 만들어라 , 뒤에. 찍어주는 거 중요하다.  
    -. 을 붙이지 않는 경우 현재 디렉터리에 프로젝트 디렉터리를 새로 생성하게 됨

2. **python manage.py runserver** 

    - 프로젝트 서버 켜준다.

    - 끌 때는 컨트롤 c

  
3. **python manage.py startapp '앱 이름'**

    - 새로운 앱 생성

![](https://blog.kakaocdn.net/dn/8Q5MP/btrK2ups3uT/4uX6qk5Aediq5KckdwcRYk/img.png)

4. **저장해준다면 아래 url이 보일 것이고 Ctrl + 좌클릭으로 열어보자. 아래와 같은 화면이 나왔다면 서버가 정상 실행된 것이다.**

![](https://blog.kakaocdn.net/dn/wl1T6/btrK6cgsg07/cRV8yhhlFkvGI6LPzk9X8k/img.png)

---

#### 4. 폴더 구조

> 프로젝트 구조

- 프로젝트란 "collection of apps"  
- 프로젝트는 앱의 집합이며 여러 앱이 포함될 수 있다.  
- 앱은 여러 프로젝트에 있을 수 있다.

![](https://blog.kakaocdn.net/dn/syavj/btrK30aBY2F/psLklawaRKPeCWVb2WNqek/img.png)

1. **__init__. py**  
    - python에게 이 디렉터리를 하나의 python 패키지로 다루도록 지시  
    - 별도 추가 코드 x

  
2. **asgi.py**  
    - Asynchronous Server Gateway Interface  
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움  
    - 추후 배포 시 사용

  
3. **setting.py**  
    - Django 프로젝트 설정을 관리  
  
4. **urls.py**   
    - 사이트의 url과 적절한 view의 연결을 지정  
  
5. **wsgi.py**     
    - Web Server Gateway Interface  
    - Django 애플리케이션이 웹서버와 연결 및 소통하는 것을 도움  
    - 추후 배포 시 사용  
  
6. **manage.py**     
    - Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드 라인 유틸리티

> 앱 구조

- 앱은 실제 요청을 처리하고 페이지를 보여주는 등의 역할 담당  
- 일반적으로 앱은 하나의 역할 및 기능 단위로 작성하는 것을 권장함

![](https://blog.kakaocdn.net/dn/O8Wop/btrK49YQJYG/ZJE6LSbQUx1B51GsIkXBC0/img.png)

1. **admin.py**  
        - 관리자용 페이지를 설정하는 곳  
  
2. **apps.py**  
        - 앱의 정보가 작성된 곳  
        - 별도로 추가 코드를 작성하지 않음  
  
3. **models.py**  
        - 애플리케이션에서 사용하는 Model을 정의하는 곳  
        - MTV 패턴의 M에 해당  
  
4. **tests.py**  
        - 프로젝트의 테스트 코드를 작성하는 곳  
  
5. **views.py**  
        - view 함수들이 정의되는 곳  
        - MTV 패턴의 V에 해당

여기서 하나 중요한 점!!!

앱을 사용하기 위해 아래 사진과 같이 **프로젝트 파일 내부의 settings.py**에 등록해줄 것이다.

![](https://blog.kakaocdn.net/dn/bL76m3/btrK2njtk9t/ndy1EiNKoKJV1jHLkJSUM1/img.png)

-    반드시 생성 후 신고를 해주어야 한다!!!! firstpjt 폴더 내의 setting.py 찾아 들어가서 사진과 같이 **'app name'**을 넣어준다 (위 사진에서는 articles 앱을 등록해주었다.)
-   앱을 등록 시 advanced 한 내용을  대비하기 위해서는 순서를 지키는 것을 권장한다.

![](https://blog.kakaocdn.net/dn/234Cb/btrK1hYc0mN/pSYaEthmiFsm2spW24f96K/img.png)
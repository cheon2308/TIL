홈페이지를 구성하며 CRUD를 다루는 방법을 배웠는데, 보통 일반인이 들어가서 CRUD를 하기 위해서는 **회원가입**의 절차가 필요하다. 

우리는 관리자로서 **인증**된 User에게 **권한**을 부여하여 우리의 서비스를 이용하게 해준다.

#### **목차**

1.  authentication system
2.  Substituting a custom User model
    1.  과정
    2.  db 초기화

---

### **1. authentication system**

-   **인증(Autentication)**과 **권한(Authorization)** 부여를 함께 제공(처리)하며, 이러한 기능을 일반적으로 **인증 시스템**이라고 함
-   필수 구성은 settings.py에 이미 포함되어 있으며 INSTALLED_APPS에서 확인 가능
    -   **django.contrib.auth**
-   **Authentication(인증)**
    -   신원 확인
    -   사용자가 '누구'인지 확인
-   **Authorization(권한, 허가)**
    -   권한 부여
    -   인증된 사용자가 수행할 수 있는 작업 결정

**# 사전 설정**

**1. 두 번째 앱으로 app-accounts 생성 및 등록**

![](https://blog.kakaocdn.net/dn/t0sHl/btrMqt2eemn/XJjYIgk4LUTS9kKDPO6qdK/img.png)

여기서 app name을 다른 이름으로 해도 되지만, 

-   auth와 관련한 경로나 키워드들을 **Django 내부적으로 accounts라는 이름으로 사용**하고 있기 때문에 되도록 accounts로 지정하는 것을 권장

**2. url 분리 및 매핑**

![](https://blog.kakaocdn.net/dn/c8Lojw/btrMqtHVbrt/Q4qZ3E5ph7xfnBBWNT2tr1/img.png)

---

### **2.** **Substituting a custom User model**

-   말 그대로 **custom user model**로 **대체하기**
-   Django는 **기본적인 인증 시스템과 여러 가지 필드가 포함된 User Model을 제공**
-   대부분의 개발 환경에서 기본 User Model을 Custom User Model로 대체함
-   개발자들이 작성하는 일부 프로젝트에서는 django에서 제공하는 **built-in User model**의 **기본 인증 요구사항**이 적절하지 않을 수 있음
    -   예 - 내 서비스에서 회원가입 시 username보다 email을 식별 값으로 사용하는 것이 적합한 경우, Django의 User Model은 기본적으로 username를 식별 값으로 사용하기 때문에 적절하지 않다.
-   Django는 현재 프로젝트에서 사용할 User Model을 결정하는 **AUTH_USER_MODEL** 설정 값으로 Default User Modle을 **재정의(override)** 할 수 있도록 함

> **AUTH_USER_MODEL**

-   프로젝트에서 User를 나타낼 때 사용하는 모델
-   **중요!! 프로젝트가 진행되는 동안** **(모델을 만들고 마이그레이션 한 후)** **변경할 수 없음**
-   프로젝트 시작 시 설정하기 위한 것이며, 참조하는 모델은 첫 번째 마이그레이션에서 사용할 수 있어야 한다.
    -   즉, **첫 번째 마이그레이션 전에 확정 지어야 하는 값**
-   기본 값

![](https://blog.kakaocdn.net/dn/buWlHB/btrMoTmxJOz/MHL5rpJZKju8Kcoxv7rNtk/img.png)

**# 참고**

**AUTH_USER_MODEL**은 settings.py에 보이지 않을 텐데 어디에 있는 것일까?

-   우리가 작성하는 settings.py는 사실 **global_settings.py**를 **상속**받아 재정의하는 파일

> **과정**

-   대체하는 과정 외우기 어렵다면 해당 공식문서 보면서 순서대로 진행
-   [https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model)

 [Customizing authentication in Django | Django documentation | Django

Django The web framework for perfectionists with deadlines. Overview Download Documentation News Community Code Issues About ♥ Donate

docs.djangoproject.com](https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#substituting-a-custom-user-model)

**1. AbstractUser를 상속받는 커스텀 User 클래스 작성**

-   기존 User 클래스도 AbstractUser를 상속받기 때문에 커스텀 User 클래스도 완전히 같은 모습을 가진다.

![](https://blog.kakaocdn.net/dn/o8AfG/btrMrwqVn6p/xEN3qNCKPVaKGV4WlgfOkK/img.png)

**2. Django 프로젝트에서 User를 나타내는 데 사용하는 모델을 방금 생성한 커스텀 User 모델로 지정**

![](https://blog.kakaocdn.net/dn/OLhfu/btrMrybcdP4/F1lYYplkUk9G7KLwPoQKRK/img.png)

**3. admin.py에 커스텀 User 모델을 등록**

-   기본 User 모델이 아니기 때문에 등록하지 않으면 admin site에 출력되지 않음

![](https://blog.kakaocdn.net/dn/d2fXTz/btrMmgig2Nn/QMks9dpHSrKOJGBfavwwD1/img.png)

**# 참고**

-   User 모델 상속 관계

![](https://blog.kakaocdn.net/dn/cDyG84/btrMldTFdZg/qiRyJeXfh1qNJCG6N1FaE0/img.png)

-   **AbstractUser**
    -   관리자 권한과 함께 **완전한 기능**을 가지고 있는 **User model을 구현하는 추상 기본 클래스**
-   **Abstract base classes(추상 기본 클래스)**  
    -   몇 가지 공통 정보를 여러 다른 모델에 넣을 때 사용하는 클래스
    -   데이터베이스 테이블을 만드는 데 사용되지 않으며, 대신 **다른 모델의 기본 클래스로 사용**되는 경우 **해당 필드가 하위 클래스의 필드에 추가**

**# 주의 - 프로젝트 중간에 AUTH_USER_MODEL 변경하기**

-   모델 관계에 영향 미치기 때문에 훨씬 더 어려운 작업 필요
    -   예 - 변경사항이 자동 수행 X -> DB 스키마를 직접 수정하고, 이전 사용자 테이블에서 데이터를 이동하고, 일부 마이그레이션을 수동으로 다시 적용 등등..
-   결론 - 중간 변경은 권장하지 않는다! 반드시 **프로젝트 처음에 진행하자**

> **데이터베이스 초기화**

프로젝트가 진행 중인 경우 데이터베이스 초기화하는 방법

1.  migrations 파일 삭제
    -   migrations 폴더 및 __init__.py는 삭제 XXXXXX
    -   번호가 붙은 파일만 삭제
2.  db.sqlite3 삭제
3.  migrations 진행
    -   makemigrations
    -   migrate
4.  custom User로 변경된 테이블 확인
    -   이제 auth_user 테이블이 아니라 accounts_user 테이블을 사용

![](https://blog.kakaocdn.net/dn/c3lcvw/btrMtGmuJch/Q3KKgx5AxNj3XH2SK0mVvK/img.png)

#### **반드시 User 모델을 대체해야 할까??**

-   Django는 새 프로젝트를 시작하는 경우 비록 기본 User모델이 충분하더라도 **커스텀 User 모델 설정**하는 것을 **강력하게 권장(highly recommended)**
-   커스텀 User 모델은 **기본 User 모델과 동일하게 작동 하면서도 필요한 경우 나중에 맞춤 설정할 수 있기 때문**
    -   **단**, User 모델 대체 작업은 프로젝트의 모든 migrations 혹은 첫 migrate를 실행하기 전에 이 작업을 마쳐야 함
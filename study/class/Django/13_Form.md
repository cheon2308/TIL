우리는 지금까지 **HTML form, input 태그**를 통해서 사용자로부터 데이터를 받았고 현재 우리의 Django는 들어오는 요청을 모두 수용하고 있다.

하지만 분명 이런 요청 중에는 **비정상적인 혹은 악의적인 요청**이 있다는 것을 생각해야 한다!!

#### **목차**

1. Form

2. Widgets

---

### **1. Form**

위에서 적은 것처럼 사용자가 입력한 데이터가 우리가 원하는 데이터 형식이 맞는지에 대한 **유효성 검증**이 반드시 필요.

이런 검증은 많은 부가적인 것들을 고려해서 구현해야 하고, 이는 개발 생산성을 늦출뿐더러 쉽지 않은 작업이다.

-   **Django** **Form**은 이 과정에서 과중한 작업과 반복 코드를 줄여줌으로써 훨씬 쉽게 유효성 검증을 진행할 수 있도록 만들어 준다!!

**# Form에 대한 Django의 역할**

-   Form은 Django의 유효성 검사 도구 중 하나로 외부의 악의적 공격 및 데이터 손상에 대한 중요한 방어 수단
-   Django는 Form과 관련한 유효성 검사를 **단순화하고 자동화할** 수 있는 기능을 제공하여, 개발자가 직접 작성하는 코드보다 더 안전하고 빠르게 수행하는 코드를 작성할 수 있다.
-   즉, **개발자가 필요한 핵심 부분만 집중할 수 있도록 돕는 프레임워크의 특성**

> **Django가 form과 관련하여 처리하는 세 부분**

1.  렌더링을 위한 데이터 준비 및 재구성
2.  데이터에 대한 HTML forms 생성
3.  클라이언트로부터 받은 데이터 수신 및 처리

**# The Django Form Class**

Django form 관리 시스템의 핵심인 **Form Class**

> **선언**

-   Form Class를 선언하는 것은 Model Class를 선언하는 것과 비슷하다.
-   비슷한 이름의 필드 타입을 많이 가지고 있지만 **이름만 같고 같은 필드는 아님**
-   Model과 마찬가지로 상속을 통해 선언 - forms 라이브러리의 Form 클래스를 상속받음

앱 폴더에 forms.py를 생성 후 ArticleForm Class를 선언해준다.

![](https://blog.kakaocdn.net/dn/bIoWP6/btrLu7699BQ/Z2qBXsNDFlnrv0EBEAt4P1/img.png)

-   form에는 model field와 달리 **TextField가 존재하지 않는다.**
-   모델의 TextField처럼 사용하려면 어떻게 작성할 수 있을지는 다음 글에서 알아보자.

![](https://blog.kakaocdn.net/dn/ca0UOq/btrLvCMEcb2/lQkKZi9X8GbctEBoVmKqcK/img.png)

**주의!**

-   "Form Class를 forms.py에 작성하는 것은 규약이 아니다."
-   파일 이름이 달라도 되고 modles.py든 어디든 작성해도 괜찮지만 우리는 항상 생각해야 된다.
-   **더 나은 유지보수의 관점,** 그리고 관행적으로 forms.py 파일 안에 작성하는 것을 권장

이후, 'new' view 함수를 업데이트시켜주자.

![](https://blog.kakaocdn.net/dn/Ax9BQ/btrLuw0pKmy/vQAPr8SFkkbpQjANrblw6k/img.png)

Template 또한 업데이트!

![](https://blog.kakaocdn.net/dn/GckQ6/btrLuyKG5AX/DnmnvnSdZj1w9koAt1Jl71/img.png)

업데이트 이후 출력을 확인해보자

![](https://blog.kakaocdn.net/dn/UT0rc/btrLsrr5JaU/cfgK68HysD96BdF1IZtEo1/img.png)

-   view 함수에서 정의한 ArticleForm의 인스턴스(form) 하나로 input과 label 태그가 모두 렌더링 되는 것을 확인하기
-   각 태그의 속성 값을 또한 자동을 설정되어있음

> **From rendering options**

-   `<label> & <input>` 쌍에 대한 3가지 출력 옵션
    1.  **as_p()**
        -   각 필드가 단락(`<p>` 태그)으로 감싸 져서 렌더링
    2.  **as_ul()**
        -   각 필드가 목록 항목(`<li> 태그)으로 감싸져서 렌더링
        -   `<ul>` 태그는 직접 작성해야 한다.
    3.  **as_table()**
        -   각 필드가 테이블(`<tr>` 태그) 행으로 감싸져서 렌더링

> **2가지 HTML input 요소 표현**

  1. Form fields

-   입력에 대한 유효성 검사 로직을 처리
-   템플릿에서 직접 사용됨

![](https://blog.kakaocdn.net/dn/5T7s8/btrLwz3d64u/fA8FadfwApU6lUs5s0GhC1/img.png)

  2. Widgets

-   웹 페이지의 HTML input 요소 렌더링을 담당
    -   input 요소의 단순한 출력 부분을 담당
-   Widgets은 **반드시 form fields에** **할당**

![](https://blog.kakaocdn.net/dn/yddUf/btrLvKRq9jY/sjAQQ3yqVYaqmFQgUw3IEK/img.png)

---

### 2. Widgets

-   Django의 HTML input element의 표현을 담당
-   단순히 **HTML 렌더링을 처리하는 것**이며 유효성 검증과 아무런 관계가 없다.
    -   "웹 페이지에서 input element의 단순 raw 한 렌더링만을 처리하는 것일 뿐"

> Textarea 위젯 적용

위에서 말했듯이 반드시!! **form fields에 작성**해준다.

![](https://blog.kakaocdn.net/dn/cbOY37/btrLu2x2ksL/DpOq5ic1KQnfljWqZRPniK/img.png)

출력 결과 확인해보기.

-   다양한 built-in 위젯은 아래 사이트에서 확인 가능
-   https://docs.djangoproject.com/ko/3.2/ref/forms/widgets/#built-in-widgets

![](https://blog.kakaocdn.net/dn/cZ1ffh/btrLu1Tru4r/7JVeJQbATgowKseMFGKuPk/img.png)

> Form fields와 widget 응용

![](https://blog.kakaocdn.net/dn/bSDbGH/btrLr3LrBat/9KMD0BqNAlolkRd25eG1MK/img.png)

아래와 같은 출력 결과를 볼 수 있다. 앞으로는 form field와 widgets 공식문서를 찾아보며 조합 사용해보자!!

![](https://blog.kakaocdn.net/dn/dePfAw/btrLu1FSjTI/CumgfOglvqdKaoUKWvAUF0/img.png)
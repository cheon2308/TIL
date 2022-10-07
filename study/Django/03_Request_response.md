#### 1. VIEW

웹 페이지에서 하이퍼링크를 통하여 다른 페이지로 이동하기 위해서는 URL이라는 주소를 적어주어야 한다.

-   **프로젝트 폴더 - urls.py의 urlpatterns 리스트 내에 경로 지정**
    -   **path('app name/', include('app name.urls'))**
-   **사용할 앱 폴더 - urls.py 내에** 모듈을 import해준다.  
	-   **from django.urls import path**
    -   **from 'app name' import views**
-   마찬가지로 **앱 폴더 -urlpatterns 리스트 내부**에 **경로를 지정**해준다.
    -   **path('함수 name/', views. 함수 name),**

![](https://blog.kakaocdn.net/dn/oId3e/btrK3ZW27lu/unztuvkQumvFNlNyif2wk1/img.png)




-   이제 앱 폴더 - view.py에 사용할 데이터 함수를 정의해준다.
    -   **def 함수 name(request): return render(request, '함수 name.html')**
    -   HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
    -   Template에게 HTTP 응답 서식을 맡김

![](https://blog.kakaocdn.net/dn/Nyhk1/btrK6BUHndN/I3UQuqATCaqkURnfnECUt0/img.png)


> render 함수

![](https://blog.kakaocdn.net/dn/kCMoi/btrK4WeqINQ/ySckKRI88rQyrKAtbVSJV0/img.png)

-   주어진 템플릿을 주어진 콘텍스트 데이터와 결합하고 랜더링 된 텍스트와 함께 HttpResponse(응답) 객체를 반환하는 함수이다.

1. requset

-   응답을 생성하는 데 사용되는 요청 객체

2. template_name

-   템플릿의 전체 이름 또는 템플릿 이름의 경로

3. context

-   템플릿에서 사용할 데이터 (딕셔너리 타입으로 작성)

---

#### 2. Templates

![](https://blog.kakaocdn.net/dn/c4SKOn/btrK2nKBqTy/RzSl204ceQmnsXf8g8Zc0K/img.png)

-   실제 내용을 보여주는 데 사용되는 파일
-   파일의 구조나 레이아웃을 정의
-   Template 파일의 기본 경로
    -   app 폴더 안의 templates 폴더
    -   app_name/templates/
    -   **중요!! 템플릿 폴더 이름은 반드시 templates라고 지정**

앞으로 Django의 코드 작성은 URL - VIEW - TEMPLATE 순으로 작성하자!! 즉, **"데이터의 흐름 순서"** 대로 작성한다.

![](https://blog.kakaocdn.net/dn/cFTlvk/btrK8e5VRoo/kkCRUHhCpF2wOAEI2cxhYK/img.png)

---

#### 3. 추가 설정

1. Language_code

-   모든 사용자에게 제공되는 번역을 결정
-   이 설정이 적용되려면 **USE_I18N이 활성화(True)**되어 있어야 한다.

![](https://blog.kakaocdn.net/dn/crApVi/btrK561JBXb/IY5S6K8cQWMF33BdgCPPj1/img.png)

2. TIME_ZONE

-   데이터베이스 연결의 시간대를 나타내는 문자열 지정
-   USE_TZ가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면, UTC 대신 새로 설정한 시간대의 인식 날짜&시간이 반환됨
-   USE_TZ이 False인 상태로 이 값을 설정하는 것은 error가 발생하므로 주의

3. USE_I18N

-   Django의 번역 시스템을 활성화해야 하는지 여부를 결정

4. USE_L10N

-   데이터의 지역화된 형식(localized formatting)을 기본적으로 활성화할지 여부를 지정
-   True일 경우, Django는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시

5. USE_TZ

-   datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
-   True일 경우 Django는 내부적으로 시간대 인식 날짜 / 시간을 사용
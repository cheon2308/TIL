### 1. Admin Site

-   **Django의 가장 강력한 기능 중 하나**
-   **automatic admin interface**
-   "관리자 페이지"
    -   사용자가 아닌 **서버의 관리자**가 활용하기 위한 페이지
    -   **모델 class를 admin.py에 등록하고 관리**
    -   레코드 생성 여부 확인에 매우 유용하며 직접 레코드를 삽입할 수도 있다.

> **admin 계정 생성**

```
python manage.py createsuperuser
```

-   username과 password를 입력하여 관리자 계정을 생성해준다.
-   email은 선택사항이라 입력하지 않고 enter로 넘겨주어도 된다.
-   비밀번호 생성 시 보안상 터미널에 입력되지 않으니 무시하고 입력 이어가도 된다.

> **admin site 로그인**

-   작성하는 app의 url에서 app name 대신 admin을 넣어주면 된다
    -   예) https://127.0.0.1:8000/~~app_name/~~ **admin/** 로 접속 후 로그인
-   계정만 만든 경우 Django 관리자 화면에서 모델 클래스는 보이지 않는다.

![](https://blog.kakaocdn.net/dn/UTxUn/btrLtL4uFMO/JGNGzick5nH8LcK6dPN1MK/img.png)

> **모델 클래스 등록**

-   모델의 record를 보기 위해서는 admin.py에 등록해주어야 한다.

![](https://blog.kakaocdn.net/dn/1OEp3/btrLntKiDex/oUk35wL1M5Kkck7W9WG6B0/img.png)

![](https://blog.kakaocdn.net/dn/zVTb2/btrLu3i1s9Y/0FOzH1PR9zQ2aFdfsWLUl1/img.png)

위와 같이 모델 클래스가 생긴 것을 확인할 수 있다.
프로젝트를 진행하며 기본 구성과 같은 같은 코드를 매번 같이 치는 것은 귀찮고 불편한 일이다.

파이썬 class를 배우며 이런 불편함을 해소하기 위하여 함수와 class에 대해서 배웠는데 **Django에서도 Class선언을 하여 상속을 해줄 수 있다는 것**을 알게 되었다!!

---

## 1. Inheritance

-   템플릿 상속은 기본적으로 코드의 재사용성에 초점을 맞춤
-   템플릿 상속을 사용하면 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override) 할 수 있는 블록을 정의하는 기본 'skeleton' 템플릿을 만들 수 있음

> 관련 태그

```PYTHON
{% extends 'skeleton name' %}
```

- 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알린다.

- **중요! 반드시 템플릿 최상단에 작성되어야 한다 - 2개 이상 사용 x**

```PYTHON
{% block content %}
{% endblock content %} 또는 {% endblock %}
```

-   하위 템플릿에서 재지정(overridde)할 수 있는 블록을 정의
-   즉, 하위 템플릿이 채울 수 있는 공간
-   가독성을 높이기 위해 선택적으로 endblock 태그에 이름을 지정할 수 있음

---

### 2. example

이전에 배웠던 bootstrap CDN을 모든 폴더에 적용시켜보자!

1. 우선 내가 진행하고 있는 PJT폴더, APP폴더와 동일한 경로에 **templates 폴더 생성 후 base.html과 같이 skeleton 템플릿을 작성**한다.

![](https://blog.kakaocdn.net/dn/bigwLI/btrLhs5zS4s/v7HXWc07gNshlMegehvBG0/img.png)

2. base.html의 위치를 앱 안의 template 디렉토리가 아닌 프로젝트 최상단 templates 폴더에 위치시켰기 때문에 기본 template 경로가 아닌 다른 경로를 추가해주기 위해서 'project' - 'settings.py' 내부에 TEMPLATES 리스트에 아래와 같이 작성

![](https://blog.kakaocdn.net/dn/c9gYMM/btrLhtwFhms/yXLzKYuMQRAiCev9MJByc1/img.png)

BASE_DIR은 Django에서 절대 경로로 편하게 작성할 수 있도록 미리 지정해둔 값

2. app폴더 - templates폴더 - index 템플릿 또는 내가 사용할 html 템플릿에서 상속받아주고 적용되었는지 확인

![](https://blog.kakaocdn.net/dn/FEwj7/btrLj9RgLDw/wVopRjy1tk9kZhxkcQ9Qyk/img.png)
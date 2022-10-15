#### 1. Tmeplate?

Django Template의 정의는 **"데이터 표현을 제어하는 도구이자 표현에 관련된 로직"**이라고 말할 수 있다.

- Django Template을 이용한 HTML 정적 부분과 동적 콘텐츠를 삽입
- Template System의 기본 목표를 숙지하자

Template System이란 **데이터 표현을 제어하는 도구이자 표현에 관련된 로직을 담당**하는 것으로 Template의 정의로 보면 된다..

### **2. Django Template Language(DTL)**

- Django template에서 사용하는 built-in template system
- 조건, 반복, 변수 치환, 필터 등의 기능을 제공한다.
  - python 처럼 일부 프로그래밍 구조(if, for 등)를 사용할 수 있지만 이것은 **Python 코드로 실행되는 것은 아니다!!**
  - Django 템플릿 시스템은 단순히 Python이 HTML에 포함된 것이 아니니 주의하자.
- 프로그래밍적 로직이 아니라 **'프레젠테이션'**을 표현하기 위한 것임을 명심하자

# DTL Syntax

syntax는 언어의 구조 및 문법에 관한 것으로 "내가 타당한 문장을 구성하였는가?"의 질문과 연관이 있다.

**1. Variable**

![](https://blog.kakaocdn.net/dn/bVawyC/btrK49LkkSk/YvkPsv4ReiDlCT4bgRpoak/img.png)

- 변수명은 영어, 숫자와 밑줄(_)의 조합으로 구성될 수 있으나 **밑줄로는 시작 할 수 없다.**
  - 또한 공백이나 구두점 문자 또한 사용할 수 없음
- dot(.)를 사용하여 변수 속성에 접근할 수 있음
- render()의 세 번째 인자로 {'key':value}와 같이 딕셔너리 형태로 넘겨주며, 여기서 정의한 **key에 해당하는 문자열**이 **template에서 사용 가능한 변수명**

**2. Filters**

![](https://blog.kakaocdn.net/dn/r45eF/btrK1hKBekF/aK0SGpCr3kW2tlsbL0vMMk/img.png)

- 표시할 변수를 수정할 때 사용
  - 예) name변수를 모두 소문자로 출력 - **{{ name | lower }}**
- 60개의 built-in template filters를 제공
- chained가 가능하며 일부 필터는 인자를 받기도 한다. **{{ name|truncatewords:30 }}**

**3. Tags**

![](https://blog.kakaocdn.net/dn/cgUf2c/btrK468XG20/Jv9828g1Jh4pbecAumBvh0/img.png)

- 출력 텍스트를 만들거나, 반복 또는 논리를 수행하여 제어 흐름을 만드는 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그가 필요 - **{% if %}{% endif %}**
- 약 24개의 built-in template tags를 제공

**4. comments(주석)**

![](https://blog.kakaocdn.net/dn/9I5TW/btrK5EdfFER/dNzQe2bDH1yLz37FKBZ2E1/img.png)

- Django template에서 라인의 주석을 표현하기 위해 사용
- 한 줄 주석에만 사용할 수 있음 (줄 바꿈 허용 x)
- 아래처럼 유효하지 않은 템플릿 코드가 포함될 수 있다.

![](https://blog.kakaocdn.net/dn/cPdHNL/btrK3YYaYKA/5RGkAI1NnUXKWdsV8bQKq1/img.png)

- 여러 줄 주석은 {% comment %}와 {% endcomment %} 사이에 입력

![](https://blog.kakaocdn.net/dn/yGY33/btrK8gQdxZh/QKXtMnmPVufPuzXO37Kfj0/img.png)

---

### 3. 간단한 실습

1. variable

![](https://blog.kakaocdn.net/dn/q3mTS/btrK6Rb5kCu/YfO75NfItwDyI7ZSFXfb30/img.png)

- urls.py에 경로를 설정 해준 후, view함수에 요청 객체를 정의해준다.
- app 폴더 내에 **templates** **폴더** 생성 후 **요청 객체 이름.html 파일**을 만들어준다.
- <body> 내에 표시할 정보 입력 및 variable을 사용한 모습

 하지만 위와 같이 작성한다면 context 내용이 많아질 경우 굉장히 가독성이 떨어질 것이다!

따라서 아래와 같이 작성해주는 것이 바람직해 보인다 :)

![](https://blog.kakaocdn.net/dn/sOWBu/btrK4WFr3Pl/Pjh2hOMfuGbw7MZ53gZTr1/img.png)

위의 오른쪽 사진에서 보듯이 foods.0과 같이 배열의 인덱스 및 딕셔너리의 키 값에 접근할 수 있다.



2. filters

![](https://blog.kakaocdn.net/dn/bb3ILv/btrK3X5Wq56/srcqt4KibenAiLIfprFoi1/img.png)

join 함수를 이용하여 리스트 형태가 아닌 문자열 형태로 출력도 할 수 있고 여러가지로 유용하게 사용할 수 있는 것을 볼 수 있다.



3. tags

![](https://blog.kakaocdn.net/dn/dFo5z3/btrK30BF7TB/kRiMBSnk2ovcNBbbl6GDJk/img.png)

반복문을 사용하기 위하여 {% for ... 과 같이 tags를 활용하여 출력해준다!



4. comments

![](https://blog.kakaocdn.net/dn/dWdgZw/btrK3W62ZK7/Np9RO0Ujl7QQX9511IJ7Uk/img.png)

방금까지 다뤄본 것들로 간단한 출력을 해볼 수 있다. 그런데 코드도 길고 새로 app을 만들 때마다 하나하나 작성해주기가 조금 귀찮은 게 느껴진다!

다음 글에서는 **파이썬**에서 배웠던 **상속**을 적용시켜 더 편하게 써보자.
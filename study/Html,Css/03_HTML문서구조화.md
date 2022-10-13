우선, HTML의 요소는 크게 인라인 / 블록 요소로 나누게 되는데 CSS에 들어가서 자세한 내용을 배우기 때문에 대충 넘어가자.

-   인라인 요소 : 글자처럼 취급
-   블록 요소 : 한 줄 모두를 사용한다.

> 먼저, 보고 있는 이 문장을 다루는 텍스트 요소에 대해 먼저 알아보자.

1.  <a></a> : href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
2.  <b></b>, <strong></strong> : 굵은 글씨 요소 -> 중요한 강조하고자 하는 요소
3.  <i></i>, <em></em> : 기울임 글씨 요소 -> 중요한 강조하고자 하는 요소
4.  <br> : 텍스트 내에 줄 바꿈 생성
5.  <img> : src 속성을 활용하여 이미지 표현
6.  <span></span> 의미 없는 인라인 컨테이너

![](https://blog.kakaocdn.net/dn/KHVJr/btrI7LSbGxL/GoaD2NKBCpSTilfh6g1jI1/img.png)

텍스트 요소 사용 예시

> 위의 리스트와 같이 전체 틀을 다루는 그룹 컨텐츠를 알아보자.

1.  ``<p></p>`` : 하나의 문단 (paragraph)
2.  ``<hr>`` : 문단 레벨 요소에서의 주제의 분리를 의미하며 수평선으로 표현됨 (A Horizontal Rule)
3.  ``<ol></ol>, <ul></ul>`` : 순서가 있는 리스트와 순서가 없는 리스트
4.  ``<pre></pre>`` : HTML에 작성한 내용을 그대로 표현, 보통 고정폭 글꼴이 사용되고 공백 문자를 유지
5.  ``<blockquote</blockquote>`` : 텍스트가 긴 인용문, 주로 들여 쓰기를 한 것으로 표현됨
6.  ``<div></div>`` : 의미 없는 블록 레벨 컨테이너

![](https://blog.kakaocdn.net/dn/b3Rxoh/btrI1hMlIer/b2sjoRyVnOfk3UgX51OncK/img.png)

그룹 태그 사용 예시

> 주소창, 검색창과 같은 정보를 서버에 제출하기 위해 사용하는 태그에 대해 알아보자.

1.  action : form을 처리할 서버의 URL (데이터를 보낼 곳)
2.  method : form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
3.  enctype : method가 post인 경우 데이터의 유형
    -   application/x-www-form-urlencoded : 기본값
    -   multipart/form-data : 파일 전송시 (input type이 file인 경우)
    -   ~~text/plain : HTML5 디버깅 용 (잘 사용 X)~~

![](https://blog.kakaocdn.net/dn/qGHk5/btrIXXtJpWb/SnVuLYERr6K97GURgEi380/img.png)

form 사용 예시

form은 내부에 input과 label이라는 태그를 이용하여 내용을 구성한다.

> input의 속성

-   다양한 타입을 가지는 **입력 데이터 유형**과 **위젯**이 제공됨
-   name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
-   value : form control에 적용되는 값 (이름/값 페어로 전송됨)
-   required, readonly, autofocus, autocomplete, disable 등

![](https://blog.kakaocdn.net/dn/TVVJH/btrIYBxaLLz/MkIpwNsKwTxLDnyRumhkt0/img.png)

input 사용 예시1

![](https://blog.kakaocdn.net/dn/dvqdXo/btrI2UCiVL8/0tTUCyJmagPHAbfeebTwM0/img.png)

input 사용 예시2

> input label

-   label을 클릭하여 input 자체의 초점을 맞추거나 활성화시킬 수 있음
    -   사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서 편하게 사용할 수 있음
    -   label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인할 수 있도록 함
-   <input>에 id 속성을, <label>에는 for 속성을 활용하여 상호 연관을 시킴

![](https://blog.kakaocdn.net/dn/qszJU/btrI7NbqdmO/qLb21KjWOPGoJ45sozMYR1/img.png)

label 태그 활용 예시

이렇게 글만 봐서는 이해도 잘 안되고 금방 까먹는다! 아래 코드를 직접 vscode에 쳐보고 실행 결과를 확인하며 배워보자

![](https://blog.kakaocdn.net/dn/YvTyb/btrI7MQ64M6/xUa0kOKksGTVtBKaKnqAJ0/img.png)

~~직접 실행해보니 자주 보던 화면이 등장 할 것이다. 그래도 조금은 이해가 더 잘 되지 않는가?~~

마지막으로 input 태그의 유형 몇 가지만 짚어보고 이번 글을 마무리해보자 파이팅!!

> input 유형 - 일반

-   text : 일반 텍스트 입력
-   password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표시 -> 단지 보이지만 않을 뿐 암호화된 것이 아니다!
-   email : 이메일 형식이 아닌 경우 form 제출 불가
-   number : min, max, step 속성을 활용하여 숫자 범위 설정 가능
-   file : accept 속성을 활용하여 파일 타입 지정 가능

![](https://blog.kakaocdn.net/dn/dXT3pq/btrI3tSjRyy/VnGytM4VPfQIzRrn5dVLv1/img.png)

일반 type 예제

> input 유형 - 항목 중 선택

-   일반적으로 label 태그와 함께 사용하여 선택 항목을 작성
-   동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
    -   checkbox: 다중 선택
    -   radio: 단일 선택

![](https://blog.kakaocdn.net/dn/DQTHc/btrI2waUhJo/69k5shrd1eUU6bd2SbHLg0/img.png)

항목 중 선택 예시

> input 유형 - 기타

-   다양한 종류의 input을 위한 picker 제공
    -   color : color picker
    -   date : date picker
-   hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정
    -   hidden : 사용자에게 보이지 않는 input

![](https://blog.kakaocdn.net/dn/Op9Tc/btrI6qOjD70/ypbkqeHPBTDKtsJqmkdxn0/img.png)

> input 유형 - 종합

-   <input> 요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지할 것!
-   참고 사이트 : [https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input)
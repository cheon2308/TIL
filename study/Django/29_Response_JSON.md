이전 글에서 알아보았던 JSON 형태로의 서버의 응답 변화와 다양한 방법의 JSON 응답에 대해 알아보자.

#### **목차**

1.  Intro
2.  Response

---

### **1. Intro**

> **서버가 응답하는 것**

-   현재까지의 Django로 작성한 서버는 사용자에게 **페이지(html)**만 응답하고 있었음
-   하지만 사실 서버가 응답할 수 있는 것은 페이지뿐만 아니라 **다양한 데이터 타입**을 응답할 수 있음

![](https://blog.kakaocdn.net/dn/JuA60/btrOYxuYFg3/YCqMAmhcCe3HJS2DVZS5c0/img.png)

페이지(html)를 응답하는 서버

![](https://blog.kakaocdn.net/dn/kQfYf/btrOYIJNhrl/GgQaqwm49BKtM9KRM5sRK1/img.png)

JSON 데이터를 응답하는 서버로의 변환

이런 과정을 거치게 된다면 사용자에게 보여질 화면은 누가 구성하게 되는 걸까?

![](https://blog.kakaocdn.net/dn/cCWgyF/btrOYokJ5Gp/4KCkS4DQnYO2MlffC4B350/img.png)

-   JSON 데이터를 받아 화면을 구성하여 사용자에게 보여주는 것은 **Front-end Framework**가 담당할 예정

![](https://blog.kakaocdn.net/dn/nRxlg/btrOYxBLI1E/QK3UVjXh6zqQCwuYnkdK3K/img.png)

-   Front-end Framework는 Vue.js를 사용
-   Django는 더 이상 Template 부분에 대한 역할 담당 x 

---

### **2. Response**

JSON 데이터를 응답하는 방법엔 4가지 방법이 있다.

---

  **1. HTML 응답**

-   문서 한 장을 응답하는 서버 확인
-   지금까지 해오던 방식

![](https://blog.kakaocdn.net/dn/bjsy0Y/btrOXkXJJj6/s3k829ekYSRPkuwvYUgKTK/img.png)

![](https://blog.kakaocdn.net/dn/bMHKNy/btrOZICxK6w/Pzp45lcbIjp2n5ixy9aK91/img.png)

![](https://blog.kakaocdn.net/dn/bwjQ9S/btrOZ88NagM/kbm1ysvQrjpO2Qp5ZiwDXK/img.png)

응답 페이지 확인

**※ 참고 - 'Content-Type' entity header**

-   리소스의 media type(MIME type, content type)을 나타내기 위해 사용
-   응답 내에 있는 컨텐츠의 콘텐츠 유형이 실제로 무엇인지 알려줌

---

  **2. JsonResponse()를 사용한 JSON 응답**

-   이제는 문서 한 장이 아닌 JSON 데이터를 응답해보기
-   Django가 기본적으로 제공하는 JsonResponse 객체 활용하여 Python 데이터 타입을 손쉽게 JSON으로 변환하여 응답 가능
-   **JsonResponse()**
    1.  Json-encoded response를 만드는 클래스 
    2.  **'safe'** parameter
        -   기본 값 True
        -   False로 설정 시 모든 타입의 객체를 serialization 할 수 있음
        -   그렇지 않으면 dict 인스턴스만 허용)

![](https://blog.kakaocdn.net/dn/qP8WV/btrOZ9Ua4ht/gK0Ts1eIm5m8SkLujA5160/img.png)

![](https://blog.kakaocdn.net/dn/dWoz45/btrOZ8VhmnE/Ix4c0JZOZil6EQ2m5u2WJk/img.png)

---

**3. Django Serializer를 사용한 JSON 응답**

-   Django의 내장 HttpResponse()를 활용한 JSON 응답
-   이전에는 JSON의 모든 필드를 하나부터 열까지 작성해야 했지만 이제는 그렇지 않음

![](https://blog.kakaocdn.net/dn/deFsN0/btrOX39lXRm/vx03U0wcMSbIDh485pPZPk/img.png)

![](https://blog.kakaocdn.net/dn/FBWWY/btrOY9ApofX/Aka8NU0xZOGTMIKUlD2O2k/img.png)

> **Serialization**

-   "직렬화"
-   데이터 구조나 객체 상태를 동일 혹은 다른 컴퓨터 환경에 저장하고, 나중에 재구성할 수 있는 포맷으로 변환하는 과정
    -   즉, 어떠한 언어나 환경에서도 **"나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정"**
-   변환 포맷은 대표적으로 json, xml, yaml이 있으며 **json**이 가장 보편적으로 쓰임

![](https://blog.kakaocdn.net/dn/J65k9/btrO9ChOcyv/aGlkMPNWLakLEqDmds1udK/img.png)

-   Django의 **serialize()**는 Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환할 수 있는 Python 데이터 타입으로 만들어 줌

![](https://blog.kakaocdn.net/dn/dn8pXV/btrO78WiO1v/uD4QRNJX6YcOTMfib2pwVK/img.png)

**4. Django REST framework를 사용한 JSON 응답**

> **Django REST framework(DRF)**

-   Django에서 Restful API 서버를 쉽게 구축할 수 있도록 도와주는 오픈소스 라이브러리
-   Web API 구축을 위한 강력한 toolkit을 제공
-   REST framework를 작성하기 위한 여러 기능을 제공
-   DRF의 SERIALIZER는 Django의 Form 및 ModelForm 클래스와 매우 유사하게 작동
-   https://www.django-rest-framework.org/

![](https://blog.kakaocdn.net/dn/dlwhV9/btrOQpkdbwt/x7ihWF1en8ayEybytFHvr1/img.png)

-   ModelForm과 유사한 ModelSerializer 구조 및 사용법 확인하기

![](https://blog.kakaocdn.net/dn/sRrSG/btrOQqpSBVI/Y2lXhF8pbsnQZoCPcvK3t0/img.png)

-   JSON 데이터를 DRF 전용 템플릿으로 응답한다.

![](https://blog.kakaocdn.net/dn/RCeXv/btrO50LijGm/uyz0YK8Tg0C3oQZZjqiw7k/img.png)
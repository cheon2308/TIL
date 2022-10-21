앞에서는 1:1 relationship, 1:N relationship을 살펴보았다면 이번엔 Many-to-many relationships **M:N** relationship에 대해서 알아보자.

한 테이블의 0개 이상의 레코드가 다른 테이블의 0개 이상의 레코드와 관련된 경우이며, 양쪽 모두에서 N:1 관계를 가진다.

#### **목차**

1.  Intro
2.  Django ManyToManyField
3.  정리

---

### **1. Intro**

**※ 데이터 모델링**

-   주어진 개념으로부터 논리적인 데이터 모델을 구성하는 작업
-   물리적인 데이터베이스 모델로 만들어 고객의 요구에 따라 특정 정보 시스템의 데이터베이스에 반영하는 작업

> **시작하기 전 용어 정리**

-   **target model**  
    -   관계 필드를 가지지 않은 모델
-   **source model**
    -   관계 필드를 가진 모델

> **N:1의 한계**

-   의사와 환자 간 예약 시스템을 구현해보자
-   지금까지 배운 N:1 관계를 생각해 한 명의 의사에게 여러 환자가 예약할 수 있다고 모델 관계를 설정

![](https://blog.kakaocdn.net/dn/dAJA9N/btrOnr4hhsS/cwigjsHBVWZkZb0XyRDKCK/img.png)

-   각각 2명의 의사와 환자를 생성하고 환자는 서로 다른 의사에게 예약을 했다고 가정

![](https://blog.kakaocdn.net/dn/bI4oKv/btrOqAF8ybc/qSV27fSH9KeG9wSOdDVtWK/img.png)

![](https://blog.kakaocdn.net/dn/8oDXz/btrOqA0vkaa/GWElNRncUaOpxvom3eUhM0/img.png)

-   1번 환자(carol)가 두 의사 모두에게 방문하려고 함

![](https://blog.kakaocdn.net/dn/d14p3T/btrOo7j6pSx/dKHjJo65pETBmEI89MIyHk/img.png)

-   여기서 동시에 예약을 할 수는 없을까?

![](https://blog.kakaocdn.net/dn/dO4Ih6/btrOqBrx0OK/k6BiZ9CTSRgwbX41wpkB80/img.png)

-   위에서 볼 수 있듯이 SyntaxError가 발생한다.
-   동일한 환자지만 다른 의사에게 예약하기 위해서는 객체를 하나 더 만들어서 예약을 진행해야 함
-   따라서 새로운 환자 객체를 생성할 수밖에 없음
-   외래 키 컬럼에 '1,2' 형태로 참조하는 것은 **Integer 타입이 아니기 때문에** 불가능

그렇다면 "예약 테이블을 따로 만들자"

> **중개 모델**

-   환자 모델의 외래 키를 삭제하고 별도의 예약 모델을 새로 작성
-   예약 모델은 의사와 환자에 각각 N:1 관계를 가짐

![](https://blog.kakaocdn.net/dn/ESFVN/btrOnrQJQN3/1QUIbcSDIw18theukktbIk/img.png)

-   Model을 수정하고 나면 migration 진행하는 것 까먹지 말기!
-   의사와 환자 생성 후 예약 만들기

![](https://blog.kakaocdn.net/dn/RIzyb/btrOnrXuCPh/23tuo5r9VUhNH6ZU9HtQ60/img.png)

-   1번 의사에게 새로운 환자 예약이 생성된다면

![](https://blog.kakaocdn.net/dn/dBiTIY/btrOreI941S/SYo2ckTXjNapdXg0gN1GT1/img.png)

---

### **2. Django ManyToManyField**

-   환자 모델에 Django ManyToManyField 작성

![](https://blog.kakaocdn.net/dn/G49xW/btrOrdQZHTe/6qsLnKWoqzsXZtfuOcpNk1/img.png)

-   마찬가지로 데이터베이스 초기화 후 Migration 진행

![](https://blog.kakaocdn.net/dn/ce7oKv/btrOnMHkatP/nRkYx0UAsxFYFcufkb6Qj1/img.png)

-   의사 1명과 환자 2명 생성

![](https://blog.kakaocdn.net/dn/bD92I4/btrOnq5oPIs/SV9oBxFLwWK0GEdKcpou7k/img.png)

-   예약 생성 (환자가 의사에게 예약)

![](https://blog.kakaocdn.net/dn/bnZ2H3/btrOre3sm7J/AGD2pFrOferNIR1lCf52Kk/img.png)

-   예약 생성 (의사가 환자를 예약)

![](https://blog.kakaocdn.net/dn/cO2DW6/btrOsbkQ5xc/KY6vXxBeMZKHewNatTmU5k/img.png)

-   예약 취소하기 (삭제)
-   기존에는 해당하는 Reservation을 찾아서 지워야 했다면, 이제는 **.remove() 사용**

![](https://blog.kakaocdn.net/dn/mLhGG/btrOscD3QXA/tELnT6YPsAZQOTynPuQex1/img.png)

-   Django는 **ManyToManyField**를 통해 **중개 테이블을 자동으로 생성**한다.

> **'related_name' argument**

-   target model이 source model을 참조할 때 사용할 manager name
-   ForeignKey()의 related_name과 동일

![](https://blog.kakaocdn.net/dn/bYcUI1/btrOreJbjMM/BCbzSoOLYQ8mD5ZlOpWND0/img.png)

-   related_name 설정 값 확인하기

![](https://blog.kakaocdn.net/dn/WXVjj/btrOrc5FxYQ/yeKAIGKPAnN6JPld6NnwU0/img.png)

> **'through' argument**

-   그렇다면 중개 모델을 직접 작성하는 경우는 없을까?
    -   중개 테이블을 수동으로 지정하려는 경우 **through** 옵션을 사용하여 사용하려는 중개 테이블을 나타내는 Django 모델을 지정할 수 있음
-   가장 일반적인 용도는 **중개 테이블에 추가 데이터를 사용**해 다대다 관계와 연결하려는 경우

-   **through 설정** 및 **Reservation Class 수정**
    -   이제는 예약 정보에 증상과 예약일이라는 추가 데이터가 생김

![](https://blog.kakaocdn.net/dn/MSRH4/btrOqN6k2WW/Krz9jWqKayElY9MYqbLUzK/img.png)

-   의사 1명과 환자 2명 생성

![](https://blog.kakaocdn.net/dn/PCsFZ/btrOsalXTUI/2cSL6PL3D7fVO4IQLHqZK0/img.png)

-   예약 생성 1

![](https://blog.kakaocdn.net/dn/buvHD4/btrOqh7VyVC/in98W26olcIUrKDbTmZAg1/img.png)

-   예약 생성 2
-    **※ through_defaults 값에 딕셔너리 타입으로 입력**

![](https://blog.kakaocdn.net/dn/qEruJ/btrOoznvtQ4/l9KykbqaeiaZhyYvEtkCuk/img.png)

-   예약 삭제

![](https://blog.kakaocdn.net/dn/bpIwky/btrOq3HQIQ9/KAkL86mNiDiE6NHQyrCAn1/img.png)

---

### **3. 정리**

-   M:N 관계로 맺어진 두 테이블에는 변화가 없음
-   Django의 ManyToManyField는 중개 테이블을 자동으로 생성함
-   Django의 ManyToManyField는 M:N 관계를 맺는 두 모델 어디에 위치해도 상관없음
    -   대신 필드 작성 위치에 따가 **참조**와 **역참조 방향**을 주의할 것
-   N:1은 완전한 종속의 관계였지만 M:N은 의사에게 진찰받는 환자, 환자를 진찰하는 의사의 두 가지 형태로 모두 표현이 가능한 것
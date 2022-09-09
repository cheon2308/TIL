orm, Modelform을 통하여 view 함수의 변화를 배워왔는데 **가장 중요!!** 한 것은 **로직, 즉 순서를 잘 지키면서 이해한 상태로 작성**하자는 것이다. 암기가 아닌 **이해가 필요한 과목**이다.

이번 글에서는 **"HTTP requests 처리에 따른 view 함수 구조 변화"**를 알아보자.

#### **목차**

1. HTTP requests

2. CREATE

3. UPDATE

---

### **1. HTPP requests**

앞에서 작성하였던 new-create, edit-update의 view 함수 역할을 잘 살펴보면 **하나의 공통점**과 **하나의 차이점**이 존재한다.

-   공통점
    -   new-create는 모두 **CREATE 로직**을 구현하기 위한 공통 목적
    -   edit-update는 모두 **UPDATE 로직**을 구현하기 위한 공통 목적
-   차이점
    -   new와 edit는 **GET 요청**에 대한 처리만을,
    -   create와 update는 **POST 요청**에 대한 처리만을 수행
-   이 공통점과 차이점을 기반으로, 하나의 VIEW 함수에서 **method에 따라 로직이 분리**되도록 변경해주자.

---

### **2. Create**

-   우선 new와 create view 함수를 합쳐주자.
-   각각의 역할은 **request.method 값을 기준**으로 나뉜다.

![](https://blog.kakaocdn.net/dn/efFcWe/btrLuBuv8W6/mqAmuac6KSBHi8L4d6KBrK/img.png)

-   method가 **POST인 경우** CREATE 함수를 수행, 아니라면 NEW 함수를 수행하도록 합쳐주었다.

이렇게 합쳐졌다면 불필요해진 new의 view 함수와 url path를 삭제해줘도 괜찮다.

![](https://blog.kakaocdn.net/dn/bIC9ma/btrLugqzMki/H317OhZEzmbJWUh9SRNVJ0/img.png)

또한, new.html 템플릿을 **create.html**로 이름 변경 및 action 속성 값을 수정해주자.

![](https://blog.kakaocdn.net/dn/I4BNT/btrLwJehaLS/g3ZSjNOXrMKjzBtDUil6K1/img.png)

그렇다면 처음 함수를 합쳐줄 때 **new.html로 지정한 템플릿 경로를 다시 create.html로 변경**해주자.

![](https://blog.kakaocdn.net/dn/bmjN9G/btrLtLqT8CO/fxq6pLpEB1aeQjfrIn5Dqk/img.png)

마지막으로 조회(index) 페이지에 있던 new 관련 링크를 수정해주면 된다.

![](https://blog.kakaocdn.net/dn/bDqpHA/btrLu1T2cUf/WnETCUvcnYk9rWG58GBFs1/img.png)

> **context의 들여 쓰기 위치**

아래와 같이 작성한다면 if form.is_valid(): 에서 **false로 평가** 받았을 때 이어질 코드가 없다.

![](https://blog.kakaocdn.net/dn/kKTD9/btrLuxFDL0U/W3HUkIvnwG3rNqfnRwnDx0/img.png)

따라서, 들여 쓰기를 처음 if-else 문에 맞춰서 작성한다면 **falsefh 평가** 받더라도, **에러 정보가 담긴 form 인스턴스가 context로 넘어갈 수 있음**

![](https://blog.kakaocdn.net/dn/EMqJC/btrLuBae7zN/xHNFL2QHe0bi3vFGwAKVy1/img.png)

---

### **3. UPDATE**

-   CREATE와 비슷하게 진행해주면 된다.
-   edit와 update의 view 함수를 합쳐준다.

![](https://blog.kakaocdn.net/dn/baVrz4/btrLu9EESYc/Lxz5nbMURlkCAUeL0KgZX0/img.png)

마찬가지로 method의 요청에 따라 어떤 로직을 수행할지 결정해준다. 또한 불필요해진 edit의 view함수와 path를 삭제!

![](https://blog.kakaocdn.net/dn/bcsg3O/btrLzn9mI2v/Kew9EG3nkMtzd7G2BBD5Pk/img.png)

삭제하였다면 이제 edit.html -> update.html 이름 변경으로 인한 관련 정보들을 수정해주면 된다.

![](https://blog.kakaocdn.net/dn/tom5O/btrLvDeieoS/tkMeSya4i082RYznjP0aMK/img.png)

![](https://blog.kakaocdn.net/dn/czB7cz/btrLuydsqWh/ayvLjLY2SBiGY0lU8KkvWK/img.png)

-   여기서 CREATE와 다른 점은 **삭제** 기능이 있기 때문에 요청이 **POST인 경우에만 삭제가 가능!** 하도록 수정해준다.

![](https://blog.kakaocdn.net/dn/PmIUC/btrLugD58x4/OHpIHhloHtNUSykfvd3kDk/img.png)
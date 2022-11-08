### **1. 개요**

-   객체는 속성(property)의 집합이며, 중괄호 내부에 key와 value 쌍으로 표현
-   key는 문자열 타입만 가능
    -   key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
-   value는 모든 타입(함수포함) 가능
-   객체 요소 접근은 점(.) 또는 대괄호([])로 가능 -> **computed property(계산된 프로퍼티)**
    -   key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
    -   식 자체를 넣는 것도 가능하다
    -   ex _ [1+4], ['안녕'+'하세요']

```
let a = 'age'

const user = {
  name = 'Mike',
  [a] : 30 // age:30
}
```

![](https://k.kakaocdn.net/dn/bMEObY/btrO2URyFYU/HsAW1f9I1tCqOh6k0YendK/img.png)

---

### **2. 객체 관련 문법**

> **객체 관련 ES6 문법 익히기**

  **1. 속성명 축약**

-   객체를 정의할 때 key와 할당하는 변수의 이름이 같으면 예시와 같이 축약 가능

![](https://k.kakaocdn.net/dn/UBjZx/btrO3EHIxoj/xkAudBXwJt5PvWlU9CXg6k/img.png)

![](https://k.kakaocdn.net/dn/CknQt/btrO3EAVotx/XOBTVra4KxQK1vhvZqLK2K/img.png)

  **2. 메서드명 축약**

-   메서드 선언 시 function 키워드 생략 가능
-   또한, 메서드 내에서는 **this** 사용하는 것을 추천

![](https://k.kakaocdn.net/dn/bxAJAk/btrO1vLtTpW/zyFTakbhJKsywChzzZCKl1/img.png)

  **3. 계산된 속성 (computed property name)**

-   객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능

![](https://k.kakaocdn.net/dn/c4YYux/btrOQGyoek7/SBEUDAeoqxCgxWrgDEVlbk/img.png)

  **4. 구조 분해 할당 (destructing assignment)**

-   배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

![](https://k.kakaocdn.net/dn/b6YgSQ/btrOFln1LPn/IIFi4EFRJnSqkQ2l9L9Xxk/img.png)

  **5. Spread syntax ( ... )**

-   배열과 마찬가지로 전개구문을 사용해 객체 내부에서 객체 전개 가능
-   얕은 복사에 활용 가능

![](https://k.kakaocdn.net/dn/cq61gH/btrO3VWKExb/MMsaklF6ozYohfNKPrBKN1/img.png)

> **JavaScriptON (JavaScript Object Notation)**

-   Key-Value 형태로 이루어진 자료 표기법
-   JavaScript의 Object와 유사한 구조를 가지고 있지만 Object는 그 자체로 타입이고, **JavaScriptON은 형식이 있는 문자열**
-   **즉, JavaScriptON을 Object로 사용하기 위해서는 변환 작업이 필요**

![](https://k.kakaocdn.net/dn/oah3d/btrODvZubFx/Nng7bTZNrfbPVR6MjH0yQk/img.png)

**※ 참고 - 배열은 객체다**

-   키와 속성들을 담고 있는 참조 타입의 객체(object)
-   배열은 인덱스를 키로 갖으며 length 프로퍼티를 갖는 특수한 객체

![](https://k.kakaocdn.net/dn/pV1Fh/btrOQDPceSD/cUkmHtbkqnljkKOplP2Cak/img.png)

---

### **3. 생성 및 삭제**

> **추가하기**

```
// 1
object.new_key_name = 'new_value_name'

// 2
object['new_key_name'] = 'new_value_name'
```

> **삭제하기**

```
delete object.key_name
```

> **in을 이용하여 property 존재하는지 확인하기**

```
const a = [1,2,3,4]

if (2 in a){
  console.log(4)
} else {
  console.log(5)
}
```

-   기본 값은 boolean형으로 True or False 반환
-   또한 아래와 같이  없는 키 값에 대해 조건을 달 경우 else 문의 결과가 나오므로 조심!!

```
const adult = {
  name: '어른'
}

if (adult.age < 20) {
  console.log(3)
} else {
  console.log(5)
}
```

---

### **4. 객체 메서드**

> **Object.assign()**

-   **객체 복제**
-   클론 유저를 만들어서 복제 x
-   네모 안의 유저에는 **~~객체가 저장된 것이 아닌~~,** 객체가 저장되어 있는 **메모리 주소****인 객체에 대한 참조값**이 들어있다 (얕은 복사)

![](https://k.kakaocdn.net/dn/czW8sZ/btrPL5chVEj/JeXp0Zk9SdhGja7fkB9S91/img.png)

-   따라서 깊은 복사를 위해서는 **assign 사용**
-   **초기값 {}**에 **user가 복사된다.**
-   빈 값이 아닌 **없는 값이라면 새로 생성**

![](https://k.kakaocdn.net/dn/d9nELw/btrPJFyR0GK/OdXBFyM3jKESoLmkaAQ6K1/img.png)

-   키가 같다면 덮어 씌운다.

![](https://k.kakaocdn.net/dn/TBlYX/btrPIXUGE0o/8SYiJmg8TsUPo5sOCiKJJK/img.png)

-   여러 개 병합 가능

![](https://k.kakaocdn.net/dn/bY03WM/btrPISeFLtI/fH7kVP6Sqlx37x7qnbIeM1/img.png)

> **Object.keys(), Object.values()**

-   파이썬과 마찬가지로 키 값과 밸류 값 반환

> **Object.entries(), Object.fromEntries()**

-   **Object.entries()** : 키/값 배열로 반환

![](https://k.kakaocdn.net/dn/LEQXy/btrPK0vw4JY/2MKkNm9RVxrNyV06NQla6k/img.png)

-   **Object.fromEntries() :** 키/값 배열을 객체로 반환

![](https://k.kakaocdn.net/dn/caXljM/btrPK4EIeLk/A0myBkNS8CII8MBu8SKOVK/img.png)
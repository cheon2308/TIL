### **1. 배열**

> **개요**

- JavaScript의 데이터 타입 중 참조 타입(reference)에 해당 하는 타입은 array와 object이며, 객체라고 말함
- 객체는 속성들의 모음(collection)
  - (참고) 객체 안쪽의 속성들은 메모리에 할당 되어있고 해당 객체는 메모리의 시작 주소 값을 가리키고 있는 형태

> **배열(Array)**

- 키와 속성들을 담고 있는 참조 타입의 **객체(object)**
- 배열은 **문자 뿐만 아니라 숫자, 객체, 함수 등**도 포함할 수 있음
- 순서를 보장하는 특징이 있음
- 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 **array.length** 형태로 접근 가능
  - (참고) 배열의 마지막 원소는 array.length -1로 접근

![](https://k.kakaocdn.net/dn/M73Ey/btrPIEzSFyj/Gd1khVRyAItAioMo0ZHoH1/img.png)

![](https://k.kakaocdn.net/dn/CxKnp/btrOQBjr5MT/ZACGsHZRo1iZBkMKFpZhik/img.png)

---

### **2. 배열 메서드 기초**

![](https://k.kakaocdn.net/dn/15E2D/btrOQz0fXYP/M6IdBHGmMdrsScVpWUnet0/img.png)

> **array.reverse()**

- 원본 배열 요소들의 순서를 반대로 정렬

![](https://k.kakaocdn.net/dn/C2xRr/btrO3VbfWvs/D6aTgSHlxhGxjM4IGGhKCK/img.png)

> **array.push(), array.pop()**

- 배열의 가장 뒤에 요소 추가 및 제거

![](https://k.kakaocdn.net/dn/bRtmeb/btrOQEgbiAt/UEdAyg59yn640oAW9dcRN0/img.png)

> **array.includes(value)**

- 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

![](https://k.kakaocdn.net/dn/byr5HL/btrO36p25Bq/Htuxxpv0wibZ7Hx8kLv8n0/img.png)

> **array.indexOf(value)**

- 배열에 특정 값이 존재하는지 확인 후 가장 첫 번째로 찾은 요소의 인덱스 반환
- 만약 해당 값이 없을 경우 -1 반환

![](https://k.kakaocdn.net/dn/lXyYO/btrO4ucU7se/QeCIO9kIr2aIZEABRrlToK/img.png)

> **array.join([separator])**

- 배열의 모든 요소를 연결하여 반환
- separator(구분자)는 선택적으로 지정 가능하며, 생략 시 쉼표를 기본 값으로 사용

![](https://k.kakaocdn.net/dn/crY0qJ/btrO3EHCe9B/nlTJnCnfv0qOvCy7vMKlOK/img.png)

---

### **3. 배열 메서드 심화**

> **Array Helper Methods**

- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 **callback 함수** 를 받는 것이 특징

**※ callback 함수 : 어떤 함수의 내부에서 실행될 목적으로 인자로 넘겨받는 함수**

![](https://k.kakaocdn.net/dn/bf4ymk/btrOQqI1CeE/ZiM07ScMPRthoBkWh8shU1/img.png)

**※ 참고 - Django로 보는 콜백함수 예시**

![](https://k.kakaocdn.net/dn/FOrPo/btrO2WPi3Eu/15hpGcwfppnruWGQKuuKQ0/img.png)

> **forEach**

- array.forEach(callback(element, index, array)
- 인자로 주어지는 함수(콜백 함수)를 배열의 각 요소에 대해 한 번씩 실행
  - 콜백 함수는 3가지 매개변수로 구성
    1.  **element:** 배열의 요소
    2.  **index:** 배열 요소의 인덱스
    3.  **array:** 배열 자체
- **반환 값(return)** 없음

![](https://k.kakaocdn.net/dn/dhI1gO/btrOQteEQLh/k1yo0LHkYtFu2a5eVAAIDk/img.png)

![](https://k.kakaocdn.net/dn/LaKF8/btrO3FNh5xS/j2ghHbz1lGm8NA6vdYHHX0/img.png)

> **map**

- array.map(callback(element, index, array)
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환**
- 기존 배열 전체를 다른 형태로 바꿀 때 유용

![](https://k.kakaocdn.net/dn/bTO9hW/btrOQBcMqhm/I7j6TKC4JRkZk7FWGL7ry0/img.png)

![](https://k.kakaocdn.net/dn/YuwCw/btrO1v5HZtG/U8qxF6BT5QQUH1zzPLOkvk/img.png)

> **filter**

- array.filter(callback(element, index, array)
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- **콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열 반환**
- 기존 배열의 요소들을 필터링할 때 유용

![](https://k.kakaocdn.net/dn/Ro9xN/btrO4glGAyD/WhEYKNsvlElujCqou4RCcK/img.png)

![](https://k.kakaocdn.net/dn/GtH0g/btrOC5s8qto/KwNoL6RKHI3O8RNsww9Dr0/img.png)

> **reduce**

- array.reduce(callback(acc, element, index, array) => initialValue)
- 인자로 주어지는 함수를 각 배열의 각 요소에 대해 한 번씩 실행해서 하나의 결과 값을 반환
- 즉, 배열을 하나의 값으로 계산하는 동작이 필요할 때 사용(총합, 평균 등)
- map, filter 등 여러 배열 메서드 동작을 대부분 대체할 수 있음

![](https://k.kakaocdn.net/dn/dfGN58/btrO3EVbNjo/8zCaQKW4RKbrGnts5aIUm0/img.png)

- reduce 메서드의 주요 매개변수
  - **acc**
    - 이전 callback 함수의 반환 값이 누적되는 변수
  - **initialValue(optional)**
    - 최초 callback 함수 호출 시 acc에 할당되는 값, default 값은 배열의 첫 번째 값
- reduce의 첫 번째 매개변수인 콜백함수의 첫 번재 매개변수('acc')는 누적된 값(전 단계 까지의 결과)
- reduce의 두 번째 매개변수인 'initialValue'는 누적될 값의 초기값, 지정하지 않을 시 첫 번째 요소의 값이 됨

**※ 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생**

![](https://k.kakaocdn.net/dn/bNkRN1/btrO3UDs58j/zmoKfNESmShklkAsemTWX1/img.png)

예시

- 동작 방식

![](https://k.kakaocdn.net/dn/l2dSE/btrO4pbAx9R/TPylhCfAC4uOF2kDJsPGG0/img.png)

> **find**

- array.find(callback(element, index, array)
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
- 찾는 값이 배열에 없으면 undefined 반환

![](https://k.kakaocdn.net/dn/NwnkO/btrOQrVuGPi/1Wpv6aJIFVug2jkhc6gGK0/img.png)

> **some**

- array.some(callback(element, index, array)
- 배열의 **요소 중 하나라도** 주어진 판별 함수를 통과하면 참을 반환
- 모든 요소가 통과하지 못하면 거짓 반환
- 빈 배열은 항상 false 반환

![](https://k.kakaocdn.net/dn/bVTEvo/btrOQEAxEr0/VKaCLe99RQ7nYVi5KGq6Uk/img.png)

> **every**

- array.every(callback(element, index, array)
- 배열의 **모든 요소가** 주어진 함수를 통과하면 참을 반환
- 하나의 요소라도 통과하지 못하면 거짓 반환
- 빈 배열은 항상 true 반환

![](https://k.kakaocdn.net/dn/bvmR67/btrO4g644qB/RA5VvVqgYR3LgZa77KT3HK/img.png)

> **배열 순회 비교**

![](https://k.kakaocdn.net/dn/BeXyg/btrOQnr1Pyc/zyAk6MKK9rXNM3zWamofl1/img.png)

![](https://k.kakaocdn.net/dn/RZofd/btrO3EHF7hN/wYOv318MTDOoi2baIr8yZ1/img.png)

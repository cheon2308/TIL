# 0720

# 함수의 결과값

> - Void function
>   
>   - 명시적인 return 값이 없는 경우, None을 반환하고 종료
> 
> - Value returning function
>   
>   - 함수 실행 후, return문을 통해 값 반환
>   
>   - return을 하게 되면, 값 반환 후 함수가 바로 종료
> 
> - print는 값을 출력하지만 반환하지는 않는다 !
>   
>   - **print를 사용하면 호출될 때마다 값이 출력**
>   
>   - **데이터 처리를 위해서는 return 사용**

###### 두 개 이상의 값 반환

> 반환 값으로 튜플 사용
> 
> ```python
> return x -y, x*y
> function(4, 5)
> ```

> 또는 리스트와 같은 컨테이너 활용

###### Argument

> - 함수 호출 시 함수의 parameter를 통해 전달되는 값
> 
> - 소괄호 안에 할당 func_name(argument)
>   
>   - 필수 : 반드시 ! 존재
>   
>   - 선택 : 값을 전달하지 않는 경우 기본값 전달
> 
> **1. positional Arguments**
> 
> **2. Keyworkd Arguments**
> 
>     - 2번 다음에 1번을 활용 x
> 
> ```python
> add(x=2, y=5)
> add(2, y=5)
> add(x=2, 5) -> Error발생
> ```

> **3. Default Arguments Values**
> 
> - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
> 
> ```python
> def add(x, y=0)
> ```

###### 가변 인자 (*args)

> - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
> 
> - 몇 개의 positional Argument를 받을지 모르는 함수를 정의할 때 유용

###### 패킹 / 언패킹

> - 여러 개의 데이터를 묶어서 변수에 할당 -> 패킹
> 
> - 시퀸스 속의 요소들을 여러 개의 변수에 나누어 할당 -> 언패킹
>   
>   - 언패킹시 *를 왼쪽에 붙이면, 할당하고 남은 요소 담음

###### 가변 키워드 인자(**kwargs)

> - 몇 개의 키워드 인자를 받을지 모르는 함수를 정의할 때 유용
> 
> - 딕셔너리로 묶여 처리 되며, parameter에 **를 붙여 표현

##### 가변 인자와 가변 키워드 인자 동시 사용 가능

```python
def print_family_name(*parents, **pets)
```

---

# Python의 범위(Scope)

> - 함수는 코드 내부에 local scope를 생성하며
>   그 외의 공간인 global scope로 구분
> 
> - variable도 마찬가지

#### 변수 수명주기(lifecycle)

> - 변수는 각자의 수명주기 존재
>   
>   - built-in scope
>     
>     - 파이썬 실행 이후 영원히 유지
>   
>   - global scope
>     
>     - 모듈 호출 시점 혹은 인터프리터 끝날 때까지 유지
>   
>   - local scope
>     
>     - 함수가 호출될 때 생성되고, 종료될 때 소멸

## 이름 검색 규칙(Name Resolution)

> - **LEGB Rule에 따라 찾아나간다.**
>   
>   1. Local scope : 현재 작업중 범위
>   
>   2. Enclosed scope : 지역 범위 한 단계 위 범위
>   
>   3. Global scope : 최상단에 위치한 범위
>   
>   4. Built-in scope : 모든 것을 담고 있는 범위 (정의하지 않고 사용할 수 있는 모든 것) - print
> 
> . 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없다 !
> 
> ```python
> a = 0
> b = 1
> def enclosed():
>     a=10
>     c=3
>     def local(c):
>         print(a,b,c) # 10 1 300
>     local(300)
>     print(a,b,c) # 10 1 3
> enclosed()
> print(a,b) # 0 1
> ```

###### global 문

> - 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이
>   global variable임을 나타냄
>   
>   - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
>   
>   - global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
> 
> ```python
> a = 10
> def func1():
>     global a
>     a = 3
> print(a) #10
> func1()
> print(a) #3
> 
> #Local scope에서 global 변수 값의 변경
> #global 키워드를 사용하지 않으면, local scope에 a변수 생
> ```

##### nonlocal

> - global 제외 가장 가까운 scope의 변수를 연결
> 
> - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal앞에 등장할 수 없음
> 
> - nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
> 
> - **nonlocal의 경우 이미 존재하는 이름과의 연결만 가능함**
> 
> - ```python
>   x = 0
>   def func1():
>       x = 1
>       def func2()
>           nonlocal x
>           x = 2
>       func2()
>       print(x) #2
>   
>   func1()
>   print(x) #0
>   ```

## 주의사항!

> - 기본적으로 local scope에 생성되며, 종료시 사라짐
>   
>   - 단, 함수 내에서 필요한 상위 scope 변수는 argument로 넘겨서 활용
> 
> - 상위 scope에 있는 변수 수정하고 싶다면, global, nonlocal 키워드 활용가능
>   
>   - 단, 코드 복잡해지고 예기치 못한 오류
>   
>   - **함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴 값 사용하는 것을 추천**

---

# 함수의 응용

**1. map(function, iterable)**

- 순회 가능한 데이터구조의 모든 요소에 함수적용하고, 그 결과를
  map object로 반환

- 알고리즘 문제 풀이시 input 값들을 숫자로 바로 활용하고 싶을 때
  
  ```python
  n, m = (int, input().split())
  
  reseult = map(str, numbers)
  ```

**2. filter(function, iterable)**

- 순회 가능한 데이터구조의 모든 요소에 함수적용하고, 그 결과가 True인 것들을 filter object로 반환

```python
def odd(n):

result = filter(odd, numbers)
```

**3.zip(*iterables)***

- 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환

```python
girls = ['d'. 'f']
boys = ['a','b']
pair = zip(girls, boys)
```

**4.lambda[parameter]:표현식**

- 익명함수

- return문 및 간편 조건문 외 조건문이나 반복문 가질 수 x

- 장점
  
  - 함수를 정의해 사용하는 것보다 간결
  
  - def를 사용할 수 없는 곳에서도 사용가능

```python
#삼각형 넓이 - def
def area(b,h)
    return o.5 * b* h
#삼각형 - 람다
area = lamda b, h : 0.5 *b*h
```

**5.재귀 함수**

- 자기 자신을 호출

- 알고리즘 설계 및 구현에서 유용하게 활용

- 변수의 사용 줄어들며, 코드 가독성 높아짐

- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성

```python
#factorial
n!
n*(n-1)!


f(3) = 3*f(2)
f(2) = 2*f(1)
f(1) = 1 -> base case

def factorial(n):
    if n ==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
#for문으로 구현
def factorial(n):
    result = 1
    while n> 1:
        result *= n
        n -= 1
    return result
    
```

- **주의사항** 
  
  - 메모리 스택이 넘치게 되면 프로그램이 동작하지 않게 됨
  
  - 파이썬에서는 최대 재귀 깊이가 1,0000번으로, 호출 횟수가 이를 넘어가게 되면 Recursion Eroor 발생

---

# 모듈

> - 다양한 기능을 하나의 파일로
> 
> - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 거

# 패키지

> - 다양한 모듈을 하나의 묶음으로
> 
> - 활용공간 = 가상환경
> 
> - 패키지 안에는 또 다른 서브 모듈

# 라이브러리

> 다양한 패키지를 하나의 묶음으로

# PIP

> 이것들을 관리하는 관리자

### 불러오기 !

```python
import module
from module import var, funcion, Class
from module import *

from package import module
from package.module import var, function, Class
```

#### 파이썬 기본 설치된 모듈과 내장함수

- [내장 모듈](https://docs.python.org/ko/3/library/index.html)

- 설치
  
  ```python
  $ pip install Somepackage
  $ pip install Somepackage == 1.0.5
  $ pip install Somepackage >=1.0.4'
  ```

- 삭제
  
  ```python
  $ pip uninstall Somepackage
  ```

- 그 외 명령어
  
  ```python
  # 리스트
  $ pip list
  
  #정보
  $ pip show Somepackage 
  
  #관리
  $ pip freeze> requirements.txt
  $ pip install -r requirements.txt
  ```

## 가상환경

> 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우
> 모두 pip를 통해 설치를 해야함
> 
> 버전이 상이 할 수 있어 가상환경을 만들어 프로젝트별로 독립적 패키지 관리 가능
> 
> ```python
> python -m venv venv #가상환경 이름
> source - venv/Scripts/activate
> # 아무것도 없는 상태에서
> pip list
> pip freeze > requir
> pip install requests
> ```

-- -

# 0722 PJT

# Dictionary

```python
print(stock['price']) # 해당 키를 받아오다가 키 값 없으면 오류

print(stock.get['price']) # 해당 키를 받아오다가 키 값 없으면 None값 반
print(stock.get['price', '비상장 주식입니다.']) # get 사용시 default값 설정 해줄 수 있음 !! 
```

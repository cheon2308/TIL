
### **1. 간단한 예제로 입력 받은 문자열 그대로 출력하기**

```cpp
#include <bits/stdc++.h> // (1)
using namespce std; // (2)
string a; // (3)
int main(){
	cin >> a; // (4)
    cout << a << "\n" // (5)
    return 0; // (6)
}
```

-   작성 후 F11 또는 컴파일 아이콘 클릭 후 실행
-   입력받은 그대로 출력되는 프로그램

![](https://blog.kakaocdn.net/dn/cbNPMv/btrZQc1mjfn/uc7Pjjsn1nqKlkE7VEZE7k/img.png)

> **주석 설명**

1.  **헤더파일을 include 시킨다.**  
    -   **bits/stdc++.h**는 C++의 모든 표준 라이브러리가 포함된 헤더파일
    -   이를 include 지시문을 통해 프로그램에 포함시킨다는 의미
2.  **std**라는 **네임스페이스**(namespce)를 사용한다는 뜻  
    -   **네임스페이스**란 많은 라이브러리를 불러서 사용하다보면 **변수명 중복이 발생**할 수 있는데 이를 방지하기 위해 **변수명에 범위를 걸어놓는 것**을 의미
    -   cin이나 cout 등을 사용할 때 원래는 std라는 네임스페이스를 통해 **std::cin** 이렇게 호출을 해야 하는데 std를 기본으로 설정해서 cin, cout 으로 호출할 수 있게 한다.
3.  **문자열 변수 a를 선언**
    -   **<타입> <변수명>** 이렇게 선언
    -   string이라는 타입을 가진 a라는 변수
    -   ex) string a = "큰 돌" 이라고 선언한다면
    -   a를 **lvalue**라고 하며 큰돌을 **rvalue**라고 한다.
        -   **lvalue**는 추후 다시 사용될 수 있는 변수
        -   **rvalue**는 한번쓰고 다시 사용되지 않은 변수를 의미
4.  **변수 a를 입력받는다**
    -   대표적으로 cin, scanf 
5.  **변수 a를 출력한다.**
    -   대표적으로 cout과 printf
6.  **main함수를 종료시키는 return 0** 
    -   프로세스를 정상적으로 마무리한다는 의미 (process exit call success)
    -   또한 C++은 cpp 파일당 하나의 main 함수만을 만들 수 있습니다.
    -   하나의 main 함수를 기반으로 구성해야 한다.

---

### **2. typedef**

-   타입의 이름을 새로이 별칭으로 정의하고 실제 타입이름 대신 사용할 수 있는 것
-   이를 통해 C++에서 이미 정의된 타입 또는 사용자가 정의한 타입(struct 또는 class)보다 더 짧거나 의미있는 이름을 지을 수 있음.

```
typedef <타입> <별칭>
```

```cpp
#include<bits/stdc++.h>
using namespace std;
typedef int i;
int main(){
	i a = 1;
    cout << a << '\n';
    return 0;
}
```

---

### **3. define**

-   상수, 매크로를 정의할 수 있음

```
#define <이름> <값>
```

```cpp
#include<bits/stdc++.h>
using namespace std;
#define PI 3.14159
#define loop(x,n) for(int x = 0; x < n; x++)

int main(){
	cout << PI << '\n';
    int sum = 0;
    loop(i, 10){
    	sum += i;
    }
    cout << sum << '\n';
    return 0;
}
```

---

### **4. STL**

-   C++은 **STL(Standard Template Library)**을 제공하며 이는 자료구조, 함수 등을 제공하는 라이브러리를 뜻한다.
-   알고리즘, 컨테이너, 이터레이터, 펑터 이렇게 4가지 제공

> **알고리즘**

-   정렬, 탐색 등에 관한 함수
-   sort()가 대표적

> **컨테이너**

-   클라우드 서비스의 컨테이너도 있고 물건을 많이 담을 수 있는 컨테이너 박스
-   여기서의 컨테이너는 C++에서 제공하는 자료구조를 의미함
-   **시퀀스 컨테이너**, **연관 컨테이너**, **정렬되지 않은 연관 컨테이너**, **컨테이너 어댑터**가 있음 

> 1. **시퀀스 컨테이너(sequence container)  
> **  
> - 데이터를 단순히 저장해 놓는 자료구조를 뜻하며  
> - **array, vector, deque, forward_list, list  
>   


> **2. **연관 컨테이너(associative** **container)  
>   
> **- 자료가 저장됨에 따라 자동정렬되는 자료구조를 말함  
> - 중복키가 가능한 것은 이름에 **multi**가 붙음  
> - **set, map, multiset, multimap  


> **3. **정렬되지 않은 연관 컨테이너(unordered associative container)**  
>   
> - 자료가 저장됨에 따라 자동정렬이 되지 않는 자료구조  
  - **unordered_set, unordered_map, unordered_multiset, unordered_multimap**  


> 4. **컨테이너 어댑터(container adapter)**  
>   
> - 시퀀스 컨테이너를 이용해 만든 자료구조를 뜻  
> - **stack, queue**는 **deque**로 만들어져 있으며, **priority_queue**는 **vector**을 이용해 **힙** **자료구조**로 만든다.  
>   


> **나중에 자세히 공부할 것!**    

> **이터레이터 및 펑터**

-   펑터 -> 함수 호출 연산자를 오버로드하는 클래스의 인스턴스
-   이터레이터 -> 나중에 학습
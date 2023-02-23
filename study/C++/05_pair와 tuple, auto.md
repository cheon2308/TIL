
### **1. pair와 tuple**

-   pair와 tuple은 **타입이나 자료구조는 xxxx.**
-   C++에서 제공하는 **utility 라이브러리 헤더의 템플릿 클래스**이며 자주 사용된다.

> **pair**

-   first와 second라는 멤버변수를 가지는 클래스
-   두가지 값을 담아야 할 때 사용
-   **{a, b}** 또는 **make_pair(a, b)**로 만들 수 있음

> **tuple**

-   세가지 이상의 값을 담을 때 사용

**tie**를 이용하여 pair나 tuple로부터 값을 끄집어 낸다.

```cpp
#include<bits/stdc++.h>
using namespace std;
pair<int, int> pi;
tuple<int, int, int> tl;
int a, b, c;
int main(){
    pi = {1, 2};
    tl = make_tuple(1, 2, 3);
    tie(a, b) = pi;
    cout << a << " : " << b << "\n";
    tie(a, b, c) = tl;
    cout << a << " : " << b << " : "<< c << "\n";
    return 0;
}
```

아래는 tie를 사용하지 않은 코드

```cpp
#include<bits/stdc++.h>
using namespace std;
pair<int, int> pi;
tuple<int, int, int> ti;
int a, b, c;
int main(){
    pi = {1, 2};
    a = pi.first;
    b = pi.second;
    cout << a << " : " << b << "\n";
    ti = make_tuple(1, 2, 3);
    a = get<0>(ti);
    b = get<1>(ti);
    c = get<2>(ti);
    cout << a << " : " << b << " : "<< c << "\n";
    return 0;
}
/*
1 : 2
1 : 2 : 3
*/
```

-   일일히 get<0>..과 같이 꺼내는 것은 별로라고 생각되어 보통 3가지 이상의 멤버변수가 필요하다면 tuple보다는 **struct**를 사용한다.

---

### **2. auto**

-   **타입추론**을 해 결정되는 타입
-   아래 코드에서는 b라는 변수를 auto로 선언했는데 **rvalue**가 1인 것을 통해 자동적으로 int 타입의 변수를 선언했듯이 쓸 수 있는 것을 볼 수 있음

```cpp
#include <bits/stdc++.h>
using namespace std;
int a = 1;
auto b = 1;
int main(){
    cout << b << '\n';
}
/*
1
*/
```

-   **auto** 타입은 **복잡하고 긴 타입의 변수명을 대신하는 간단한 방법**
-   아래 코드처럼 pair<int, int> it가 아닌 auto it로 조금 더 짧게 선언되는 것을 볼 수 있음

```cpp
#include<bits/stdc++.h>
using namespace std;
int main(){
    vector<pair<int, int>> v;
    for(int i = 1; i <= 5; i++){
        v.push_back({i, i});
    }
    for(auto it : v){
        cout << it.first << " : " << it.second << '\n';
    }
     for(pair<int, int> it : v){
        cout << it.first << " : " << it.second << '\n';
    }
    return 0;    
}


/*
1 : 1
2 : 2
3 : 3
4 : 4
5 : 5
1 : 1
2 : 2
3 : 3
4 : 4
5 : 5
*/
```

c++을 공부하며 파이썬과 가장 다른 점은 **엄격한 타입시스템**으로 인해 매번 **타입(type)**을 설정해줘야 한다는 점이다.

또한 매개변수의 수나 타입 등에 따라 함수를 다르게 인식한다. 예를 들어 **func(int a, int b)**와 **func(int a)**는 엄연하게 다른 함수로 인식된다.

### **# 타입**

-   아래는 알고리즘에서 자주 나오는 타입 8개이다.

```cpp
void, char, string, bool, int, long long, double, unsigned long long
```

---

#### **1. void : 리턴하는 값이 없다.****

```cpp
#include <bits/stdc++.h>
using namespace std;
int ret = 1;
void a(){
    ret = 2;
    cout << ret << "\n";
    return;
}
int main(){
    a();
    return 0;
}
```

-   a라는 함수가 ret을 바꾸고 아무것도 리턴하지 않음을 보여준다.
-   이렇게 아무것도 리턴하지 않는 함수에는 **void**로 선언한다.

함수를 선언할 때 어떤 타입을 반환하는지 명시해주어야 하고 이를 return하는 값과 맞춰주어야 하는데 예를 들어 아무것도 반환하지 않는 void가 아닌 double 타입을 반환하는 함수는 어떻게 정의할 수 있을까?

-   아래 코드처럼 a()라는 함수는 double 타입으로 정의된 것을 볼 수 있다. 1.23333이라는 double타입의 변수를 return하는 것을 볼 수 있다.

```cpp
#include <bits/stdc++.h>
using namespace std;
double a(){
	return 1.2333;
}
int main(){
    double ret = a();
    cout << ret << "\n";
    return 0;
}
```

-   또한 함수를 선언할 때는 항상 호출되는 **위쪽 부분에 선언**을 해야 한다.
-   앞의 코드를 보면 a()라는 함수를 위에 선언했고 main에서 a()라는 함수를 호출하는 것을 볼 수 있다.
-   다른 방법으로는 아래와 같이 **타입과 인자만 선언**을 해 놓고 **아래쪽에 함수를 정의하는 식**으로 **선언부**와 **정의부**를 나눠서 함수를 설정하는 방법 또한 있다. (비추천)
    -   아래와 같이하게 되면 2번을 해야하므로 그냥 위에다 선언과 정의를 한꺼번에 하자!

```
#include <bits/stdc++.h>
using namespace std;
double a();
int main(){
    double ret = a();
    cout << ret << "\n";
    return 0;
}
double a(){
    return 1.2333;
}
```



#### **2. char : 문자**

-   작은 따옴표 '' 이렇게 선언해야 하며 **1바이트의 크기**를 가진다.
-   아래와 같이 a를 선언하고 a를 출력하는데 **한 문자**만 들어간다.

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    char a = 'a';
    cout << a << "\n";
    return 0;
}
```

-   char을 리턴하기 위해서는 위에서 본 것과 같이 함수로 정의해주면 된다.

```cpp
#include <bits/stdc++.h>
using namespace std;
char b(){
    char a = 'a';
    return a;
}
int main(){
    char a = b();
    cout << a << "\n";
    return 0;
}
```

---

#### **3. string : 문자열**

-   앞서 배운 char을 아래 코드처럼 배열로 선언하거나 그냥 string으로 선언해 여러개의 문자모음이자 문자 배열인 문자열을 선언할 수 있다.

```cpp
char s[10];
string a;
```



-   아래 코드에서는 배열처럼 a[0]로 접근하거나 통째로 a를 출력하는 것을 볼수 있다.

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string a = "나는야";
    cout << a[0] << "\n";
    cout << a[0] << a[1] << a[2] << '\n';
    cout << a << "\n";
    string b = "abc";
    cout << b[0] << "\n";
    cout << b << "\n";
    return 0;
}
/*
?
나
나는야
a
abc
*/
```

-   출력결과를 확인해보면 한글로 선언한 a의 경우 a[0]을 출력했을 때 이상한 문자가 나타난 것을 볼 수 있다.
-   문자열을 선언하고 **a[0], a[1] 이렇게 접근**한다는 의미는 **1바이트씩 출력**한다는 것을 의미하는데, 영어는 한 글자당 1바이트지만 한글은 힌 글자당 3바이트이다.

**string method**

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
	string a = "love is";
    a += " pain!";
    a.pop_back();
    cout << a << " : " << a.size() << "\n";
    cout << char(* a.begin()) << '\n';
    cout << char(* (a.end() - 1)) << '\n';
    //string& insert (size_t pos, const string& str);
    a.insert(0, "test ");
    cout << a << " : " << a.size() << "\n";
    // string& erase (size_t pos = 0, size_t len=npos);
    a.erase(0,5);
    cout << a << " : " << a.size() << "\n";
    // size_t find (const string& str, size_t pos = 0);
    auto it = a.find("love");
    if (it != string::npos){
		cout << "포함되어 있다." << '\n';
    }
    cout << it << '\n';
    cout << string::npos << '\n';
    // string substr (size_t pos = 0, size_t len = npos) const;
    cout << a.substr(5, 2) << '\n';
    return 0;
}
/*
love is pain : 12
l
n
test love is pain : 17
love is pain : 12
포함되어 있다.
0
18446744073709551615
is
*/
}
```

> **+=** 

-   메서드는 아니며 문자열에서 문자열을 더할 때 보통 += 써서 문자열 또는 문자를 더한다.
-   push_back()라는 메서드가 있지만 이는 문자 밖에 더하지 못해 보통 += 를 사용

> **begin()**

-   문자열의 첫번째 요소를 가리키는 **이터레이터를 반환**한다.

> **end()**

-   문자열의 마지막 요소 그 다음을 가리키는 이터레이터를 반환
-   참고로 **begin()**과 **end()**는 자료구조인 **vector, Array, 연결리스트, 맵, 셋**에서도 존재하며 똑같은 의미를 지닌다.

> **size()**

-   문자열의 사이즈를 반환
-   **O()**의 **시간복잡도**

> **insert(위치, 문자열)**

-   특정위치에 문자열을 삽입
-   **O(n)의** **시간복잡도**

> **erase(위치, 크기)**

-   특정위치에 크기만큼 문자열을 지운다.
-   **O(n)의 시간복잡도**

> **pop_back()**

-   문자열 끝을 지운다.
-   **O(1)의 시간복잡도**

> **find(문자열)**

-   특정 문자열을 찾아 위치를 반환
-   만약 해당 문자열을 못 찾을 경우 **string::npos**를 반환하며 
    -   string::npos는 **size_t 타입**의 **최대값**을 의미
    -   size_t 타입의 최대값은 OS에 따라 달라지며 64비트 운영체제라면 **64비트 부호가 없는 최대 정수 -> 18446744073709551615**
    -   32비트 운영체제라면 **32비트 부호가 ㅇ벗는 최대 정수값**을 가진다.
    
-   **O(n)****의 시간복잡도**

> **substr(위치, 크기)**

-   특정 위치에서 크기만큼의 문자열을 추출
-   **O(n)의 시간복잡도**

> **아스키코드와 문자열**

-   만약 숫자로 된 문자에서 ++ 증감연산자를 통해 1을 더해준다면 **아스키코드에서 +1한 값**이 된다.

```cpp
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    string s= "123";
    s[0]++;
    cout << s << "\n"; // 223
    return 0;
}
```

-   위 코드를 보면 123에서 s[0]에 1을 더해 223이 되었는데 이는 아스키코드 **49에서 1을 더한 값이 50이 가리키는 값**이 **2**이기 때문에 **123에서 223이 되는 것**
-   즉, 문자열에서 + 하는 연산은 **아스키코드**를 기반으로 수행
-   문자열을 이루는 문자는 **아스키(ASCII)** **값 (0에서 127 사이의 정수)**로 저장되어 구현
-   예를 들어 'A'의 ASCII 값은 65인데 이것이 의미하는 바는 문자 변수에 'A'를 할당하면 'A' 자체가 아니라 **65라는 숫자가 해당 변수에 저장**된다는 것.

**아스키 코드**는 1964년 미국 ANSI에서 표준화한 정보교환용 7비트 부호체계이며 000(0x00)부터 127(0x7F)까지 총 128개의 부호가 사용된다.

-   1바이트를 구성하는 8비트 중에서 7비트만 쓰도록 제정된 이뉴는, 나머지 1비트를 **통신 에러 검출**을 위한 용도로 비워두었기 때문
-   이는 영문 키보드로 입력할 수 있는 모든 기호들이 할당되어 있는 **가장 기본적인 부호 체계**
-   아래 표 모두 외울 필요는 없지만 **97 : a / 65 : A 정도는 외우자**
-   또한 127까지의 숫자를 지원하기 때문에 **127이 넘어가는 숫자를 만들면 에러**가 발생하니 조심

![](https://blog.kakaocdn.net/dn/bgH2mM/btr0hpTcS5g/4VKtSPcyMGYKumT9UKb4Tk/img.png)

![](https://blog.kakaocdn.net/dn/KFPIh/btr0glqaeJ3/xVPBD1TSkjOKkUY1uZkStk/img.png)

-   (int)’a’를 통해 문자 char을 정수 int로 변환할 수 있는데 이를 하게 되면 다음 코드처럼 97로 변환된다.

```cpp
#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false); cin.tie(NULL);
    cout.tie(NULL);
    char a = 'a';
    cout << (int)a << '\n';
    return 0;
}
// 97
```

> **reverse()**

-   문자열 string은 reverse()라는 메서드를 지원하지 않는다.
-   문자열을 거꾸로 뒤집고 싶다면 **STL**에서 지원하는 함수인 **reverse()**를 쓰면 된다.

```cpp
template <class BidirectionalIterator> void reverse (BidirectionalIterator
first, BidirectionalIterator last);
```

-   reverse() 함수는 void 타입으로 아무것도 반환하지 않는다. 그리고 **원본 문자열도 바꿔버린다.**

아래 코드처럼 구축이 가능하며, **a.begin() + 3**처럼 시작위치를 바꿔 뒤집고 싶은 부분만을 바꿀 수 있다.

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string a = "It's hard to have a sore leg";
    reverse(a.begin(), a.end());
    cout << a << '\n';
    reverse(a.begin(), a.end());
    cout << a << '\n';
    reverse(a.begin() + 3, a.end());
    cout << a << '\n';
    return 0;
}
/*
gel eros a evah ot drah s'tI
It's hard to have a sore leg
It'gel eros a evah ot drah s
*/
```

> **split()**

-   다른 프로그래밍 언어에서도 문자열을 특정 문자열을 기준으로 쪼개어서 배열화시키는 함수라는 의미로 사용되는데 C++에서는 **STL에서 split()** 함수를 지원하지 xxxxxxx
-   따라서, 만들어서 사용해야 한다.
-   보통 아래와 같이 구현하며 **O(n)의 시간 복잡도**

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<string> split(string input, string delimiter) {
    vector<string> ret;
    long long pos = 0;
    string token = "";
    while ((pos = input.find(delimiter)) != string::npos) {
    	token = input.substr(0, pos);
        ret.push_back(token);
        input.erase(0, pos + delimiter.length());
    }
    ret.push_back(input);
    return ret;
}

int main(){
    string s = "안녕하세요 저는 취준생 입니다 감사합니다!", d = " ";
    vector<string> a = split(s, d);
    for(string b : a) cout << b << "\n";
}

/*
안녕하세요
저는
취준생
입니다
감사합니다!
*/
```

-   복잡해보이지만 아래 코드 3줄만 외우면 된다.

```cpp
while ((pos = input.find(delimiter)) != string::npos) {
    token = input.substr(0,pos);
    ret.push_back(token);
    input.erase(0, pos + delimiter.length());
}
```

**input**에서 **delimiter**를 찾는데 못 찾을 때까지는 이 루프는 반복된다.

```cpp
while ((pos = input.find(delimiter)) != string::npos)
```

찾았다면 **해당 pos****까지 해당 부분 문자열을 추출**한다.

예를 들어 abcd에서 d를 찾았다면 pos는 3을 반환하게 되고 3만큼 **substr**을 하기 때문에 abc를 추출하게 된다.

```cpp
token = input.substr(0, pos);
```

그 다음 이 **추출한 문자열을 ret이란 배열**에 집어 넣는다.

```cpp
ret.push_back(token);
```

그리고 앞에서 부터 문자열을 지운다. abcdabc에서 d가 delimeter이라면 pos = 3, delimeter의 사이즈는 1이기 때문에 앞에서 부터 4의 크기의 문자열을 제거해 abc만 남게 된다.

```cpp
input.erase(0, pos + delimiter.length());
```

> **범위기반 for 루프**

-   앞의 코드를 보면 범위기반 for루프가 있는 것을 볼 수 있는데 C++11부터 범위기반 for 루프가 추가되어서 이를 쓸 수 있다.

```
for ( range_declaration : range_expression )
    loop_statement
```

-   아래 코드는 vector a 내에 있는 요소인 **string 타입의 요소를 탐색**한다는 코드이고
-   아래 두 코드는 같은 의미이다.

```
for(string b : a) cout << b << "\n";
```

```
for(int i = 0; i < a.size(); i++) cout < a[i] << "\n";
```

```cpp
#include <bits/stdc++.h>
using namespace std;
string a[2] = {"out of time", "i love you"};
int main() {
    for(string b: a) cout << b << '\n';
    
    for(int i = 0; i < 2; i++) cout << a[i] << "\n";
}

/*
out of time
i love you
out of time
i love you
*/
```

> **atoi(s.c_str())**

-   문자열을 int로 바꿔야 할 상황에 사용

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    string s = "1";
    string s2 = "amumu";
    cout << atoi(s.c_str()) << '\n';
    cout << atoi(s2.c_str()) << '\n';
    return 0;
}

/*
1
0
*/
```

---

#### **4. bool, 참과 거짓**

-   **1바이트, true** 또는 **false**
-   **1 또는 0**으로 선언해도 무방
-   참고로 C++에서는 0이면 false, 0이 아닌 값들은 모두 true가 되며 bool()을 통해 간단하게 bool형으로 형변환이 가능

```cpp
#include<bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int a = -1;
    cout << bool(a) << "\n";
    a = 0;
    cout << bool(a) << "\n";
    a = 3;
    cout << bool(a) << "\n";
}

/*
1
0
1
*/
```

---

#### **5. int, 4바이트짜리 정수**

-   4바이트짜리 정수를 사용할 때 쓰이며 
-   표현범위는 -2,147,483,648 ~ 2,147,483,647 -> **약 20억까지 표현** 가능
-   즉, 문제를 푸는 코드에 들어가있는 값들의 예상값이 **20억을 넘어간다면 int가 아닌 long long**을 써야하며 또한 문제를 풀 때는 이상한 문제가 아니라면 int의 최대값으로 20억까지가 아닌 987654321 또는 1e9를 쓴다.
-   왜냐하면 이 INF를 기반으로 INF + INF라는 연산이 일어날 수도 있고 INF * 2연산, 그리고 INF + 작은 수 연산이 일어날 때 **오버플로를 방지**할 수 있기 때문

```
const int INF = 987654321;
```

-   const는 수정할 수 없는 변수를 뜻한다.
-   C++ 에서는 INF 또는 방향벡터와 같은 곳에 const 를 사용하는데 
-   이 const를 붙임으로써 **수정하지 말아야 된다는 것, 유지보수성, 수정시 쉽게** **에러탐지**의 장점이 있다.

> **오버플로(overflow)**

-   **타입의 허용범위를 넘어갈 때 발생하는 에러**를 뜻한다.
-   아래 코드처럼 최대범위를 벗어나게 되면 최댓값 +1이 아닌 **최솟값**으로 돌아가버린다.
-   이를 **UB(unexpected Behavior)**라고 부른다.

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int a = 2147483647;
    cout << a << '\n';
    a++;
    cout << a << '\n';
}
/*
2147483647
-2147483648
*/
```

> **언더플로**

-   오버플로와는 반대로 취급할 수 있는 결과값보다 작아지게 되면 언더플로가 발생된다.

```cpp
#include <bits/stdc++.h>
using namespace std;
int main(){
    int a = -2147483648;
    cout << a << '\n';
    a--;
    cout << a << '\n';
}
/*
-2147483648
2147483647
*/
```

---

#### **6. long long, 8바이트짜리 정수**

-   8바이트 짜리 정수
-   범위는 –9,223,372,036,854,775,808 ~ 9,223,372,036,854,775,807이고 int로 표현이 안될 때 쓰면 된다.
-   예를 들어 문제의 최대범위가 int로는 처리할 수 없는 30억이라면 바로 long long을 써야 한다.
-   보통은 아래와 같이 INF와 비슷한 이유로 1e18로 정의를 해놓고 쓰면 되나 이는 문제마다 다르니 참고만 해주시면 된다.

```cpp
typedef long long ll;
ll INF = 1e18;
```

---

#### **7. double, 실수 타입**

-   **8바이트** 이며 소수점 아래로 **15자리 까지 표현 가능**
-   참고로 **float**도 있는데 이는 4바이트, 소수점 아래로 7자리까지 표현이 가능

```cpp
double pi = 3.221;
```

---

#### **8. unsigned long long, 8바이트짜리 양의 정수**

-   부호가 없는 정수
-   long long에서 -로 표현할 범위를 몽땅 + 범위에 추가한 타입
-   아주 가끔 사용한다 !
-   범위 : 0 ~ 18,446,744,073,709,551,615

[백준 3613 - java vs c++](https://www.acmicpc.net/problem/3613)

#### **시간 제한 1초, 메모리 제한 128MB**

## **# 조건**

- Java 예찬론자 김동규와 C++ 옹호가 김동혁은 서로 어떤 프로그래밍 언어가 최고인지 몇 시간동안 토론을 하곤 했다. 
- 동규는 Java가 명확하고 에러가 적은 프로그램을 만든다고 주장했고, 동혁이는 Java는 프로그램이 느리고, 긴 소스 코드를 갖는 점과 제네릭 배열의 인스턴스화의 무능력을 비웃었다.
- 또, 김동규와 김동혁은 변수 이름을 짓는 방식도 서로 달랐다. 
- Java에서는 변수의 이름이 여러 단어로 이루어져있을 때, 다음과 같은 방법으로 변수명을 짓는다. 
- 첫 단어는 소문자로 쓰고, 다음 단어부터는 첫 문자만 대문자로 쓴다. 또, 모든 단어는 붙여쓴다.
- 따라서 Java의 변수명은 `javaIdentifier`, `longAndMnemonicIdentifier`, `name`, `bAEKJOON`과 같은 형태이다.
- 반면에 C++에서는 변수명에 소문자만 사용한다. 단어와 단어를 구분하기 위해서 밑줄('`_`')을 이용한다. C++ 변수명은 `c_identifier`, `long_and_mnemonic_identifier`, `name`, `b_a_e_k_j_o_o_n`과 같은 형태이다.
- 이 둘의 싸움을 부질없다고 느낀 재원이는 C++형식의 변수명을 Java형식의 변수명으로, 또는 그 반대로 바꿔주는 프로그램을 만들려고 한다. 각 언어의 변수명 형식의 위의 설명을 따라야 한다.
- 재원이의 프로그램은 가장 먼저 변수명을 입력으로 받은 뒤, 이 변수명이 어떤 언어 형식인지를 알아내야 한다. 
- 그 다음, C++형식이라면 Java형식으로, Java형식이라면 C++형식으로 바꾸면 된다. 만약 C++형식과 Java형식 둘 다 아니라면, 에러를 발생시킨다. 
- 변수명을 변환할 때, 단어의 순서는 유지되어야 한다.
- 재원이는 프로그램을 만들려고 했으나, 너무 귀찮은 나머지 이를 문제를 읽는 사람의 몫으로 맡겨놨다.
- 재원이가 만들려고 한 프로그램을 대신 만들어보자.

### **입력**
- 첫째 줄에 변수명이 주어진다.
- 영어 알파벳과 밑줄('_')로만 이루어져 있고, 길이는 100을 넘지 않는다.

### **출력**
- 입력으로 주어진 변수명이 Java형식이면, C++형식으로 출력하고, C++형식이라면 Java형식으로 출력한다. 둘 다 아니라면 "Error!"를 출력한다.


## **# 접근 방법**

- 주어진 문자열을 순회하면서 ' _ ' 가 먼저 나오는지, 대문자가 먼저 나오는지 판단해준다.
- 즉, c++인지 java인지 error인지 판단을 해주는데 아래의 예외 케이스가 생각보다 많았다.
	- 첫 글자가 언더바 또는 대문자이면 에러
	- 마지막 글자가 언더바이면 에러
	- 언더바가 중복되어 나오면 에러
	- 대문자와 언더바가 동시에 나온다면 에러
- 이외의 경우에는 정상 변환해준 후 출력해준다.


```python
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def check(word):
    w_cnt = 0
    u_cnt = 0

    if word[0] == '_' or word[0].isupper() or word[-1] == '_':
        return 'Error!'

    for i, t in enumerate(target):
        if t.isupper():
            w_cnt += 1
            
        elif t == '_':
            u_cnt += 1
            if target[i-1] == '_':
                return 'Error!'
    if w_cnt > 0 and u_cnt > 0:
        return 'Error!'
    elif w_cnt > 0:
        return 'Java'
    elif u_cnt > 0:
        return 'C++'
    else:
        return word
    
def java_to_c(s):
    cv = ''
    for c in s:
        if ord('A') <= ord(c) and ord(c) <= ord('Z'):
            cv += '_'
            cv += c.lower()
        else:
            cv += c

    return cv

def c_to_java(s):
    cv = ''
    upper_flg = False
    for c in s:
        if c == '_':
            upper_flg = True
        else:
            if upper_flg:
                cv += c.upper()
                upper_flg = False
            else:
                cv += c

    return cv

target = input().strip('\n')
mode = check(target)
if mode == 'Error!':
    print(mode)
elif mode == 'Java':
    print(java_to_c(target))
elif mode == 'C++':
    print(c_to_java(target))
else:
    print(mode)
```
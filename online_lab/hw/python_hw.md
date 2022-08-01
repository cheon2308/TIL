# 0718

## 1. 평균 성적 구하기

```python
score = {'python': 80, 'django': 89, 'web': 83}

score['algorithm'] = 90 #추가
score['python'] = 85 #수정


aver = sum(score.values()) / len(score) #평균값

print(aver)
```

## 2. 각 자릿 수 더하기

```python
s = input('숫자를 입력해주세요 : ')
sum = 0
for i in list(str(s)):

    sum += int(i)

print(sum)
```

--- 

# 0719

## 1.  카페 주문내역 확인하기

```python
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders_list = list(orders.split(','))

print(len(orders_list))

menu = []
for i in orders_list:
    if i not in menu:
        menu.append(i)
menu.sort(reverse=True)  
print(menu)
```

## 2. 아이스 음료 주문 몇개 들어왔는지, 메뉴별 출력

```python
orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders_list = orders.split(',')
#1
cnt = 0 # 결과값 들어갈 변수
for i in orders_list:
    if '아이스' in i: 
        cnt += 1


print(cnt) # 아이스 들어간 주문 수 추출

#2
orders_set = list(set(orders_list))
orders_set.sort() # 중복안되게 메뉴판 작성

j = 0
for char in orders_set:
    count = 0
    for i in orders_list: # 메뉴판과 주문메뉴가 동일하면
        if i == char:
            count += 1 # 카운트 증가
    print(char, count) # 안쪽 for문 끝날 때마다 메뉴와 주문 수 출력
```

# 0720

## 1. 윤년 판별

```python
year = int(input())

if year % 4 == 0:
    if year % 100 != 0:
        print(str(year)+ '년 = 윤년')
    elif year % 400 == 0:
        print(str(year)+ '년 = 윤년')
    else:
        print(str(year)+ '년 = 윤년아님')
```

# 2. 삼각형 종류 판별

```python
s_triangle = map(int, input().split(' ')) # 숫자 3개 받아서
a,b,c = sorted(s_triangle) #오름차순 정렬해준다

print(sorted)
if a+b > c: # 가장 긴변 c보다 a+b가 크다면 삼각형 성립
    if a ==b and b ==a: #모든 변이 같다면 정삼각형
        print('정삼각형')

    elif a==b or b==c or a==c: #3변 중 2변이 같다면 이등변 삼각형
        print('이등변 삼각형')

    elif a**2 + b**2 == c**2: #가장 긴 변의 제곱 = 나머지 두변의 제곱의 합이라면 직각삼각형 (피타고라스)
        print('직각 삼각형')

    else:
        print('삼각형') # 위 조건들 중 하나도 해당 안한다면 그냥 삼각형

else:
    print('삼각형아님') # 가장 긴변보다 나머지 두 변의 합이 작다면 삼각형 아님
```

---

# 0721

# 1. 끝말잇기

```python
words = ["round", "tweet","dream","magnet",  "tweet", "trick", "kiwi"]

# 끝말잇기 몇 번째 사람 탈락
# 틀리거나 이전에 등장했던 단어 사용하는 경우 지게 된다.
# cnt를 이용해 사람 수 체크
# 반복문 이용하여 마지막 글자와 앞에 글자 비교
# 이전에 등장했던 단어인지 체크
cnt = 1
pre_words = []
for i in range(len(words)):
    cnt += 1
    j = i+1
    if words[i] in pre_words:
        break
    if words[j][0] != words[i][-1]:
            break
    pre_words.append(words[i])

print(f'{cnt}번째 사람이 탈락입니다.')
```

## 2. 문자열 애너그램

```python
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_dict = {}  # 애너그램단위로 묶은 결과가 들어있는 딕셔너리
# key : 해당 단어를 정렬한 결과
# value : key와 같은 애너그램 그룹에 있는 단어들의 모음을 리스트로 만든다.

for word in words:
    sorted_word = "".join(sorted(word))  # sorted() => 결과가 리스트, 문자열로 변환해야한다. ==> join()
    # word = "eat"
    # sorted(word) = ["a" , "e" , "t"]
    # "".join(sorted(word)) = "aet"
    # ".".join(sorted(word)) = "a.e.t"
    #print(sorted_word)
    if anagram_dict.get(sorted_word):  # 딕셔너리에 애너그램 그룹이 존재한다.
        anagram_dict[sorted_word].append(word)  # 존재하면 리스트에 추가를 해준다.
    else:
        anagram_dict[sorted_word] = [word]  # 존재하지 않으면 리스트를 새로 만들어준다.

print(anagram_dict)
```

--- 

# 0725

## 1.  윤년 판별하기(함수)

```python
def leap_year(year):
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
        return f'{year}년은  윤년입니다.'
    else:
        return f'{year}년은  윤년이 아닙니다.'
```

## 2. 제너레이터와 셀프넘버

```python
#1 제너레이터 함수
# 입력된 숫자의 각 자릿수 숫자들 + 자신을 더한 숫자

def fn_d(n):
    result = 0
    for i in str(n):
        result += int(i)
    result += n

    return result

#2 셀프 넘버
# 1, 3, 5, 7, 9, 20 과 같이 제너레이터가 없는 숫자 구하기
def is_selfnumber(n):
    genernumber = []
    for i in range(1, n):

        genernumber.append(fn_d(i))
        #print(([int(j) for j in str(i)]))
        selfnumber =list(set(range(1,n)) - set(genernumber))
        selfnumber.sort()

    return selfnumber

if __name__ == '__main__':
    print(is_selfnumber(100))
```

--- 

# 0726

## 1. 소금물 농도 구하기

```python
salt = []  # 소금
salt_water = []  # 소금물
i = 0

while i < 5:
    i += 1
    s = input(f'{i}.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')

    if s == 'Done':
        break

    S, L = int(s[: s.find('%')]), int(s[s.find(' ') + 1 : s.find('g')])

    salt.append(S * L / 100)
    salt_water.append(L)

print('{:.2f}% {}g'.format(sum(salt) / sum(salt_water) * 100, sum(salt_water)))
```

# 2. 애너그램 함수

```python
def group_anagrams(words):

    anagram_dict = {}  # 애너그램단위로 묶은 결과가 들어있는 딕셔너리
    # key : 해당 단어를 정렬한 결과
    # value : key와 같은 애너그램 그룹에 있는 단어들의 모음을 리스트로 만든다.

    for word in words:
        sorted_word = "".join(sorted(word))  # sorted() => 결과가 리스트, 문자열로 변환해야한다. ==> join()
        # word = "eat"
        # sorted(word) = ["a" , "e" , "t"]
        # "".join(sorted(word)) = "aet"
        # ".".join(sorted(word)) = "a.e.t"
        #print(sorted_word)
        if anagram_dict.get(sorted_word):  # 딕셔너리에 애너그램 그룹이 존재한다.
            anagram_dict[sorted_word].append(word)  # 존재하면 리스트에 추가를 해준다.
        else:
            anagram_dict[sorted_word] = [word]  # 존재하지 않으면 리스트를 새로 만들어준다.

        anagram_lst = list(anagram_dict.values())
    return anagram_lst


if __name__ == '__main__':
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
```

--- 

# 0727

# 1. 강아지 클래스 만들기

```python
class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        print(f'{kind}인 {name}가 태어났습니다.')
        Doggy.num_of_dogs +=1
        Doggy.birth_of_dogs +=1


    def bark(self):
        print(self.name + ':왈왈')

    def dog_status(self):
        print(self.name + '천국으로 갔어요ㅠㅠ')
        Doggy.num_of_dogs -= 1 

    def get_status( num_of_dogs, birth_of_dogs):
        print(f'강아지 마릿 수 : {Doggy.num_of_dogs},태어난 강아지 수 :{Doggy.birth_of_dogs}' )

dog_one = Doggy('절미', '푸들')
dog_one.bark()
dog_two = Doggy('깜이','닥스훈트')
dog_three = Doggy('워윅이','포메라니안')
dog_one.dog_status()
Doggy.get_status('','')
```

# 2. Collatz

```python
def solution(num):
    answer = 0
    while num > 1:
        if num%2==0:
            num /= 2
        elif num%2 == 1:
            num = (num*3)+1
        answer += 1
    if answer >= 500:
        answer = -1
    return answer

if __name__ == '__main__':
    print(solution(6))
```

---

# 0728

# 1. Point클래스

```python
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

class Rectangle:

    def __init__(self, p1, p2):
        #self.x1 = p1.x
        #self.y1 = p1.y
        #self.x2 = p2.x
        #self.y2 = p2.y
        self.p1 = p1
        self.p2 = p2
        self.width = abs(self.p1.x - self.p2.x)
        self.height = abs(self.p1.y - self.p2.y)

    def get_area(self):
        #area = (self.x2-self.x1) * (self.y1-self.y2)
        # 가로 *세로
        #width = abs(self.p1.x - self.p2.x)
        #height = abs(self.p1.y - self.p2.y)

        return self.width*self.height

    def get_perimeter(self):
        #perimeter = (self.x2-self.x1) * 2 + (self.y1-self.y2) *2
        #width = abs(self.p1.x - self.p2.x)
        #height = abs(self.p1.y - self.p2.y)

        return (self.width +self.height) *2

    def is_square(self):
        #bool = (self.x2 == self.y1 and self.x1 == self.y2)
        #width = abs(self.p1.x - self.p2.x)
        #height = abs(self.p1.y - self.p2.y)

        return self.width == self.height


p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3,7)
p4 = Point(6,4)
r2 = Rectangle(p3,p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
```

# 2. 스택 구현하기

```python
class Stack():
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        pop_object = None
        if self.empty():
            return None
        else:
            pop_object = self.stack.pop()
            
        return pop_object
            
    def top(self):
        top_object = None
        if self.empty():
            return None
        else:
            top_object = self.stack[-1]
            
        return top_object
            
            
    def empty(self):
        empty = False
        if len(self.stack) == 0:
            empty = True
        return empty
    
    def __repr__(self):
        return self.stack

stk = Stack()        # stack 객체 생성
        # stack object 생성 확인

print(stk.empty()) # 처음에는 아무것도 들어있지 않으므로 True 출력
stk.push(1)          # stk 에 1 넣음 : [1]
stk.push(2)          # stk 에 2 넣음 : [1,2]

print(stk.pop())     # stk 에 2가 꺼내지면서 출력 : 2 / [1]
print(stk.__repr__())
print(stk.empty()) # 비어있지 않으므로 False 출력
print(stk.pop())     # stk 에 1가 꺼내지면서 출력 : 1 / []
print(stk.empty()) # 객체에 아무것도 들어있지 않으므로 True 출력

```

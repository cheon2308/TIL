# 0718

# 1. 문자출력

```python
print("c:\python_project\\test")
```

# 2. 총 페이지 수 구하기

```python
# text, page_1 = list(map(int, input().split())) # 총 게시글 수 , 한 페이지에 들어갈 게시글 수

page_made = text / page_1 #생성되는 페이지 수 

if text % page_1 == 0:
    print (int(page_made))
else:
    print (int(page_made +1))
```

# 3. 주민번호 비식별 처리

```python
num = list(str(input()))

i=0
id=''
for i in range(0 ,len(num)): #주민번호 길이만큼 반복

    if i <= 5:

        id = str(id) + num[i] # 생년월일은 출력

    else:
        id = str(id) + '*' #그 외에는 비식별
    i = i+1

print(id)
```

# 4. 2와 7의 배수의 합 구하기

```python
number = list(range(1,1000))

A =0

for i in number:
    if i % 2 == 0:
        A = A + i
    elif i % 7 == 0:
        A = A + i
    elif i % 2 and i % 7 == 0:
        A = A - i
    else:
        continue
    i+= 1

print(A)
```

# 5. 직사각형 *로 출력하기

```python
n = 4 #가로길이

m = 5 #세로길이

N = '*' * int(n)

M = (N +  '\n') * int(m)

print(M)
```

---

# 0719

# 1. 근의 공식

```pyton
a = 3

b = 6

c = - 5

root1 = ( -b + (b**2 - 4*a*c)**(1/2)) / (2*a)

root2 = ( -b - (b**2 - 4*a*c)**(1/2)) / (2*a)

print(round(root1,4), round(root2,4))
```

# 2. 특수문자 빼기

```python
s = input()
#1
new_string = ''.join(char for char in s if char.isalnum())

#2
new_string = ''
for char in s:
    if char.isalnum() == True:  #숫자 또는 문자가 맞다면
        new_string += char    #추가
new_string = new_string.lower() #소문자변환
new_string = new_string.capitalize() #첫 글자만 대문자
print(new_string)

#3
new_string = ''.join(filter(str.isalnum, string))
```

# 3. 끝말잇기

```python
sen = input()

sen = sen.split()


j=1
for i in sen:

    word = list(i) # 한 단어를 리스트로 만들기
    if j < len(sen): # sen리스트 길이 안에서만 비교
        if word[-1] == sen[j][0]: # 첫 단어의 끝 글자와, 다음 글자의 첫 글자를 비교
            sta = 'pass' #같다면 pass 변수 할당 후 sen 인덱스값 +1
            j+=1     
        else:
            sta = 'fail' # 다르다면 fail 변수 입력 후 탈출
            break
    else:
        break
print(sta)
```

# 4. 고기값 출력

```python
steak =  float(50000)
vat  =   float(steak * 1.15)
total =  float(steak + vat)

print(f'steak가격은 {steak}원이고 vat 금액 {vat}원이 포함되어 총 {total}원 입니다.')
```

# 5. 제일 비싼 농작물

```python
veg = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

veg = dict(veg) # 딕셔너리로 변환

s= max(dict(veg).values()) # 최고 value 값 추출

for k,v in veg.items(): #veg 딕셔너리 순회하며 value값에 맞는 키값 추출
    if v == 4500:
        print(k)

print([k for k, v in veg.items() if v == s]) # 조건표현식으로 추출
```

---

# 0720

# 1.  썩은 과일 바꾸기

```python
fruit = input()

fruit = fruit.split(',')
new_fruit = []
for i in fruit:
    i = i.lower()
    if 'rotten' in i:
        i = i.replace('rotten','')
    new_fruit.append(i)
print(new_fruit)
```

# 2.  중간 문자 구하기

```python
def get_middle_char(a):
    if len(a) % 2 == 0:
        return a[len(a)//2-1:len(a)//2+1] # 중간값 직전 인덱스 이상, 중간값 다음값 미만 출력
    else:
        return a[len(a) // 2]

print(get_middle_char('coding'))
```

# 3. Dictionary 내부의 나이 더하기

```python
dict_list_sum = ([{'name':'kim', 'age':12}, 
                  {'name':'lee', 'age':4}])

age_val = {}
age = 0 

for i in dict_list_sum:
    age += i['age']    

print(age)
```

# 4. 혈액형으로 딕셔너리 구성

```python
# key : 혈액형 종류, value : 사람수
# 리스트로 받아서 딕셔너리 구성
blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_A, blood_B, blood_O, blood_AB = (0, 0, 0, 0)
blood_people = {}
for i in blood_types:
    if i == 'AB':
        blood_AB +=1
    elif i == 'A':
        blood_A += 1
    elif i == 'B':
        blood_B += 1
    else: # i == 'O':

        blood_O += 1


blood_people = {'A' : blood_A, 'B' :blood_B, 'O':blood_O, 'AB': blood_AB}
print(blood_people)
```

# 5. 소금물 농도 구하기

```python
# 소금물 퍼센트 농도와 소금물의 양 입력
# Done 입력시 혼합물의 퍼센트 농도와 양 출력
# 최대 5개의 소금물 입력가능
# 반올림 2번째 자리까지 표현


salt_water = list(map(float, input('소금물의 농도, 양 순서로 입력해주세요:').split()))  


salt = []
concentration = []
water = []
for i in range(len(salt_water)):  #입력되는 소금물 리스트의 값을 농도, 양으로 나누고 농도/양 *100을 통하여 소금의 양 구하기
    if i % 2 == 0:
        water.append(salt_water[i+1]) #소금물의 양
        concentration.append(salt_water[i]) #농도
        salt.append(salt_water[i] * 0.01 * salt_water[i+1]) # 소금의 양

# 합쳐진 소금물의 소금의 양, 소금물의 양 구하기
total_salt = sum(salt) #총 소금의 양
total_water = round(sum(water),2) # 총 소금물의 양

total_concentration = round((total_salt/total_water)*100, 2) # 혼합물의 농도 구하기

#print(salt,concentration, total_salt, total_water)

if input() == 'Done':   #Done 입력시 농도와 양 출력
    print (f'혼합물의 농도 : {total_concentration}%, 혼합물의 양 : {total_water}ml')
```

---

# 0721

# 1. 비밀번호 입력

```python
# 맞는 비밀번호 입력까지 반복
# 3번 이상 틀리면 종료

password = input()

cnt=0
while cnt < 3:
    j = input()
    cnt += 1
    if j == password:
        print('문이 열립니다.')
        break
    if cnt != 3:   
        print('다시 입력하세요 : ')
    else:
        print('문을 열수 없습니다.')
```

# 2. 반장선거

```python
students = ['박해피', '이영희', '조민지', '조민지', 
            '김철수', '이영희', '이영희', '김해킹',
            '박해피', '김철수', '한케이', '강디티',
            '조민지', '박해피', '김철수', '이영희',
            '박해피', '김해킹', '박해피', '한케이','강디티']

# 입력받은 리스트를 딕셔너리로 구성
# key : 이름, value : 득표수

vote = {}

for i in students:
    if i in vote:
        vote[i] += 1
    else:
        vote[i] = 1

print(sorted(vote.keys(), key = lambda item : item[1], reverse = True)) #sorted(정렬 데이터, key 파라미터(기준값), reverse 파라미터)
```

# 3. 중복 숫자 제거

```python
num = list(map(int, input().split()))
print(num)
new_num = []
for i in range(len(num)):
    if [num[i]] != num[i+1:i+2]:
        new_num.append(num[i])

print(new_num)
```

# 4. 아스키 코드 변환

```python
word1 = input('첫 번째 이름을 입력하세요 : ')
word2  = input('두 번째 이름을 입력하세요 : ')

def get_strong_word(a,b):
    sum1 = 0
    sum2 = 0
    for i in a:
        sum1 += ord(i) #a 변환 후 합
    for j in b:
        sum2 += ord(j) #b 변환 후 
    if sum1 > sum2:
        return a
    elif sum1 == sum2:
        return a, b
    elif sum1 < sum2:
        return b   


#get_strong_word('z', 'a')
s = get_strong_word(word1, word2) 
print(s)
```

# 5. 반의어 출력

```python
words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

words = list(words_dict.keys())
#print(words)
# b,m,p일 때 im-
# l일 때, il-
# r일 때, ir-
new_words = [] # 한 문자씩 쪼개기

for i in words:

    if i[0:1] == 'b' or i[0:1] == 'p' or i[0:1] == 'm': #문자열 슬라이싱을 통해 첫글자 비교
        i = 'im'+i
    elif i[0:1] == 'l':
        i = 'il'+i
    elif i[0:1] == 'r':
        i = 'ir'+i
    new_words.append(i)

print(sorted(new_words))
```

---

# 0725

# 1. 썩은 과일 교체하기

```python
def fruit(a):
    a = a.lower()
    a = a.replace('rotten','')
    a = a.split(',')

    return a

if __name__ == '__main__':
    print(fruit('apple,rottenBanana,apple,RoTTenorange,Orange'))
```

# 2. 모듈 import하여 각 연산 수행하는 함수 실행

```python
# calc.py
def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):

    try:
        num1 / num2

    except ZeroDivisionError:
        return '0으로는 나눌 수 없습니다.'

    return num1/num2  

#예제 풀기
import calc 

if __name__ == '__main__':
    print(calc.add(2, 3)) # 5
    print(calc.sub(2, 3)) # -1
    print(calc.mul(2, 3)) # 6
    print(calc.div(2, 3)) # 0.6666666666666666

    print(calc.div(2, 0)) # 0으로 나눌 수 없습니다.
```

# 3. 특수문자 지우기

```python
def string_change(sentence):


    result = ''
    for char in sentence:
        if char.isalpha() or char == ' ':
            result += char


    return result.capitalize()

if __name__ =='__main__':
    print(string_change('@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'))
```

# 4.  중복 안된 숫자만 더하기

```python
def sum_of_repeat_number(number):
    result = 0

    for i in number:
        if number.count(i) == 1:

            result += i
    return result



if __name__ =='__main__':
    print(sum_of_repeat_number([4,4,7,8,10,4]))
```

# 5. 반의어 출력하기

```python
words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

words = list(words_dict.keys())
#print(words)
# b,m,p일 때 im-
# l일 때, il-
# r일 때, ir-
new_words = [] # 한 문자씩 쪼개기

for i in words:

    if i[0:1] == 'b' or i[0:1] == 'p' or i[0:1] == 'm': #문자열 슬라이싱을 통해 첫글자 비교
        i = 'im'+i
    elif i[0:1] == 'l':
        i = 'il'+i
    elif i[0:1] == 'r':
        i = 'ir'+i
    new_words.append(i)

print(sorted(new_words))
```

---

# 0726

# 1. 주민번호 식별하기

```python
def de_identify(numbers):

    new_num = ''
    for i in range(len(numbers)):

        if i > 5:
            numbers =numbers.replace(numbers[i],'*')
            new_num +=numbers[i]
        else:
            new_num += numbers[i]
    return new_num

if __name__ == '__main__':
    print(de_identify('970103-1234567'))
    print(de_identify('8611232345678'))
```

# 2. 가장 비싼 작물

```pyton
veg = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

veg = dict(veg) # 딕셔너리로 변환

s= max(dict(veg).values()) # 최고 value 값 추출

for k,v in veg.items(): #veg 딕셔너리 순회하며 value값에 맞는 키값 추출
    if v == 4500:
        print(k)

print([k for k, v in veg.items() if v == s]) # 조건표현식으로 추출
```

# 3. 모음 갯수

```python
def count_vowels(word):
    #result = word.count('i') + word.count('a') +word.count('e') + word.count('o') + word.count('u')
    result = 0

    #for char in word:
    #    if char in 'aeiou':
    #        result +=1

    for char in 'aeiou':
        result += word.count(char)

    return result

if __name__ == '__main__':
    print(count_vowels('apple'))
    print(count_vowels('banana'))
```

# 4. 혈액형

```python
blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

blood_A, blood_B, blood_O, blood_AB = (0, 0, 0, 0)
blood_people = {}
for i in blood_types:
    if i == 'AB':
        blood_AB +=1
    elif i == 'A':
        blood_A += 1
    elif i == 'B':
        blood_B += 1
    else: # i == 'O':

        blood_O += 1


blood_people = {'A' : blood_A, 'B' :blood_B, 'O':blood_O, 'AB': blood_AB}
print(blood_people)
```

# 5. 각 자릿수 더하기(함수)

```python
#1
def sumOfDigits(num):
    digits = map(int, list(str(num)))
    return sum(digits)

if __name__ == '__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))

#2
def sumOfDigits(num):
    sum = 0
    for c in list(str(num)):
        sum += int(c)

    return sum

if __name__ == '__main__':
    print(sumOfDigits(47253))
    print(sumOfDigits(643))
```

--- 

# 0727

# 1. 국적

```python
class Nationality:
    def __init__(self, location):
        self.location =f'나의 국적은 {location}'




korea_nationality = Nationality('대한민국')
print(korea_nationality.location) # 나의 국적은 대한민국
```

# 2. 끝말잇기

```python
def wordrelay(words):
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

    return f'{cnt}번째 참가자가 탈락하였습니다.'

# 끝말잇기 몇 번째 사람 탈락
# 틀리거나 이전에 등장했던 단어 사용하는 경우 지게 된다.
# cnt를 이용해 사람 수 체크
# 반복문 이용하여 마지막 글자와 앞에 글자 비교
# 이전에 등장했던 단어인지 체크

if __name__ == '__main__':
    words = ["round","dream","tweet","magnet","tweet","trick","kiwi"]
    print(wordrelay(words)) # 5번째 참가자가 탈락하였습니다.
```

# 3. 계산기

```python
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        pass
    
    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

    def mul(self):
        return self.num1 * self.num2

    def div(self):

        try:
            self.num1 / self.num2

        except ZeroDivisionError:
            return '0으로는 나눌 수 없습니다.'

        return self.num1/self.num2  

problem1 = Calculator(1,2)
problem2 = Calculator(2,1)
problem3 = Calculator(3,4)
problem4 = Calculator(4,0)

print(problem1.add())
print(problem2.sub())
print(problem3.mul())
print(problem4.div())

```

# 4. 주차요금 계싼하기

```python
import math

def fee(time, distance):
    lent_fee = 1200 * time /10
    insuarance_fee = 525 * math.floor(time/30)
    ride_fee = 0
    
    if distance > 100:
        ride_fee = 170 * 100 + 85*(distance-100)
    else:
        ride_fee = 170 *distance
        
    total = lent_fee + insuarance_fee + ride_fee
    return total

if __name__ == '__main__':
    print(fee(600,50))
```

# 5. 페어프로그래밍

```python

```

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

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

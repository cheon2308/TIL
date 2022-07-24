# 0718

# 0719

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

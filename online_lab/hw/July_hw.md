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

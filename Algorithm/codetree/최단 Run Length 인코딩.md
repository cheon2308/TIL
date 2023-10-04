
[코드트리 - 최단 Run Length 인코딩](https://www.codetree.ai/cote/13/problems/shortest-run-length-encoding?&utm_source=clipboard&utm_medium=text)

![](assets/Pasted%20image%2020231005004032.png)

## **# 접근 방법**

- 문자열을 비손실 압축 방식으로, 오른쪽으로 shift를 통하여 최소 길이로 만드는 문제이다.
- 평소에 많이 접해보지 않은 문제이지만 아이디어를 떠올리는 것이 어렵지 않았다.
- 오른쪽 shift를 통해서 현재보다 짧은 길이로 만들기 위해서는, **가장 먼저 나온 문자열**과 **가장 마지막에 나온 문자열이 같아야 된다.** 
- 우선, 주어진 문자열을 순회하며 비손실 압축을 해준다.
- 이후 길이가 2인 경우 => 모든 문자열이 1개로 이루어진 경우는 바로 **2**를 출력해준다.
- 그렇지 않다면, 뒤에서 2번째 문자와 가장 첫 문자를 비교해준 후, 같다면 개수를 합쳐준다.

```python
import sys  
input = sys.stdin.readline  
  
words = input().strip()  
new_word = ''  
val = words[0]  
cnt = 0  
for i in words:  
    if i == val:  
        cnt += 1  
    else:  
        new_word += val + str(cnt)  
        cnt = 1  
        val = i  
new_word += val + str(cnt)  
if len(new_word) == 2:  
    print(len(new_word))  
else:  
    if new_word[0] == new_word[-2]:  
        val = new_word[-1]  
        new_word = list(new_word[:-2])  
        new_word[1] = str(int(new_word[1]) + int(val))  
    print(len(new_word))
```
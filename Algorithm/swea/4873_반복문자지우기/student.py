import sys
sys.stdin = open("input.txt")

class Stack:
    def __init__(self, size=1000):
        self.size = size
        self.arr = [None for _ in range(size)]
        self.top = -1

    def __len__(self):
        return self.top+1

    def push(self, value):
        if not self.is_full():
            self.top += 1
            self.arr[self.top] = value

    def pop(self):
        if not self.is_empty():
            result = self.arr[self.top]
            self.arr[self.top] = None
            self.top -= 1
            return result
        else:
            raise IndexError("Stack is Empty!!")

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False

    def is_full(self):
        if self.top == self.size-1:
            return True
        else:
            return False

    def peek(self):
        if not self.is_empty():
            return self.arr[self.top]
        else:
            raise IndexError("Stack is Empty!!")


T = int(input())

for tc in range(1, T+1):
    word = input()  # 단어 입력받기
    s1 = Stack()    # 스택 생성
    for c in word:  # 문자 하나씩 순회
        # 스택이 비어있지 않고,
        if not s1.is_empty() and s1.peek() == c:
            s1.pop()
        else:
            s1.push(c)

    print(f"#{tc} {len(s1)}")
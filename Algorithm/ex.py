import sys
sys.stdin = open('input.txt')
# 최소합을 구해주기 위해선 -뒤에 다음 -가 나오기 전까지 괄호를 쳐주면 된다.

# 중위 표기법 -> 후위 표기법 변환
def infix_to_postfix(expression):
    cal = []  # 후위 표기법 받을 문자열
    stack = []  # 스택
    cnt = 0


    for e in range(len(expression)):
        # e가 숫자라면 cal에 더하기
        if expression[e] not in '+-':
            cal.append(expression[e])

        # -의 우선순위를 높게 쳐준다.
        elif expression[e] == '-':
            # 같은 -가 나오기전까지
            # stack pop하고 cal에 더한다.
            while stack and stack[-1] == '+':
                cal.append(stack.pop())
            # 이제 없다면 stack에 e push
            stack.append(expression[e])
        # 더하기는 무조건 더해준다.
        elif expression[e] == '+':
            while stack and stack[-1] != '-':
                cal.append(stack.pop())
            stack.append(expression[e])
        # 연산이 끝났는데 괄호가 하나밖에 없다면

    # stack에 남아있는 연산자 cal에 더해주면 후위 표기식 완성
    while stack:
        cal.append(stack.pop())
    print(cal)
    return cal


# 후위 표기법의 수식 계산
def cal_postfix(expression):
    stack = []
    for e in expression:
        # e가 숫자라면 stack에 push
        if e.isdigit():
            stack.append(int(e))
        # e가 연산자라면 stack에서 숫자 두개를 꺼내와 연산자로 계산 후 stack에 push
        elif e in '+-' and len(stack)>1:
            num1 = stack.pop()
            num2 = stack.pop()
            if e == '+':
                stack.append(num2 + num1)
            elif e == '-':
                stack.append(num1 - num2)

    return stack.pop()  # 최종 값 반환

T = int(input())
for idx in range(1, T+1):
    exp = input()    # 식 받아오기
    expression = []
    a= ''
    # 숫자와 식 따로 분리
    for i in range(len(exp)):
        if exp[i] not in '+-':
            a += exp[i]
            if i == len(exp) -1:
                expression.append(a)
        else:
            expression.append(a)
            expression.append(exp[i])
            a = ''

    # 중위 표기법 -> 후위 표기법 변환
    postfix = infix_to_postfix(expression)

    # 후위 표기법의 수식 계산
    result = cal_postfix(postfix)
    print(result)
    # print(f'#{idx} {result}')
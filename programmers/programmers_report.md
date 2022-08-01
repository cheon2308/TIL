[프로그래머스 신고횟수 ](https://school.programmers.co.kr/learn/courses/30/lessons/92334)

```python
def solution(id_list, report, k):
    answer = [0] * len(id_list) # 결과 도출을 위한 answer 리스트의 길이정의
    report_person = {id: [] for id in id_list} # 신고횟수를 기록할 딕셔너리 길이 정의

    report = set(report) # 중복 제거


    for i in report: 
        new_report = i.split(' ') #공백을 기준으로 신고한 사람과 당한 사람 나눈다.
        report_person[new_report[1]].append(new_report[0]) # 신고당한 사람을 key로 두며 신고한 사람을 value값으로 준다면 value리스트의 길이 = 신고당한 횟수를 알 수 있게된다.

    for key, value in report_person.items(): # 신고 정보가 있는 dictionary를 반복해주며 당한 횟수 >= k라면 answer에 +1을 반영해준다.
        if len(value) >= k:
            for j in value:
                answer[id_list.index(j)] +=1 # answer에 +1을 해주기 위하여 value값을 순회시키며 동일한 이름을 index메서드를 이용하여 찾아준다
                                             # ex) frodo인 경우 id_list의 [1]인덱스값을 가지므로 answer = [0, 1, 0, 0]으로 만들어준다.

    return answer

if __name__ == '__main__':
    print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
```

# 접근 방법

1. 주어진 정보를 적절한 자료형을 이용하여 푸는 문제라고 생각하였습니다.

2. 중복이 없는 -> `set`를 활용하였습니다.

3. `split`을  이용하여 나눠준 report 리스트의 값을 dictionary의 key와 value값으로 받아주며 원하는 결과를 얻을 수 있었습니다.

# 어려웠던 점

1. 아직은 리스트를 이용하여 데이터를 다루는 것이 익숙하여 Dict을 생각하지 못하였고 report를 나눠 담은 리스트에서 count 메서드를 이용하여 결과를 구하려고 하였습니다.

2. 중첩 for를 이용하여 순회를 하다보니 count 메서드의 비교 문자열이 원하는 대로 나오지 않았습니다.

# 해결방법

1. 해결 flow를 다시 그려보며, dict을 통해 데이터 정렬을 해준다면 원하는 값을 도출하기 쉬울 것이라고 생각하였습니다.

2. key, value에 들어갈 값을 헷갈렸지만 `신고당한 사람 : number`로 구성하기 위하여 key=신고 당한 사람, value = 신고한 사람으로 구성하였습니다.

3. append를 이용하여 값을 추가해주었고 len(value)를 통하여 신고받은 횟수 체크, index(인자)를 통하여 answer값을 변환해주었습니다.

# 배운 점

1. 문제를 풀기 전 조건, 주어진 정보를 잘 파악하여 주석 or 메모를 통하여 전체 flow를 그려보는 것이 중요한 것 같습니다.

2. 각 흐름에서 어떤 자료형을 쓸지, 어떤 메서드가 어울리는지 생각을 해보며 여러 방면으로 코딩을 해보았고 잘 짜여진 계획은 문제해결 시간을 줄여준다는 것을 깨달았습니다.





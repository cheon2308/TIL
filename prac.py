def solution(absolutes, signs):
    answer = 0
    
    abosol_num = absolutes
    plus_minus = signs
    for i in range(len(abosol_num)):
        if plus_minus[i] == False:
            abosol_num[i] = -abosol_num[i]
                   
    answer = sum(abosol_num)
    return answer

print(solution([4,5,6],[True,False,True]))
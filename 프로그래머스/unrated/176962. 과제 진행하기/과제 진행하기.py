from datetime import datetime
def solution(plans):
    answer = []
    sus = []
    plans.sort(key = lambda x : x[1])

    for i in range(1, len(plans)):
        tmp = int(( datetime.strptime(plans[i][1],"%H:%M") - datetime.strptime(plans[i-1][1], "%H:%M")).seconds//60)
        if tmp < int(plans[i-1][2]):
            sus.append((plans[i-1][0],(int(plans[i-1][2]) - tmp)))
        else:
            answer.append(plans[i-1][0])
            tmp -= int(plans[i-1][2])
            while sus:
                if tmp >= sus[-1][1]:
                    tmp -= sus[-1][1]
                    answer.append(sus[-1][0])
                    sus.pop()
                else:
                    a,b = sus.pop()
                    sus.append((a,b - tmp))
                    break
    answer.append(plans[-1][0])
    while sus:
        answer.append(sus.pop()[0])
    
    return answer
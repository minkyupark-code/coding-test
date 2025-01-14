def solution(progresses, speeds):
    answer = []
    num = 0
    
    while(sum(answer) != len(progresses)):
        for i in range(len(progresses)):
            progresses[i] = progresses[i] + speeds[i]
            print(progresses)
        
        for j in range(len(progresses)):
            if progresses[j] >= 100:
                num += 1
                
            elif len[progresses] == 0 or progresses[j] < 100:
                answer.append(num)
                num = 0
                break
    return answer

def solution(n, build_frame): #여러분 기둥과 보 난이도 미쳤습니다. 오늘 일하는 중에 하루 종일 풀었습니다. 휴.....
    answer = []
    for build in build_frame:
        if build[3]==1:# [1,0,0,1] 설치 했다는 거
            re3=build[:3]#[1,0,0]
            if re3[2]==0 and 0<=re3[0]<=n and 0<=re3[1]<n:# [1,0,0] 0인 기둥
                if re3 not in answer: # 같은거 겹치면 안됨.
                    if ([re3[0],re3[1]-1,0] in answer) or ([re3[0],re3[1],1] in answer) or ([re3[0]-1,re3[1],1] in answer):#보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다
                        answer.append(re3)
                    elif re3[1]==0:#3 바닥 위에 있거나
                        answer.append(re3)
            elif re3[2]==1 and 0<=re3[0]<n and 1<=re3[1]<=n:# [1,0,1] 1 인 보
                if re3 not in answer: # 같은거 겹치면 안됨
                    if ([re3[0],re3[1]-1,0] in answer) or ([re3[0]+1,re3[1]-1,0] in answer) or (([re3[0]-1,re3[1],1] in answer) and ([re3[0]+1,re3[1],1] in answer)):# 0 인 기둥이 밑에 존재하는가, 양쪽 1인 보 존재하는가
                        answer.append(re3)

        elif build[3]==0: # [1,0,0,0] 삭제했다는거
            rej=build[:3]
            lst=answer.copy()
            if rej in lst:
                lst.remove(rej)
                h=True
                for re3 in lst:
                    if re3[2]==0:# [1,0,0] 0인 기둥
                        if ([re3[0],re3[1]-1,0] in lst) or ([re3[0],re3[1],1] in lst) or ([re3[0]-1,re3[1],1] in lst):#보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다
                            continue
                        elif re3[1]==0:#3 바닥 위에 있거나
                            continue
                        else:
                            h=False
                    elif re3[2]==1:# [1,0,1] 1 인 보
                        if ([re3[0],re3[1]-1,0] in lst) or ([re3[0]+1,re3[1]-1,0] in lst) or (([re3[0]-1,re3[1],1] in lst) and ([re3[0]+1,re3[1],1] in lst)):# 0 인 기둥이 밑에 존재하는가, 양쪽 1인 보 존재하는가
                            continue
                        else:
                            h=False
                if h:
                    answer.remove(rej)
    answer.sort()   
    return answer

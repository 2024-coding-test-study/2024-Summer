import heapq


def solution(sequence, k):
    num=k
    lst=[]
    for i in range(len(sequence)):
        first=i
        while i<len(sequence):
            k-=sequence[i]
            if k<0:
                k=num
                break
            elif k==0:
                last=i
                lst.append([first,last])
                k=num
                break
            i+=1
            
            if i==len(sequence):
                k=num
                break
            
    hqueue = []
    for t in lst:
        diff = t[1] - t[0]
        heapq.heappush(hqueue, (diff, t[0], t))
    result = heapq.heappop(hqueue)
    answer=result[2]
    return answer

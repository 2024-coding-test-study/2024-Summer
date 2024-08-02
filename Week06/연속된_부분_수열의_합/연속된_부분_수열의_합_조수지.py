# 시간초과 ㅠ

from collections import deque

def solution(sequence, k):
  answer = deque([])
  l = 99999 # 부분 수열의 길이 저장할 변수
  
  for i in range(len(sequence)) :
    cur_sum = 0 # 연속된 수열의 합 저장할 변수
    
    for j in range(i, len(sequence)) :
      if sequence[j] > k : # k보다 큰 값을 만나면 종료
        break
      
      cur_sum += sequence[j]
      
      if cur_sum == k : # 합이 k인 부분 수열을 찾았을 때
          if not answer or (j - i + 1) < l : # 최초로 찾은 부분 수열이거나 이전에 찾은 부분 수열보다 짧다면
            if answer : # answer에 이미 존재할 때는
              answer.clear() # 비워줌
              
            answer.append(i)
            answer.append(j)
            l = j - i + 1
            
  return list(answer)
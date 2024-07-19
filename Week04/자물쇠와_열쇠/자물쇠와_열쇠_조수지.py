def solution(key, lock):
  
  # 이런 식으로 하면 key와 lock의 크기가 맞지 않아서 안됨...
  '''
  cnt = 0 # True의 개수를 저장할 변수
  
  # key와 lock을 XOR 연산
  for i in range(len(lock)) :
    for j in range(len(lock)) :
       if lock[i][j] ^ key[i][j] == 1: # XOR 연산의 결과가 1이면 cnt 값을 1 더해줌
         cnt += 1
 
  if cnt == len(lock) * len(lock) :
    answer = True
  else :
    answer = False
  '''
  return answer
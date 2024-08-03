# task 스택 가장 위의 과제가 완료 되는지 확인하는 함수
def check(task) :
  global score
  
  if task :
      current_task = task.pop()
      a, t = current_task
      t -= 1
      
      if t > 0 :
        task.append((a, t))
      else :
        score += a

import sys
input = sys.stdin.readline # 이걸 안하면 시간 초과 뜸
        
n = int(input()) # 이번 학기가 몇 분인지 나타내는 변수 입력 받기
task = [] # 과제 저장할 리스트
score = 0 # 과제 점수 저장할 변수
        
for i in range(n) :
  INPUT = list(map(int, input().split()))
  
  if INPUT[0] == 1 :
    task.append((INPUT[1], INPUT[2]))
    
    check(task)
        
  elif INPUT[0] == 0 :
    check(task)
    
print(score)
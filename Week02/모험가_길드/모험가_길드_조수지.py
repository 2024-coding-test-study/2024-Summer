#20분 걸림

n = int(input())
x = list(map(int, input().split()))

# 여행을 떠날 수 있는 그룹 수의 최댓값을 알아내야 하기에 내림차순 정렬
x.sort(reverse=True)

cnt = 0
index = 0

for i in range(n) :
  if index >= n :
    break
  
  index = index + x[index] 
  cnt += 1
  
print(cnt)
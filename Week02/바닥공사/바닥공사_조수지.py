# 18분 걸림
'''
n = int(input())
cnt = 0

if n % 2 == 0 :
  #2x2로만 다 채우는 경우 -> 1
  #2x1로만 다 채우는 경우 -> 1
  #1x2로만 다 채우는 경우 -> 1
  #1x2와 2x1로 채우는 경우
  #1x2와 2x2로 채우는 경우
  #2x1와 2x2로 채우는 경우
  #세개로 채우는 경우
  
else :
  #2x1로만 다 채우는 경우 -> 1
  #1x2와 2x1로 채우는 경우
  #2x1와 2x2로 채우는 경우
  #세개로 채우는 경우
'''
 
# 다이나믹만 보면 머리가 움직이지 않는다.....
# 책과 같다 
n = int(input())

d = [0] * 1001
d[1] = 1 # 가로가 1일때는 무조건 한가지 경우만 존재
d[2] = 2 # 가로가 2일때는 두가지 경우만 존재

for i in range(3, n + 1) :
  d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796
  
print(d[n])
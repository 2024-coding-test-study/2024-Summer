'''
# 무언가 잘못됐음을 깨달음
x = int(input())
cnt = 0

while x > 1 :
  if x % 5 == 0 :
    x /= 5
    cnt += 1
    print(x)
  elif x % 3 == 0 :
    x /= 3
    cnt += 1
    print(x)
  elif x % 2 == 0 :
    x /= 2
    cnt += 1
    print(x)
  else :
    x -= 1
    cnt += 1
    print(x)
   
print(" ") 
print(cnt)
'''

# 잘 이해가 안돼서 한참동안 보고 있었음
# 책과 같은 코드. 
x = int(input())

d = [0] * 30001

# 2부터 x까지 반복
# 각 연산에서 1을 더해주는 이유는 연산 횟수 1임
for i in range (2, x + 1) :
  d[i] = d[i-1] + 1 # 1을 뺀 경우 
  
  if i % 2 == 0 : # 2로 나눠 떨어지는 경우
    d[i] = min(d[i], d[i//2] + 1)
    
  if i % 3 == 0 : # 3으로 나눠 떨어지는 경우
    d[i] = min(d[i], d[i//3] + 1)
    
  if i % 5 == 0 : # 5로 나눠 떨어지는 경우
    d[i] = min(d[i], d[i//5] + 1)
    
#바텀업 방식으로 최소 연산 횟수를 구함.
print(d[x])


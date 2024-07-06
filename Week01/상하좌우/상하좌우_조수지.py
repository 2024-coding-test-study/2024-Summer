n = int(input()) #공간의 크기 입력 받기. n x n
a = input().split() #L, R, U, D 입력받기
x, y = 1, 1 #시작점 위치

for i in range(len(a)):
  if a[i] == 'L' and y > 1 and y <= n :
    y -= 1
  elif a[i] == 'R' and y < n and y > 0 :
    y += 1
  elif a[i] == 'U' and x > 1 and x <= n :
    x -= 1
  elif a[i] == 'D' and x < n and x > 0 :
    x += 1
    
print(x, y)
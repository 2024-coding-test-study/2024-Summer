#바닥을 채우는 경우
#i-1까지 채워진 경우 1가지(가로가 1인경우)
#i-2까지 채워진 겨우 2가지(1X2, 2X2, 2X1이 두개인 경우는 이미 i-1에서 고려되어짐)
#점화식 = a[i] = a[i-1] + a[i-2]*2

n = int(input())
lst = [0] *1001 # n <= 1000
lst[1] = 1
lst[2] = 2
for i in range(3, n+1):
  lst[i] = lst[i-1] + lst[i-2] * 2

print(lst[n])
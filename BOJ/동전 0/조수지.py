n, k = map(int, input().split()) 
coin = []

# n가지 종류의 동전 입력받기
for i in range(n) :
    coin.append(int(input()))

cnt = 0

# 큰 동전부터 k와 비교해나감
for i in range (n - 1, - 1, -1) :
  if coin[i] > k : # k보다 동전이 크면 무시
    continue
  
  val = k // coin[i]
  cnt += val
  k -= val * coin[i]
  
print(cnt)
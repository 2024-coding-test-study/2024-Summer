#소수의 합으로 나타낼 수 있는 경위의수
import sys
n = int(sys.stdin.readline().rstrip())
#소수 찾아서 배열에 저장 -> 이게 시간초과의 원인이였음 소수를 어떻게 효율적으로 찾을것인가...
primes = [False, False] + [True] * (n-1)
data = []
for i in range(2, n+1):
    if primes[i]:
        data.append(i)
       
        j = 2
        while i*j <= n:
            primes[i*j] = False
            j += 1


start, end = 0, 0
total = 0
cnt = 0
while start <= end:
  if total == n: #start 포인터 이동해서 다른 구간도 가능한지 검사
    total -= data[start]
    start += 1
    cnt += 1
  elif total < n:
    if end >= len(data):
      break
    total += data[end]
    end += 1
    
  elif total > n:
    total -= data[start]
    start += 1

print(cnt)
t = int(input()) # 테스트케이스 수

for _ in range(t) :
  n = int(input()) # 날 수 입력받기
  prices = list(map(int, input().split())) # 각 날의 주가 입력받기
  
  max_price = 0
  benefit = 0
  
  for i in range(n - 1, -1, -1) : # 미래에서 현재로 주가를 확인하며
    if prices[i] > max_price :
      max_price = prices[i]
      
    # 미래에서부터 주가를 확인하기 때문에 가능.
    # 만약 첫날의 주가가 가장 높고 갈수록 하락세를 탄다면(ex) [10, 7, 6]) max_price가 6, 7, 10 순으로 갱신. benefit은 결과적으로 0이 됨
    # 만약 마지막날의 주가가 가장 높을 때(ex) [3, 5, 9]) max_price는 9이므로 benefit은 결과적으로 10이 됨
    # 만약 최고가가 중간에 끼여 있다면(ex) [1, 1, 3, 1, 2]) max_price는 2, 3 순으로 갱신. 
    # 2일 때 1을 만나 이익이 1이고 3일때 1을 두 번 만나 각각 1, 2의 이익. benefit은 결과적으로 5가 됨
    benefit += max_price - prices[i]
    
  print(benefit)
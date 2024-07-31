from collections import deque

n = int(input()) # 카드 묶음의 개수 입력받기
cards = []

for i in range(n) :
  cards.append(int(input()))

cards.sort() # 오름차순 정렬
sort_cards = deque(cards) # deque로 변환

result = 0

while len(sort_cards) > 1 :
  sum = sort_cards.popleft() + sort_cards.popleft() # 가장 왼쪽의 카드뭉치 2개를 더해줌
  result += sum
  
  l, r = 0, len(sort_cards)
  
  while l < r : # 합친 묶음이 들어갈 자리를 찾기 위해서 이진 탐색
    mid = (l + r) // 2
    
    if sort_cards[mid] < sum :
      l = mid + 1
    else :
      r = mid
  
  sort_cards.insert(l, sum) # 삽입
  
print(result)
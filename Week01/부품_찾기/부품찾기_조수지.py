""" # 처음 생각한 코드 (이진 탐색 X)
n = int(input())
shop = list(map(int, input().split()))
m = int(input())
guest = list(map(int, input().split()))

for i in range(m) :
  if guest[i] in shop :
    print("yes", end=' ')
  else :
    print("no", end=' ')
"""

# 이진 탐색 사용한 코드
def b_search(arr, val, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == val:
            return True
        elif arr[mid] > val:
            end = mid - 1
        else:
            start = mid + 1

    return False

n = int(input())
shop = list(map(int, input().split()))
m = int(input())
guest = list(map(int, input().split()))

# shop 리스트 오름차순 정렬
shop = sorted(shop)

for i in range(m):  # guest 리스트 값만큼 반복
    if b_search(shop, guest[i], 0, n - 1):
        print("yes", end=' ')
    else:
        print("no", end=' ')

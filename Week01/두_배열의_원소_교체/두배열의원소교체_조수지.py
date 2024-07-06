"""
#첫번째 시도 (정렬을 안함)
n, k = map(int, input().split())  # n개의 원소, 최대 k번까지 바꿔치기 연산 가능
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# 최대 k번 바꿔치기 연산 수행
for _ in range(k):
    min_a = min(a)
    max_b = max(b)
    
    # a의 최솟값이 b의 최댓값보다 작을 경우에만 교환
    if min_a < max_b:
        min_a_index = a.index(min_a)
        max_b_index = b.index(max_b)
        
        # 교환
        a[min_a_index], b[max_b_index] = b[max_b_index], a[min_a_index]
    else:
        break

print(sum(a))
"""

#두번째 시도 (정렬o)
n, k = map(int, input().split())  # n개의 원소, 최대 k번까지 바꿔치기 연산 가능
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a는 오름차, b는 내림차순 정렬
a.sort()
b.sort(reverse=True)

for i in range(k) : 
    if a[i] < b[i] : # a[i]가 b[i]보다 작은 값이면 교체해 줌
        a[i], b[i] = b[i], a[i]
        
print(sum(a))
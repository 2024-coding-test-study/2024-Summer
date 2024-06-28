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
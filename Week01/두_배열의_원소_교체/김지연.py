# 풀이시간: 20m 32s
# 약간 고민된던것: 최대 k번 교체할 수 있단말은 k까지 교체안하고 a배열을 최대로 만들 수 있다는 경우가 있다는것 -> a와 b를 계속 비교하면서
#a = [6, 4, 3, 3]
#b = [5, 3, 2, 2]
#일경우  첫번재 교환 a = [6, 5, 3, 3], b = [4, 3, 2, 2]일 텐데 이때 b[0]과 adml [2]를 교환하는게 최댓값을 구할 수 있는거 아닌가?

#첫번째 풀이 -> 시간복잡도가 많이 나옴.. 이렇게 복잡하나? 다시 풀어봄
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

idx_a = 0
idx_b = 0
while k != 0 and idx_a < n:
  if a[idx_a] < b[0]:
    a[idx_a], b[0] = b[0], a[idx_a]
    idx_a += 1
    k -= 1
    b.sort(reverse=True) #-> 정렬할 필요가 없음 -> a와 바꾸
  else:
    idx_a += 1
      
print(sum(a))


#두번째 풀이 -> a가 오름차순인걸 간과함 -> b와 같은 인덱스로 비교해서 b보다 작으면 교체(a다음 인덱스는 교체된 원소보다 무조건 크니까 b를 다시 정렬할 필요가 없음)b보다 크면 b의 모든 원소가 a의 가장 작은 원소보다 작으므로 교체할 필요가 없음.
for i in range(k):
  if a[i] < b[i]:
    print(a)
    a[i], b[i] = b[i], a[i]
  else: #a의 가장 작은 원소가 b의 가장 큰 원소보다 크니까 b에는 a보다 큰 원소가 없음
    break
print(sum(a))
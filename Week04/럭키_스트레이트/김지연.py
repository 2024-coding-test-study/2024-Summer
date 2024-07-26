#n의 자릿수를 알아낸후 반으로 나눈 인덱스를 기준으로 자릿수 덧셈
#time: 4m 49s
n = input()
left = map(int, list(n[:len(n)//2]))
right = map(int, list(n[len(n)//2:]))
if sum(left) == sum(right):
  print("LUCKY")
else:
  print("READY")
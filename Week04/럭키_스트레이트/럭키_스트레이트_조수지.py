# 8분 소요
score = list(map(int, input()))
left, right = 0, 0
mid = len(score) / 2

for i in range(len(score)) :
  if i < mid :
    left += score[i]
  else :
    right += score[i]
    
if left == right :
  print("LUCKY")
else :
  print("READY")
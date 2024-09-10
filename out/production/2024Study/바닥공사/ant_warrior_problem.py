d=[0]*100
n=int(input())
lst=list(map(int,input().split()))

d[1]=lst[0]
d[2]=max(lst[0],lst[1])
for i in range(3,n+1):  
    d[i]=max(d[i-2]+lst[i-1],d[i-1])
print(d[n])
# 이문제는 해설을 참고안하고 혼자 알아냈다. 점화식을 세워서 차근 차근 풀면 답이 보인다.
#점화식의 형태는 An=A(n-1)+A(n-2) 같은 덧셈 곱셈과 같은 사칙연산 형태 일수도 있고 An=min or max(An,A(n-1)) 같은 둘의 크기 비교형태일수도 있다.

x=int(input())
dp=[0]*100
for i in range(2,x+1):
    dp[i]=dp[i-1]+1
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
    elif i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    elif i%5==0:
        dp[i]=min(dp[i],dp[i//5]+1)
    

print(dp[x])
#솔직히 다른방법으로 풀어볼려고 했는데 잘 안됐다. 이 방법 말고는 더 좋은 방법이 있는지는 모르겠다.
    

'''
N개의 카드개수 중 3개를 선택해 
그 합이 M을 넘지 않고, M에 가장 가까운 수를 구해라
'''

N, M = map(int,input().split())
arry =list(map(int,input().split()))
result = 0

for i in range(N-2):
  for j in range(i+1,N):
    for k in range(j+1,N):
      if arry[i]+arry[j]+arry[k] <= M:
        result = max(result,arry[i]+arry[j]+arry[k])

print(result)

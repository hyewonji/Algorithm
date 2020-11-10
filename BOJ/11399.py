'''
Greedy

N명이 현금인출기에서 돈을 뽑는데 걸리는 시간이 각각 주어진다
1번째 사람부터 N번째 사람까지 각각 돈 뽑는데 걸리는 시간의 합의 최솟값 구하기
'''


N = int(input())
arry = sorted(map(int, input().split()))[::-1]
result = 0

for i in range(N):
  result += arry[i]*(i+1)
 
print(result)

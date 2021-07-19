'''
정수 수열 A가 주어진다. 
수열 A의 해당 항까지의 평균값을 그 항으로 하는 정수 수열 B가 있다.

수열 B가 주어졌을 때, 수열 A를 구해라.
'''

N = int(input())
arr = list(map(int,input().split()))
currentSum = 0
answer = []


for i, v in enumerate(arr):
  answer.append(v*(i+1)-currentSum)
  currentSum = v*(i+1)
print(*answer)

'''
Greedy

동전의 종류와 금액을 입력받아 
금액에 맞는 돈을 만들기 위한 최소한의 동전 개수 찾기
'''



N, K = map(int,input().split())
arry = list(int(input()) for _ in range(int(N)))
result=0

for i in arry[::-1]:
  if i <= K:
    result += int(K/i)
    K = K%i

print(result)

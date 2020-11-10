'''
Greedy

숫자 N을 5와 3으로 분배할 때 
나올 수 있는 최소한의 개수
'''


N = int(input())
a = int(N/5)

for i in range(a,-1,-1):
  b = N-(5*i)
  if (b%3) == 0:
    result = i + (b/3)
    break

try:
  print(int(result))
except:
  print(-1)

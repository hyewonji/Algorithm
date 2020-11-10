'''
Greedy

양의 정수가 주어질 때, 피보나치 수들의 합이 주어진 정수와 같게 되는 최소 개수의 서로 다른 피보나치 수들을 구하라. 
양의 정수 n의 최대값은 1,000,000,000이다.

**
1,000,000,000이하의 피보나치 수열을 입력하고
for문을 사용하는게 시간단축이 됐다.
**
'''




N=int(input())

for n in range(N):
  num = int(input())
  i = 0
  k = 1
  arry=[]
  result = []
  while (i+k)<=num:
    temp = k
    k = i+k
    i = temp
    arry.append(k)

  st = len(arry)-1

  while num>0:
    if (num-arry[st])>=0:
      result.append(arry[st])
      num = num-arry[st]
    if num == 0:
      break
    st -= 1

  print(*result[::-1])
  
  
  
N=int(input())
arry=[0,1]

for i in range(2,46):
  arry.append(arry[i-2]+arry[i-1])
  
for n in range(N):
num = int(input())
result = []
st = len(arry)-1

while num>0:
  t = arry[st]
  if (num>t):
    result.append(t)
    num = num-t
  if num == 0:
    break
  st -= 1

print(*result[::-1])

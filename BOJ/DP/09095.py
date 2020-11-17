'''
DP

정수 n이 주어졌을 때, 
n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하라.

**n이 1, 2, 3, 4 로 증가할때 규칙 찾기**
n의 방법의 수는 {(n-1)의 방법의수 + (n-2)의 방법의수 + (n-3)의 방법의수}로 구한다. 
'''



T = int(input())
arry = [1,2,4]

for i in range(3,10):
  arry.append(arry[i-1]+arry[i-2]+arry[i-3])

for i in range(T):
  print(arry[int(input())-1])

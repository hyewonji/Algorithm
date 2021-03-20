'''
세자리 자연수가 주어질때, 각자리수의 곱과 합을 나타내라
'''

N1 = int(input())
N2 = input()[::-1]
arry = []

for i in range(len(N2)):
  arry.append(N1 * int(N2[i])*(10**i))
  print(N1 * int(N2[i]))

print(sum(arry))

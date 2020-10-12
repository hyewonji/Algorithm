'''
245의 분해합은 256(=245+2+4+5)이 된다.
이와같이 주어진 N의 분해합중 최소값을 찾아라
'''


N = int(input())
i=0

def get_devided_num(num):
  devided_num = sum(list(map(int,str(num)))) + i
  return(devided_num)

while get_devided_num(i) != N:
  if i == N:
    i=0
    break
  else:
    i += 1

print(i)

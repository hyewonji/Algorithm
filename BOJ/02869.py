'''
A, B, V가 공백으로 구분되어서 주어짐
낮에 A미터 올라가고 밤에 B미터 미끄러진다. 
또, 정상에 올라간 후에는 미끄러지지 않는다.
달팽이가 나무 막대를 모두 올라가려면, 며칠이 걸릴까?
'''

import math
ABV=input().split()
abv=[]

for i in ABV:
  abv.append(int(i))

print(math.ceil((abv[2]-abv[0])/(abv[0]-abv[1]))+1)

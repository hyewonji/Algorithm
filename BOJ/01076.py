'''
저항은 색 3개를 이용해서 그 저항이 몇 옴인지 찾기
'''


N = list(input() for _ in range(3))
color = [
  'black','brown','red','orange','yellow','green','blue','violet','grey','white'
]

second = color.index(N[1])*(10**color.index(N[2]))
first = color.index(N[0])*(10**color.index(N[2]))*10

print(first + second)

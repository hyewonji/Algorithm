'''
주어진 시간에서 45분 전 시간 출력
'''

HM = input().split()
result = []

if int(HM[0]) == 0:
  if int(HM[1]) >= 45:
    h = 0
    m = int(HM[1])-45
    print(h,m)
  else:
    h = 23
    m = int(HM[1])+60-45
    print(h,m)
else:
  if int(HM[1]) >= 45:
    h = int(HM[0])
    m = int(HM[1])-45
    print(h,m)
  else:
    h = int(HM[0])-1
    m = int(HM[1])+60-45
    print(h,m)

N = input()
n=0

if int(N)>=10:
  T = int(N[0])+int(N[1])
  M = N
else:
  T = int(N)
  N = '0'+N
  M = N


while True:
  if T>=10:
    N = N[1]+str(T%10)
    T = int(N[0])+int(N[1])
    n+=1
  else:
    N = N[1]+str(T)
    T = int(N[0])+int(N[1])
    n+=1
  if N==M:
    break

print(n)

A = input()
alp = [-1]*26
for i in A:
  alp[ord(i)-ord('a')]=A.index(i)
print(*alp)

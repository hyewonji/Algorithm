'''
알고리즘 분류 : 정렬 , 이진탐색

N개의 숫자배열 arr, M개의 숫자 배열 test_arr가 주어진다.
test_arr의 숫자가 arr 배열에 존재하면 1, 존재하지 않으면 0을 출력한다.
숫자카드는 -10,000,000보다 크거나 같고, 10,000,000보다 작거나 같다.
'''

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
test_arr = list(map(int, input().split()))


for i in test_arr:
  low, high = 0, N
  while low <= high:
    mid = (low + high) // 2
    if 0 <= mid < N:
      if arr[mid] < i:
        low = mid + 1
      else:
        high = mid -1
    else: break
    
  if 0 <= high + 1 < N:
    if arr[high + 1] == i: print(1, end=" ")
    else: print(0, end=" ")
  else: print(0, end=" ")

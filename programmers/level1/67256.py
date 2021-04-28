'''

1. 왼손으로 누를 수 있는 숫자 : 1, 4, 7
2. 오른손으로 누를 수 있는 숫자 : 3, 6, 9
3. 그 외의 숫자(2, 5, 8, 0)는 현재 위치에서 더 적게 움직일 수 있는 손을 사용해 누른다.
  1. 움직여야하는 거리가 같다면 변수 hand에 저장되어있는 손으로 누른다.
  
'''

def get_hand(hand,left_distance,right_distance):
  if left_distance > right_distance:
    return 'R'
  elif left_distance < right_distance:
    return 'L'
  else:
    return 'L' if hand == 'left' else 'R'


def get_distance(position, left, right):

  x_left = (position-left)%3
  x_right = (right-position)%3
  y_left = abs((position-left)//3)
  y_right = abs((right-position)//3)

  left_distance = x_left + y_left
  right_distance = x_right + y_right
  
  return {
    'left_distance' : left_distance,
    'right_distance' : right_distance 
  }


def solution(numbers, hand):
  numbers_left = [1, 4, 7]
  numbers_right = [3, 6, 9]

  position = {'L': 10, 'R': 12}
  answer = ''
  
  for i in numbers:
    if i == 0:
      i = 11

    if i in numbers_left:
      answer += 'L'
      position['L'] = i
    elif i in numbers_right:
      answer += 'R'
      position['R'] = i
    else:
      distance = get_distance(i,position['L'],position['R'])
      selected_hand = get_hand(hand,distance['left_distance'],distance['right_distance'])
      answer += selected_hand
      position[selected_hand] = i  

  return answer

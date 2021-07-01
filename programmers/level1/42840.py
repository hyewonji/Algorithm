def solution(answers):
  first = [1,2,3,4,5]
  second = [2,1,2,3,2,4,2,5]
  third = [3,3,1,1,2,2,4,4,5,5]
 
  first_len = len(first)
  second_len = len(second)
  third_len = len(third)
  
  score = [0,0,0]
  answer = []

  for (i,v) in enumerate(answers):
    if first[i%first_len] == v:
      score[0] += 1

    if second[i%second_len] == v:
      score[1] += 1
    
    if third[i%third_len] == v:
      score[2] += 1

  for i,v in enumerate(score):
    if v == max(score):
      answer.append(i+1)

  return answer

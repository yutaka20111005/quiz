from question_lambda import *
from r_answer_lambda import *

for i in range(3):
  print(QUESTION[i])
  ans = input()
  if ans == R_ANS[i] or ans == R_ANS2[i] or ans == R_ANS3[i]:
    print("正解です")
  else:
    print("不正解です")

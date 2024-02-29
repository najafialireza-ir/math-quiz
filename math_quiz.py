
"""ask random question number between 1, 9 
             and random choice of math oprator"""

import random
import time


def question_generator():
    a = random.randint(1, 9)
    b = random.randint(1, 9)

    operator_list = ["+", "-", "*"]
    selected_operator = random.choice(operator_list)
    
    print(f"{a} {selected_operator} {b} = ?")
    
    if selected_operator == "+":
        return a + b
    elif selected_operator == "-":
        return a - b
    else:
        return a * b
    
        
    
question_number_limit = 5
question_number = 0

score = 0
time_limit = 10


while question_number < question_number_limit:
    
    result = str(question_generator())
    start_time = time.time()
    
    # get user number 
    user_answer = input(f"Please Enter your answer: ")
    end_time = time.time()
    time_dif = float(end_time - start_time)
    
    # check time and user answer
    if time_limit > time_dif:
        if result == user_answer:
            score += 1
            print(f"Correct => your score is: {score} , and Elapsed time is: {time_dif:.0f}sec")
        else:
            print("Your answer is wrong!")
    else:
        print("Your time is passed!")
        
        
    question_number += 1
    
    
print(f"Finally score:{score} out of{question_number_limit}")
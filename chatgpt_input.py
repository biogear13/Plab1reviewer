import numpy as np
import pandas as pd
import re
working_df = pd.read_csv('plab_chatgpt.csv')
# random question generator
import random
def random_question(df):
    random_number = random.randint(0,len(df))
    print(f'Index is {random_number}')
    print(df['question'][random_number])
    print(df['a'][random_number])
    print(df['b'][random_number])
    print(df['c'][random_number])
    print(df['d'][random_number])
    print(df['e'][random_number])
    print(df['f'][random_number])
    print(df['g'][random_number])
    print(df['h'][random_number])
    print(df['i'][random_number])
    print(df['j'][random_number])
    print(df['k'][random_number])
    print(df['l'][random_number])
    print(df['m'][random_number])
    x = input('What is your answer?: ')
    print(df['answer'][random_number])
    if np.isnan(df['chatgpt'][random_number]):
        df['chatgpt'][random_number]=input('What does your research say?: ')
    else:
        print(df['chatgpt'][random_number])
    if np.isnan(df['final_answer'][random_number]):
        df['final_answer'][random_number]=input('What is the correct answer?: ')
    else:
        print(f"The correct answer is {df['final_answer'][random_number]}")
    if x==df['final_answer'][random_number]:
        return 'y'
num_questions=int(input('How many questions do you want to answer?(intiger): '))
correct_answer=0
for i in range(num_questions):
    print(f'Question # {i+1} of {num_questions}')
    self_check=random_question(working_df)
    if self_check=='y':
        correct_answer+=1
print(f'You got {round(correct_answer/num_questions*100,2)}% correct.')
working_df.to_csv('plab_chatgpt.csv', index=False)
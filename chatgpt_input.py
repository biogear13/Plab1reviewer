import numpy as np
import pandas as pd
import re
working_df = pd.read_csv('plab_chatgpt.csv')
# random question generator
import random
def random_question(df):
    answered = pd.read_csv('answered.csv')
    if answered['answered'].isnull().sum()==0:
        answered = answered.drop(['answered', 'correct', 'wrong'], axis=1)
        answered['answered'] = []
        answered['correct'] = []
        answered['wrong'] = []
    random_number = random.randint(0,len(df)-1)
    while answered.loc[random_number,'answered'] == 1:
        random_number = random.randint(0,len(df))
    print(f'Index is {random_number}')
    print(df['question'][random_number])
    print(df['a'][random_number])
    print(df['b'][random_number])
    print(df['c'][random_number])
    if df['d'][random_number]!='nan':
        print(df['d'][random_number])
    if df['e'][random_number]!='nan':
        print(df['e'][random_number])
    if df['f'][random_number]!='nan':
        print(df['f'][random_number])
    if df['g'][random_number]!='nan':
        print(df['g'][random_number])
    if df['h'][random_number]!='nan':
        print(df['h'][random_number])
    if df['i'][random_number]!='nan':    
        print(df['i'][random_number])
    if df['j'][random_number]!='nan':
        print(df['j'][random_number])
    x = input('What is your answer?: ').lower()
    print(f"The key is {df.loc[random_number,'gpt_letter']}")
    print(df.loc[random_number, 'chat'])
    answered.at[random_number,'answered'] = 1
    print(answered.loc[random_number,'answered'])
    answered.to_csv('answered.csv', index=False)
    print(f"total reviewed question: {answered['answered'].notnull().sum()}")
    if x==df.loc[random_number,'gpt_letter']:
        answered.at[random_number, 'correct'] = 1
        answered.to_csv('answered.csv', index=False)
        c=answered['correct'].notnull().sum()
        w=answered['wrong'].notnull().sum()
        print(f"total correct answer: {c} ({round(c/(c+w)*100,2)}%)")
        return 'y'
    else:
        answered.at[random_number, 'wrong'] = 1
        answered.to_csv('answered.csv', index=False)
        c=answered['correct'].notnull().sum()
        w=answered['wrong'].notnull().sum()
        print(f"total correct answer: {c} ({round(c/(c+w)*100,2)}%)")
num_question=1
correct_answer=0
stop = 0
while stop == 0:
    print(f'Question # {num_question}')
    self_check=random_question(working_df)
    if self_check=='y':
        correct_answer+=1
    answered = pd.read_csv('answered.csv')
    if answered['answered'].isnull().sum()==len(answered):
        print('You have finished all the questions in this round.')
        stop=1
        break        
    s = input('Do you want to continue? (y/n): ').lower()
    if s=='n':
        stop=1
    num_question+=1
print(f'You got {round(correct_answer/(num_question-1)*100,2)}% correct for this round.')
working_df.to_csv('plab_chatgpt.csv', index=False)
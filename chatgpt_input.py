import numpy as np
import pandas as pd
import re
working_df = pd.read_csv('plab_chatgpt.csv')
# random question generator
import random
def random_question(df):
    answered = pd.read_csv('answered.csv')
    if answered['answered'].isnull().sum()==0:
        answered = answered.drop('answered', axis=1)
        answered['answered'] = []
    random_number = random.randint(0,len(df))
    while answered.loc[random_number,'answered'] == 'y':
        random_number = random.randint(0,len(df))
    answered.loc[random_number,'answered'] == 'y'
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
    print(f"The key is {df.loc[random_number,'key_letter']}")
    print(df.loc[random_number, 'chat'])
    answered.to_csv('answered.csv', index=False)
    if x==df.loc[random_number,'key_letter']:
        return 'y'
num_question=1
correct_answer=0
stop = 0
while stop == 0:
    print(f'Question # {num_question}')
    self_check=random_question(working_df)
    if self_check=='y':
        correct_answer+=1
    s = input('Do you want to continue? (y/n): ').lower()
    if s=='n':
        stop=1
    num_question+=1
print(f'You got {round(correct_answer/(num_question-1)*100,2)}% correct.')
working_df.to_csv('plab_chatgpt.csv', index=False)
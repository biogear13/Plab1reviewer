
from flask import Flask, render_template, request, session, redirect, url_for
import pandas as pd
import random
import os
#from dotenv import load_dotenv
#load_dotenv()

app = Flask(__name__)
app.secret_key = 'SUPER_SECRET_KEY'  # Change this!

def random_question(df):
    answered = pd.read_csv('answered.csv')
    if answered['answered'].isnull().sum()==0:
        answered = answered.drop('answered', axis=1)
        answered['answered'] = []
    random_number = random.randint(0,len(df))
    while answered.loc[random_number,'answered'] == 'y':
        random_number = random.randint(0,len(df))
    answered.loc[random_number,'answered'] == 'y'

    question = df['question'][random_number]
    options = {'a': df['a'][random_number],
               'b': df['b'][random_number],
               'c': df['c'][random_number]}

    for letter in 'defghij':
        if df[letter][random_number] != 'nan':
            options[letter] = df[letter][random_number]
    key = df.loc[random_number,'key_letter']
    chat = df.loc[random_number, 'chat']
    
    answered.to_csv('answered.csv', index=False)
    
    return question, options, key, chat

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        answer = request.form['answer'].lower()
        correct_answer = session.get('correct_answer')
        if answer == correct_answer:
            return render_template('correct.html', answer=answer, explanation=chat)
        else:
            return render_template('incorrect.html', answer=answer, correct_answer=correct_answer, explanation=chat)

    working_df = pd.read_csv('plab_chatgpt.csv')
    question, options, correct_answer, chat = random_question(working_df)
    session['correct_answer'] = correct_answer  # Save correct answer in session
    return render_template('quiz.html', question=question, options=options)


if __name__ == '__main__':
    app.run(debug=True)

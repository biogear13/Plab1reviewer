import numpy as np
import pandas as pd
import re
working_df = pd.read_csv('plab_final.csv')
working_df['chatgpt'][415]=input('Chatgpt answer:')
working_df.to_csv('plab_chatgpt.csv')
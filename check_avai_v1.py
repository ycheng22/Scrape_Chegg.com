# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 18:11:56 2021

@author: Yunpeng Cheng

@E_mail: ycheng22@hotmail.com

Reference:
"""
import pandas as pd

sub_folder = './April3/'
df_question_link = pd.read_csv(sub_folder + 'question_April_3.csv', encoding = "charmap")
###charmap, windows-1252, utf-8
df_question_link['question'] = df_question_link['question'].str.lower()

#########################################################################
Q1 = ['x kg object','3.00, 0', 'm/s collides', 'y kg', '1.25', 'angleof 30', 'y component']

Q2 = ['6000 kg truck', 'x, y', '2500 kg car', 'a, b', 'stuck together', 'after the collision']

Q3 = ['6000 kg truck', 'velocity of x', '2500 kg car', 'moving at y', 'stuck together', 'energy was lost']

Q4 = ['x kg car', 'traveling at 20.0', 'hits a giant rubber ball', 'mass x/1000', 'sitting motionless', 'ratio of the velocity']

Q5 = ['5.00 g bullet', 'shot vertically', 'x kg wooden block', 'stays embedded', 'lifts upward a distance 8.00', 'bullet just before']

Q6 = ['x-kg crate', 'frictionless surface', 'an angle of Y', 'constant external', 'constant external', 'crate a distance of 3.000 m', 'incline at constant speed']

Q7 = ['two horses', 'pull a canal boat', '745.7 w', 'constant velocity of x', 'angle between the motion', 'ropes is y', 'tension in each rope']
#########################################################################
Q = [Q1, Q2, Q3, Q4, Q5, Q6, Q7]
for idx_Q in range(7):
    check_qst = Q[idx_Q]
    out_filename = sub_folder + 'Q' + str(idx_Q+1) + '_same.csv'
    list_in = []
    for idx in range(len(df_question_link)):
        cnt_in = 0
        q_txt = df_question_link.loc[idx]['question']
        for ele in check_qst:
            if ele in q_txt:
                cnt_in = cnt_in + 1
        if cnt_in >= 2:
            list_in.append(df_question_link.loc[idx])
            print(f'Q {idx_Q+1} has same')
            txt_name = f'Q{idx_Q+1}_has_same.txt'
            with open(sub_folder + txt_name, 'w') as a:
                a.close()
    df_in = pd.DataFrame(list_in)
    df_in.to_csv(out_filename)   
        
    
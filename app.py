import streamlit as st
import pickle
import pandas as pd


teams=['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']


cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']





st.title('IPL Win Predictor')
pipe=pickle.load(open('pkl_file/matchwinpredictormodel(pip).pkl','rb'))
col1,col2 = st.columns(2)

with col1:
    batting_team=st.selectbox('Select Batting team',sorted(teams))
with col2:
    bowling_team=st.selectbox('Select Bowling team',teams)

selected_city=st.selectbox("Select Host City",sorted(cities))

target=st.number_input("Target")

col3,col4,col5=st.columns(3)

with col3:
    score=st.number_input("Score")
with col4:
    overs=st.number_input("Overs Completed")
    if overs ==0:
        overs=1
with col5:
    wicket=st.number_input("Wickets Out")
if st.button("Prdict Probaility"):
    runs_left=target-score
    balls_left=120-(overs*6)
    wickets=10-wicket
    crr=score/overs
    rrr=runs_left*6/(balls_left)

    input_df=pd.DataFrame({'batting_team':[batting_team],
    'bowling_team':[bowling_team],
    'city':[selected_city],
    'runs_left':[runs_left],
    'bowls_left':[balls_left],
    'wickets':[wickets],
    'total_runs_x':[target],
    'curr_run_rate':[crr],
    'requ_run_rate':[rrr]
    })
    result=pipe.predict_proba(input_df)
    # st.table(input_df)
    loss=result[0][0]
    win=result[0][1]

    st.header(batting_team + '- ' + str(round(win*100)) +'%')
    st.header(bowling_team+ '- ' + str(round(loss*100)) +'%')

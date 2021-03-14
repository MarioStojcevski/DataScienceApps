import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def file_download(df):
	csv = df.to_csv(index=False)
	b64 = base64.b64encode(csv.encode()).decode()
	href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download file</a>'
	return href



st.title('NBA Player Stats Explorer')

st.markdown("""
	Mario's quick app for NBA Players :)
""")

st.sidebar.header('User Inputs')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2021))))


@st.cache
def load_data(year):
	url = 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_per_game.html'
	html = pd.read_html(url, header = 0)
	df = html[0]
	raw = df.drop(df[df.Age == 'Age'].index)
	raw = raw.fillna(0)
	player_stats = raw.drop(['Rk'], axis = 1)
	return player_stats

player_stats = load_data(selected_year)

#

sorted_unique_team = sorted(player_stats.Tm.unique())
selected_team = st.sidebar.multiselect('Team', sorted_unique_team)

unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos)

df_selected_team = player_stats[(player_stats.Tm.isin(selected_team)) & (player_stats.Pos.isin(selected_pos))]

st.header('Display Player Stats of Selected')
st.write('Data size: ' + str(df_selected_team.shape[0]) + ' x ' + str(df_selected_team.shape[1]))
st.dataframe(df_selected_team)

st.markdown(file_download(df_selected_team), unsafe_allow_html=True)
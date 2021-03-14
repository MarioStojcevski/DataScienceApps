import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def count_function(seq):
	data = dict([
		('A', seq.count('A')),
		('T', seq.count('T')),
		('G', seq.count('G')),
		('C', seq.count('C')),
		])
	return data


st.write("""
# Mario's first streamlit app :)
""")

st.header('Enter the DNA sequence below')

sequence_input = "GAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence = st.text_area('Input', sequence_input, height=150)
lines = sequence.splitlines()
formatted = ''.join(lines)


st.write("""
***
""")

data = count_function(formatted)

st.subheader('DataFrame')
df = pd.DataFrame.from_dict(data, orient='index')
df = df.rename({0: '#'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index': 'Nucleotide'})
st.write(df)

st.subheader('Chart')
st.write(df.plot(kind='line', x='Nucleotide', y='#'))

# modules

import os
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt

# creating needed directories:

# histograms
if not os.path.exists('histograms'):
	os.makedirs('histograms')

def select_file():

	"""Read .csv or .xlsx file contained in the /input directory"""

	print('Please make sure your file is in the /input directory.')
	print('If you are just trying this package, try the TEST data.')
	
	# display available files
	files = dict(enumerate(os.listdir('input')))

	print('\nFiles available in /input:\n')
	for file in files:
		print(f'{file}: {files[file]}')

	# selection
	file_number = int(input("\nSelect a file by index (like 0): "))
	selected_file = files[file_number]
	path_to_file = f'input/{selected_file}'

	# loading file
	if selected_file[-4:] == '.csv':

		df = pd.read_csv(path_to_file)
		print('Great, file loaded.')

	elif selected_file [-5:] == '.xlsx':

		df = pd.read_excel(path_to_file)
		print('Great, file loaded.')

	else:

		print('Only .csv or .xlsx for now. Check your file.')
		return None

	# returning also the file name for later folder creation
	selected_file = selected_file[:-4]

	return df, selected_file

def analyze_file(df):

	"""Brings a summary for the file: number of rows/columns, which columns are available and your respective data types."""

	print('\nSUMMARY\n')
	print(f'Rows: {len(df)}')
	print(f'Columns: {len(df)}')
	print('-')
	print('Columns:')
	print('-')

	for c in df.columns:
		print(f'{df[c].name}: {df[c].dtype}')

def generate_histograms(df, selected_file):

	"""Generate histograms for all numeric columns. Histograms are available in /histograms directory, named by column name."""

	# creating directory for current file
	if not os.path.exists(f'histograms/{selected_file}'):
		os.makedirs(f'histograms/{selected_file}')

	for c in df.columns:
		if df[c].dtypes == 'float64' or 'int64':
			plt.hist(df[c], edgecolor = 'black')
			plt.title(c)
			plt.savefig(f'histograms/{selected_file}/{c}.png')
			plt.close()

df, selected_file = select_file()

if df is not None:
	analyze_file(df)
	generate_histograms(df, selected_file)
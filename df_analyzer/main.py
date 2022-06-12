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

def import_file():

	"""Read .csv or .xlsx file contained in the /input directory"""

	print('Please make sure your file is in the /input directory.')
	print('If you are just trying this package, try the TEST data.')
	name = input('Insert file name (TEST for test data): ')

	if name == 'TEST':
		name = 'input/heart_failure_clinical_records_dataset.csv'

	if name[-4:] == '.csv':

		df = pd.read_csv(name)
		print('Great, file loaded.')

	elif name [-5:] == '.xlsx':

		df = pd.read_excel(name)
		print('Great, file loaded.')

	else:

		print('Only .csv or .xlsx for now. Check your file.')
		return None

	return df

def analyze_file(df):

	"""Brings a summary for the file: number of rows/columns, which columns are available and your respective data types."""

	print(f'Rows: {len(df)}')
	print(f'Columns: {len(df)}')
	print('-')
	print('Columns:')
	print('-')

	for c in df.columns:
		print(f'{df[c].name}: {df[c].dtype}')

def generate_histograms(df):

	"""Generate histograms for all numeric columns. Histograms are available in /histograms directory, named by column name."""

	for c in df.columns:
		if df[c].dtypes == 'float64' or 'int64':
			plt.hist(df[c], edgecolor = 'black')
			plt.title(c)
			plt.savefig(f'histograms/{c}.png')
			plt.close()

df = import_file()
analyze_file(df)
generate_histograms(df)
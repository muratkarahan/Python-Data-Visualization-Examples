
import pandas as pd
import numpy as np
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go



def PlotCsvFile(CsvFile):
	# Import data from csv
	df = pd.read_csv(CsvFile)
	df.head()

	dataX=[]
	for col in df.columns:
		traceX = go.Scatter(x=df.index, y=df[col], mode='lines', name=col )
		dataX.append(traceX)	

	layout = go.Layout(title=str(CsvFile),plot_bgcolor='rgb(230, 230,230)')

	fig = go.Figure(dataX, layout=layout)

	plot(fig)


# Generic Imports
import glob

# Pandas and Numpy Imports
import numpy as np
import pandas as pd

# Plotly Imports
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

#python xlwings
import xlwings as xw



def PrintCsvFiles(CsvPath):
	print(glob.glob(CsvPath+"/*.csv"))


# CSV Files
def ConCatCsv(CsvPath):

	listCsv = []

	CsvPathFiles = glob.glob(CsvPath+"/*.csv")

	for fileCsv in CsvPathFiles:
		df=pd.read_csv(fileCsv,index_col=None,header=0)
		listCsv.append(df)
		print(df)

	frame = pd.concat(listCsv,axis=1)	
	frame.to_csv("merged.csv",sep=",")
	print(listCsv)
	return frame


def SaveCsv(CsvName,CsvArr,CsvHeader):
    np.savetxt(CsvName,CsvArr,delimiter=",",header=CsvHeader)


    
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



def PlotCsvWithSlider(CsvFile):
	# Import data from csv
	df = pd.read_csv(CsvFile)
	df.head()
	dataX=[]
	for col in df.columns:
		traceX = go.Scatter(x=df.index, y=df[col], mode='lines', name=col,fill="tonexty" )
		dataX.append(traceX)	
	
	layout = dict(
                title='Time series with range slider and selectors',
                xaxis=dict(
                    rangeslider=dict(
                        visible = True
                        ),
                    )
                )
	fig = dict(data=dataX, layout=layout)
	plot(fig)




def CsvFindLastCells():
    row_cell = xw.sheets[0].api.Cells.Find(What="*",
            After= xw.sheets[0].api.Cells(1, 1),
            LookAt=xw.constants.LookAt.xlPart,
            LookIn=xw.constants.FindLookIn.xlFormulas,
            SearchOrder=xw.constants.SearchOrder.xlByRows,
            SearchDirection=xw.constants.SearchDirection.xlPrevious,
            MatchCase=False)

    column_cell = xw.sheets[0].api.Cells.Find(What="*",
            After=xw.sheets[0].api.Cells(1, 1),
            LookAt=xw.constants.LookAt.xlPart,
            LookIn=xw.constants.FindLookIn.xlFormulas,
            SearchOrder=xw.constants.SearchOrder.xlByColumns,
            SearchDirection=xw.constants.SearchDirection.xlPrevious,
            MatchCase=False)

    print((row_cell.Row, column_cell.Column))

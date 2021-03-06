import plotly.express as px
import csv
import numpy as np

def Fif(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x='Coffee in ml',y='sleep in hours')
        fig.show()
def getDataSource(data_path):
    Coffee_in_ml=[]
    sleep_in_hours=[]
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv-file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row['Coffee in ml']))
            sleep_in_hours.append(float(row['sleep in hours']))

    return{'x':Coffee_in_ml,'y':sleep_in_hours}
def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks in percentage and Days present :-  \n--->",correlation[0,1])

def setup():
    data_path  = "./data/Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)
    plotFigure(data_path)

setup()

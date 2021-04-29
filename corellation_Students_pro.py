import csv
import plotly.express as px 
import numpy as np

def get_data_source(datapath):
    ice_cream_sales = []
    Temperature = []
    with open("Student Marks vs Days Present.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Marks In Percentage"]))
            Temperature.append(float(row["Days Present"]))

    return{"x":Temperature, "y":ice_cream_sales}

def find_correlation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation :- \n-->", correlation[0,1])

def setup():
    datapath = "Student Marks vs Days Present.csv"
    datasource = get_data_source(datapath)
    find_correlation(datasource)

setup()
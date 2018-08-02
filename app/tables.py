import pandas as pd
import os

my_path = os.path.abspath(os.path.dirname(__file__))

# make a function to take in the filename and make a url
def show_table(d=','):
    url = my_path + '/static/data/redsox_2018_hitting.txt'
    bos18 = pd.read_csv(url, sep=d)
# pandas has a funciton to return pandas dataframe as html
    return bos18.to_html()

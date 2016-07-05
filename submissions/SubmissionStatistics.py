import os
import pandas as pd
import csv
import glob
import io
import seaborn as sns
import matplotlib.pyplot as plot
import numpy as np
import json
from pandas.io.json import json_normalize

collectionpath="/home/shahbaz/commentstest"
filepath="/home/shahbaz/file1"
csvcollection="/home/shahbaz/SubmissionsCsv"

# Function to remove empty files in a directory
def remove_emptyfiles(collectionpath):
    for file in os.listdir(collectionpath):
        path = os.path.join(collectionpath, file)
        if os.path.isfile(path):
            if os.path.getsize(path) == 0:
                os.remove(path)

# Function to count the number of lines in a collection
def count_linesincollection(collectionpath):
    totalcount=0
    for file in os.listdir(collectionpath):
        path = os.path.join(collectionpath, file)
        if os.path.isfile(path):
            with open(path) as current_file:
                for i, l in enumerate(current_file):
                    pass
                #print(current_file.name, i+1)
                totalcount=totalcount+(i+1)
    return totalcount


# Function to count the number of lines in a file
def count_linesinfile(filepath):
    totalcount=0
    if os.path.isfile(filepath):
        with open(filepath) as current_line:
            for i,l in enumerate(current_line):
                pass
            #print(i+1)
        return i+1


# Function to read json files to pandas dataframes
def read_jsontodataframe(filepath):
    if os.path.isfile(filepath):
        with open(filepath,'rb') as file:
            data= file.readlines()
        data = map(lambda x: x.rstrip(), data)
    data_json_str= "["+','.join(data)+"]"

    dataframe = pd.read_json(data_json_str)
    return dataframe


def convertcollection_todataframe(collectionpath):
    for file in os.listdir(collectionpath):
        path = os.path.join(collectionpath, file)
        if os.path.isfile(path):
            with open(path) as current_file:
                dataframe= read_jsontodataframe(path)
                dataframe.to_csv('/home/shahbaz/SubmissionsCsv/'+file.capitalize()+'.csv', sep=',', encoding='utf-8')


def merge_csv(csvcollection):
    filewriter = csv.writer(open('/home/shahbaz/submission.csv',"wb"))
    file_counter = 0
    for input_file in glob.glob(os.path.join(csvcollection,"*.csv")):
        with open(input_file,'rU') as csv_file:
            filereader = csv.reader(csv_file)
            if file_counter < 1:
                for row in filereader:
                    filewriter.writerow(row)
            else:
                header = next(filereader, None)
                for row in filereader:
                    filewriter.writerow(row)
        file_counter += 1


def draw_hist():
    df=pd.read_csv('/home/shahbaz/submissiontest.csv', sep=',', header=None)
    df.drop(df.columns[0], axis=1, inplace=True)
    df1= df.ix[1:]
    print (df1.head(n=100))
    print (df1.loc[df1[5].idxmax()])
    #df1=df[['wordcount']]
    #hist= sns.distplot(df1, bins=(range(0, 1000, 25)), color='#d50000', kde=False)
    #hist.set_ylabel('Number of Submissions')
    #hist.set_xlabel('Length of Submissions')
    #plot.show()



def read_tojson(jsonfile):
    data=[]
    with io.open(jsonfile,'rU', encoding='utf-8') as current_file:
        for line in current_file:
            data.append(json.loads(line))
    return data

data= read_tojson('/home/shahbaz/test.jsonl')
print (data['comment'])






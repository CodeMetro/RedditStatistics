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


def draw_hist(df):
    df1=df['wordcount']
    hist= sns.distplot(df, bins=(range(0, 2000, 25)), color='#BF360C', kde=False)
    hist.set_ylabel('Number of Submissions')
    hist.set_xlabel('Length of Submissions')
    plot.show()






def json_todataframe(jsonfile):
    with io.open(jsonfile,'rU', encoding='utf-8') as current_file:
        for line in current_file:
            yield json.loads(line)
            #df=df.append(json.loads(line),ignore_index=True)
    #draw_hist(df)
            #data.append(json.loads(line))

frame=pd.DataFrame(json_todataframe('/home/bd-ss16-g2/submissions.jsonl'))
print(frame.head(n=10))



#print(count_linesinfile('/home/shahbaz/submissions.jsonl'))
#print(count_linesinfile('/home/shahbaz/workspace/JsontoCSV/submissionswordcount.csv'))
#print(count_linesinfile('/home/shahbaz/comments.jsonl'))
#print(count_linesinfile('/home/shahbaz/workspace/JsontoCSV/commentswordcount.csv'))


def dataframe_fromcsv(csvpath):
    df=pd.read_csv(csvpath,header=None)
    return df


#subcsv='/home/shahbaz/workspace/JsontoCSV/submissionswordcount.csv'
#commcsv='/home/shahbaz/workspace/JsontoCSV/commentswordcount.csv'

#frame=dataframe_fromcsv(subcsv)
#draw_hist(frame)

#df= pd.DataFrame(data)

#draw_hist(df)

#print ("Longest comment is ", df.loc[df['wordcount'].idxmax()])
#print ("Shortest comment is ", df.loc[df['wordcount'].idxmin()])










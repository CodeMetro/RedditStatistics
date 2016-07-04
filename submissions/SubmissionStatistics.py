import os
import pandas as pd

collectionpath="/home/shahbaz/submissions"
filepath="/home/shahbaz/file1"
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





#totalCount = count_linesincollection(collectionpath)
#print(totalCount)

dataframe = read_jsontodataframe(filepath)
print dataframe['comment'].iloc[0]


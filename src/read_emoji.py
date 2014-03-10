#!/usr/bin/python
# coding: UTF-8
 
# CSVファイルの読み込み
 
import csv
import json

filename = "EmojiSources.csv"
csvfile = open(filename)

output = []
for row in csv.reader(csvfile,delimiter=';'):
    if len(row) != 0:
        output.append(row[0])
        
print json.dumps(output) 
#print csvfile
# coding=utf8

'''
Created on May 01, 2022 08:40 PM
Last revised : May 01, 2022 11:28 PM

Author : Chao-Hsuan Ke

read CSV
ES insert

Reference
https://ithelp.ithome.com.tw/articles/10244571

'''

import csv
from elasticsearch import Elasticsearch

csvfile = 'aa.csv'
es = Elasticsearch(["http://127.0.0.1:9200"])

with open(csvfile, newline='') as f:
  # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(f)

  members = dict()
  id_index = 8
  for row in rows:
    members = {'name':str(row['name']), 'id':str(row['id']), 'extession':str(row['extension']), 'phone':str(row['phone'])}
    # print(members)
    #print(row['name'], row['id'], row['extension'], row['phone'])
    result = es.create(index='qmc_members', id=id_index, body=members)
    id_index+=1
    print(result)
# coding=utf8

'''
Created on May 01, 2022 08:40 PM
Last revised : May 01, 2022 11:28 PM

Author : Chao-Hsuan Ke

'''

import csv

csvfile = 'QM(TOC)_20211012_name_id.csv'  # file full-location

# include read head (first row)
# with open(csvfile, "r", encoding="utf-8") as f:
#     myCsv = csv.reader(f)
#     #headers = next(myCsv)
#     for row in myCsv:
#         print(row)
#
# # no head (no (first row))
# with open(csvfile, "r", encoding="utf-8") as f:
#     myCsv = csv.reader(f)
#     for row in myCsv:
#         print(row)

with open(csvfile, newline='') as f:
  # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
  rows = csv.DictReader(f)
  # 以迴圈輸出指定欄位
  for row in rows:
    print(row['name'], row['id'], row['extension'], row['phone'])
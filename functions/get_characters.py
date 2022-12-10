import pandas as pd

'''
Created on May 01, 2022 08:40 PM
Last revised : May 01, 2022 11:28 PM

Author : Chao-Hsuan Ke

read CSV
ES insert

Reference
https://ithelp.ithome.com.tw/articles/10244571

'''

sheet_name = '匯出工作表'
df = pd.read_excel("../source/name.xlsx", sheet_name=sheet_name)
#print(df)

#print(df['NAME'].tolist())
#print(df['NAME'])

allName = ''

for i in range(len(df['NAME'])):
    allName += df['NAME'][i]
    #print(df['NAME'][i])

#print(len(allName))

result = "".join(dict.fromkeys(allName))
print(len(result))

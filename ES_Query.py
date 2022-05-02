
'''
version: May 02 2022, 08:40 PM
Last revision: May 02 2022, 10:37 PM

Author : Chao-Hsuan Ke
'''

'''
Reference
https://iter01.com/583334.html
'''

from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search

es = Elasticsearch(["http://127.0.0.1:9200"])
index_name = 'qmc_members'

class ESQuery():

    # def __init__(self):
    #     self.description = ""
    #     self.claim = list()


    def get_nameList(self, namelist):
        #print(namelist)
        for name in namelist:
            s = Search(using=es, index=index_name).filter("match_phrase", name=name)    # 非常精準
            #s = Search(using=es, index=index_name).filter("match", name=name)
            response = s.execute()
            if len(response) > 0:
                for responseWord in response:
                    print(responseWord.name)
            # if len(response) == 0:
            #     print('單位無此人')
            #     break
            # else :
            #     print(response[0].name, response[0].id, response[0].phone)
            #     break


    def main_processing(self, namelist):
        query.get_nameList(namelist)


query = ESQuery()
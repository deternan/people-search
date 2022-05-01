# coding=utf8

'''
Created on April 04, 2022    11:32 PM
Last revised : May 01, 2022 11:05 AM

Author : Chao-Hsuan Ko


Reference
https://blog.csdn.net/ltochange/article/details/122811731
https://github.com/mozillazg/python-pinyin#id3
https://pypi.org/project/pycorrector/
https://www.jb51.net/article/216777.htm
https://github.com/kjanjua26/Pyphones

Data
https://data.gov.tw/dataset/5961

'''

from pypinyin import pinyin, lazy_pinyin, Style
#import os
#import pickle


def get_all_char_pinyin():
    path = "all_chars.txt"
    pinyin_dict = {}
    with open(path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            ch = line.strip()
            ch_pinyin = pinyin(ch, style=Style.TONE3, heteronym=False)
            # heteronym 是否启用多音字模式
            for p_li in ch_pinyin:
                for p in p_li:
                    if p not in pinyin_dict:
                        pinyin_dict[p] = [ch]
                    else:
                        pinyin_dict[p].append(ch)
    return pinyin_dict


if __name__ == '__main__':
    pinyin_dict = get_all_char_pinyin()
    # 列出全部字元 (all_chars.txt)
    #print(pinyin_dict.keys())   # 注音
    print(pinyin_dict.items())  # 注音+中文字
    #print(pinyin_dict.values()) # 中文字

    similarity_dict = {}
    similarityText_list = []

    inputStr = '廖健宏'
    #print(len(blank))
    #print(list(blank))
    for word in list(inputStr):
        # 獲取同音漢字
        ch_pinyin = pinyin(word, style=Style.TONE3, heteronym=False)    # 注音
        #print(ch_pinyin)
        #print(ch_pinyin[0], ch_pinyin[1])
        res = []

        #判斷是否有同音字在列表中
        ch_pinyin_all = ch_pinyin[0].pop()
        if ch_pinyin_all in pinyin_dict:
            similarityText_list = pinyin_dict.get(ch_pinyin_all)
            print(word, ch_pinyin_all, pinyin_dict.get(ch_pinyin_all))
            for p_li in ch_pinyin:
                for p in p_li:
                    if word in pinyin_dict[p]:
                        # if match_char in pinyin_dict[p]:
                        # pinyin_dict[p].remove(match_char)
                        pinyin_dict[p].remove(word)
                    # else:
                    #     #print('此字尚未收錄')
                    res.extend(pinyin_dict[p])
                #print(res)
        else:
            #print('no')
            print(word, '此字尚未收錄')









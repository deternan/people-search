# coding=utf8

'''
Created on April 04, 2022    11:32 PM
Last revised : May 01, 2022 08:45 PM

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

from pypinyin import pinyin, Style
from itertools import product


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
    #print(pinyin_dict.items())  # 注音+中文字
    #print(pinyin_dict.values()) # 中文字

    similarityText_Dict = dict()

    inputStr = '廖健宏'

    collect_check = True
    for word in list(inputStr):
        # 獲取同音漢字
        ch_pinyin = pinyin(word, style=Style.TONE3, heteronym=False)    # 注音

        #判斷是否有同音字在列表中
        ch_pinyin_all = ch_pinyin[0].pop()
        if ch_pinyin_all in pinyin_dict:
            similarityText_list = pinyin_dict.get(ch_pinyin_all)
            print(word, ch_pinyin_all, pinyin_dict.get(ch_pinyin_all))
            # 將同音字存入 dic 中
            similarityText_Dict[word] = pinyin_dict.get(ch_pinyin_all)
            similarityText_Dict.update(similarityText_Dict)
        else:
            print(word, '此字尚未收錄')
            collect_check = False

    if collect_check==False:
        print('此姓名不包含於員工紀錄中')
    else:
        print('此姓名有包含於員工紀錄中')
        # 計算姓名中的各個組合
        #print(similarityText_Dict)

        index = 0
        all_list = []
        for pinyinword in similarityText_Dict:
            words_list = []
            for pinyinword2 in similarityText_Dict.get(pinyinword):
                words_list.append(pinyinword2)
            all_list.append(words_list)
        #print(all_list)

        first_wordlist = ''
        second_wordlist = ''
        third_wordlist = ''
        four_wordlist = ''
        output_list = []

        # Last Name (姓)
        for character in all_list[0]:
            first_wordlist += character

        if len(all_list) == 2:
            for character in all_list[1]:
                second_wordlist += character
                output_list = list(product(first_wordlist, second_wordlist))
            print(output_list)
        elif len(all_list) == 3:
            for character in all_list[1]:
                second_wordlist += character
            for character in all_list[2]:
                third_wordlist += character
                output_list = list(product(first_wordlist, second_wordlist, third_wordlist))
            print(output_list)
        elif len(all_list) == 4:
            for character in all_list[1]:
                second_wordlist += character
            for character in all_list[2]:
                third_wordlist += character
            for character in all_list[3]:
                four_wordlist += character
                output_list = list(product(first_wordlist, second_wordlist, third_wordlist, four_wordlist))
            print(output_list)


        # Display
        display_str = ''
        for nameCandidate in output_list:
            display_str = ''
            for name in nameCandidate:
                display_str += name
            print(display_str)







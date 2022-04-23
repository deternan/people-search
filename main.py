# coding=utf8

'''
Created on April 04, 2022    11:32 PM
Last revised : April 23, 2022 04:07 PM
author: Chao-Hsuan Ke
'''

from pypinyin import pinyin, lazy_pinyin, Style
import os
import pickle


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
    print(pinyin_dict.keys())

    similarity_dict = {}
    match_char = "民"

    blank = '台灣'
    #print(len(blank))
    #print(list(blank))
    for word in list(blank):
        #print(word)
        # 獲取同音漢字
        #ch_pinyin = pinyin(match_char, style=Style.TONE3, heteronym=False)
        ch_pinyin = pinyin(word, style=Style.TONE3, heteronym=False)
        print(ch_pinyin[0])
        res = []

        #判斷是否有同音字在列表中
        if ch_pinyin[0].pop() in pinyin_dict:
            print('yes')
        else:
            print('no')

        for p_li in ch_pinyin:
            for p in p_li:
                #print(p)
                if word in pinyin_dict[p]:
                #if match_char in pinyin_dict[p]:
                    #pinyin_dict[p].remove(match_char)
                    pinyin_dict[p].remove(word)
                else:
                    print('此字尚未收錄')
                res.extend(pinyin_dict[p])
        print(res)







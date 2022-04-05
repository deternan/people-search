'''
version: April 05, 2022 09:00 PM
Last revision: April 05, 2022 09:30 PM

Author : Chao-Hsuan Ko

'''

'''
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
    #print(pinyin_dict)
    # 获取同音汉字
    similarity_dict = {}
    match_char = "民"
    ch_pinyin = pinyin(match_char, style=Style.TONE3, heteronym=False)
    res = []
    for p_li in ch_pinyin:
        for p in p_li:
            print(p)
            if match_char in pinyin_dict[p]:
                pinyin_dict[p].remove(match_char)
            res.extend(pinyin_dict[p])
    print(res)




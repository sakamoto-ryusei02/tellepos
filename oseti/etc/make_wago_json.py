# -*- coding: utf-8 -*-
import json

PATH = 'C:\\Users\\jieti\\Desktop\\TestProject\\Python\\oseti\\oseti\\dic\\wago.121808.pn'
with open(PATH,encoding="utf-8") as fd:
    wago_dict = {}
    for line in fd:
        try:
            polarity, word = line.rstrip().split('\t')
            word = word.replace(' だ', '').replace(' と', '').replace(' の', '').replace(' です', '')
            word = word.replace(' ある', '')
        except:
            continue
        wago_dict[word] = polarity
json.dump(wago_dict, open('pn_wago.json', 'w'))

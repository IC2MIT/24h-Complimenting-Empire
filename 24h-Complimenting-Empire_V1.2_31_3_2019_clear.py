# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#author: xxf

import codecs
import random
import re

#Compliment_list =  ['您目光深邃，一看您就是一位有思想的人',
#                    '从您的言谈中可以看出，我今天遇到的是很有修养的人。',
#                    '别开玩笑了，看您的容貌，肯定不到二十岁。',
#                    '这么魁梧的身材，潇洒的外表，不是大老板才怪了呢！',
#                    '您一看就是大富大贵的人!',
#                    '我真佩服您的头脑，多少别人办不成的事，您一到便迎刃而解。',
#                    '您的语调独特，言谈话语中充满了感染力。',
#                    '听君一席话，胜读十年书，今天与您交谈，我受益匪浅。',
#                    '您一看就是大富大贵的人',
#                    '您真幽默，话从您口中说出来就是不一样。',
#                    '这么魁梧的身材，潇洒的外表，不是大老板才怪了呢！']
#print(random.choice(Compliment_list))

filename = 'complimentlist_31_03_2019.txt'
f = codecs.open(filename, mode='r+', encoding='utf-8')
print(random.choice(f.readlines()))

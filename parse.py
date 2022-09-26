import csv
import os
import stat
import string

path_server = os.path.join("/mnt/data2/asr-datasets/RuDevices/RuDevices/", "First_Dataset/")
path = os.path.join("/Users/ruslanzalikov/РаботаЛаниус/", "First_Dataset/")

os.system(f"touch {path}ruszal_train.tsv")   #создаю tsv пустую
os.system(f"touch {path}ruszal_train.wrd")   #wrd
os.system(f"touch {path}ruszal_train.ltr")   #ltr

txt_line = []
with open(f"{path}transcript.txt") as txt:
    line = ""
    for index, value in enumerate(txt.read()):                                                  #Парсинг построчный
        if value == "\n":
            txt_line.append(line)
            line = ""
            continue
        line += value


txt_line = list(map(lambda x: x.split("|"), txt_line))

with open(f'{path}ruszal_train.tsv', 'w') as tsvfile:
    # print("/mnt/data2/asr-datasets/RuDevices/RuDevices", " ", file=tsvfile)
    print(" ", " ", file=tsvfile)
    for index, value in enumerate(txt_line):
        stat = os.stat(os.path.join(f"{path}", f"{value[0]}"))       #tsv
        print(value[0], stat.st_size, file=tsvfile)

with open(f'{path}ruszal_train.wrd', 'w') as wrdfile:            #wrd
    for index, value in enumerate(txt_line):
        value[1] = value[1].translate(str.maketrans('', '', string.punctuation))
        value[1] = value[1].replace("—", "")
        print(value[1], file=wrdfile)

with open(f'{path}ruszal_train.ltr', 'w') as ltrfile:            #ltr
    for index, value in enumerate(txt_line):
        value[1] = value[1].translate(str.maketrans('', '', string.punctuation))
        value[1] = value[1].replace(" ", "|")
        value[1] = value[1].replace("", " ")
        value[1] = value[1].replace("—", "")
        print(value[1], file=ltrfile)




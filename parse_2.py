import csv
import os
import stat
import string

path = os.path.join("/mnt/data2/asr-datasets/RuDevices/RuDevices/", "Second_Dataset/")
path_mac = os.path.join("/Users/ruslanzalikov/РаботаЛаниус/", "Second_Dataset/")

os.system(f"touch {path}ruszal_train.tsv")   #создаю tsv пустую
os.system(f"touch {path}ruszal_train.wrd")   #wrd
os.system(f"touch {path}ruszal_train.ltr")   #ltr

with open(f"{path}audio_dataset/df.csv") as txt:
    file_reader = csv.reader(txt, delimiter=",")
    txt_line = []
    for row in file_reader:
        txt_line.append([row[7], row[0]])
    txt_line.pop(0)

with open(f'{path}ruszal_train.tsv', 'w') as tsvfile:
    # print("/mnt/data2/asr-datasets/RuDevices/RuDevices", " ", file=tsvfile)
    print(" ", " ", file=tsvfile)
    for index, value in enumerate(txt_line):
        stat = os.stat(os.path.join(f"{path}", "audio_dataset", f"{value[0]}"))       #tsv
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

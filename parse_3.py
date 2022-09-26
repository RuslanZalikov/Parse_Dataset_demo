import csv
import os
import stat
import string

path = os.path.join("/mnt/medraid/asr-datasets/", "Third_Dataset/")
path_mac = os.path.join("/Users/ruslanzalikov/РаботаЛаниус/", "Third_Dataset/")

os.system(f"touch {path}ruszal_train.tsv")   #создаю tsv пустую
os.system(f"touch {path}ruszal_train.wrd")   #wrd
os.system(f"touch {path}ruszal_train.ltr")

txt_line = []

for common in os.listdir(path=f"{path}/data"):
    if "." != common[0]:
        for file in os.listdir(path=f"{path}/data/{common}/ru"):
            if "." != file[0] and ".tsv" in file:
                with open(f"{path}/data/{common}/ru/{file}") as txt:
                    file_reader = csv.reader(txt, delimiter="\t")
                    for row in file_reader:
                        if row[1] != "path":
                            txt_line.append([f"data/{common}/ru/clips/{row[1]}", row[2]])

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

print("MTUCI")

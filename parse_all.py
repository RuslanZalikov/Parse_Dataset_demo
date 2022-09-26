import csv
import os
import stat
import string

path_server = os.path.join("/mnt/medraid/asr-datasets/")
path = os.path.join("/Users/ruslanzalikov/РаботаЛаниус/")

os.system(f"touch {path}ruszal_train.tsv")   #создаю tsv пустую
os.system(f"touch {path}ruszal_train.wrd")   #wrd
os.system(f"touch {path}ruszal_train.ltr")

txt_line = []
txt_line_wrd = []

for common in os.listdir(path=path):
    if "Dataset" in common and "." not in common: ###############
        for file in os.listdir(path=f"{path}{common}"):
            if ".tsv" in file:
                with open(f"{path}{common}/{file}", encoding="ISO-8859-1") as txt:
                    file_reader = csv.reader(txt, delimiter="\t")
                    for row in file_reader:
                        row = list(map(lambda x: x.split(" "), row))
                        if len(row[0]) == 2:
                            print(row)
                            txt_line.append([row[0][0], row[0][1]])
            if ".wrd" in file:
                with open(f"{path}{common}/{file}", encoding="ISO-8859-1") as txt_wrd:
                    line = ""
                    for index, value in enumerate(txt_wrd.read()):
                        if value == "\n":
                            txt_line_wrd.append(line)
                            line = ""
                            continue
                        line += value

with open(f'{path}ruszal_train.tsv', 'w', encoding="ISO-8859-1") as tsvfile:
    print(" ", " ", file=tsvfile)                               #tsv
    for index, value in enumerate(txt_line):
        print(value[0], value[1], file=tsvfile)
    print(len(txt_line))



with open(f'{path}ruszal_train.wrd', 'w', encoding="ISO-8859-1") as wrdfile:            #wrd
    for index, value in enumerate(txt_line_wrd):
        print(value, file=wrdfile)
    print(len(txt_line_wrd))

with open(f'{path}ruszal_train.ltr', 'w', encoding="ISO-8859-1") as ltrfile:            #ltr
    for index, value in enumerate(txt_line_wrd):
        value = value.replace(" ", "|")
        print(value, file=ltrfile)
# -*-coding:utf-8-*-

from os import listdir
from os.path import isfile, join
import xlrd
import pickle

mypath = './doc'
all_f = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(all_f)
infoLst = []

def oneXL(path):
    workbook = xlrd.open_workbook(path, formatting_info=True)
    sub_sheets = workbook.sheet_names()
    for val in sub_sheets:
        dic = {}
        dic['xl'] = path
        dic['sheet'] = val
        sheet = workbook.sheet_by_name(val)
        lst = sheet.merged_cells
        for tup in lst:
            # print(tup, tup[0], tup[2])
            if tup[2] == 0 and type(sheet.cell_value(tup[0], tup[2])) == float:
                dic[int(sheet.cell_value(tup[0], tup[2]))] = sheet.cell_value(tup[0], tup[2]+2)
        infoLst.append(dic)

if len(all_f) != 0:
    for f in all_f:
        docpath = '{}/{}'.format(mypath, f)
        oneXL(docpath)

with open(r'info.pkl', 'wb') as pf:
    pickle.dump(infoLst, pf)

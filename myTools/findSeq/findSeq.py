# -*-coding:utf-8-*-

from os import listdir
from os.path import isfile, join
import xlrd

mypath = './doc'
all_f = [f for f in listdir(mypath) if isfile(join(mypath, f))]
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

def search(v):
    for d in infoLst:
        for val in d:
            if v in d[val]:
                print('******************************************************')
                print('表格文件: {}'.format(d['xl']))
                print('子表名称: {}'.format(d['sheet']))
                print('所查姓名: {}'.format(d[val]))
                print('所查序号: {}'.format(val))
                print('******************************************************')
                return
    print('###################################')
    print(' 不存在所查姓名。')
    print('###################################')

# oneXL('{}/{}'.format(mypath, all_f[0]))

if len(all_f) != 0:
    for f in all_f:
        docpath = '{}/{}'.format(mypath, f)
        oneXL(docpath)

while True:
    name = input('输入查询名字： ')
    search(name)

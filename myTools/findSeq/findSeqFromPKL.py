# -*-coding:utf-8-*-
import pickle

with open(r'info.pkl', 'rb') as pf:
    infoLst = pickle.load(pf)

def search(v):
    exist = False
    for d in infoLst:
        for val in d:
            if v in d[val]:
                print('******************************************************')
                print('表格文件 Excel:     {}'.format(d['xl']))
                print('子表名称 Sheet:    {}'.format(d['sheet']))
                print('所查姓名 Name:    {}'.format(d[val]))
                print('所查序号 Number: {}'.format(val))
                print('******************************************************')
                exist = True
    if exist == False:
        print('###################################')
        print(' 不存在所查姓名。Don\'t exist.')
        print('###################################')

while True:
    name = input('输入查询名字 Please input name: ')
    search(name)

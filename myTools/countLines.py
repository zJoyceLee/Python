import sys
import os


def counter(path):
    if  os.stat(path).st_size == 0:
        return 0
    with open(path, 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def traverseF(path):
    pathLst = []
    for dirName, subdirList, fileList in os.walk(path):
        for fname in fileList:
            f = '{0}/{1}'.format(dirName, fname)
            filterF(f) and pathLst.append(f)
    return pathLst

def filterF(f):
    f_lst = ['.htm', '.html', '.css', '.js', '.php']
    extension = f[f.rfind('.'):]
    if extension in f_lst:
        return True
    return False

def main(root):
    paths = traverseF(root)
    countLine = 0
    for path in paths:
        countLine += counter(path)
    print(countLine)

if __name__ == '__main__':
    try:
        rootPath = sys.argv[1]
        main(rootPath)
    except:
        print('USAGE: python countLines rootPath')
        exit()

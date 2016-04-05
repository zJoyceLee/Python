import os

def readFile(path):
    all_the_text = '\n\n#' + path+'\n'
    with open(path) as file_obj:
        all_the_text += file_obj.read()
        # print(all_the_text)
    return all_the_text

if __name__=='__main__':
    try:
        text = ''

        nameLst= []
        folderLst = os.listdir('./NumericalCalculation')
        for _ in folderLst:
            if _[0] != 'C':
                folderLst.remove(_)
        folderLst.sort()
        print(folderLst)

        fileLst = []
        for _ in folderLst:
            path = './NumericalCalculation/' + _
            print(path)
            fileLst = os.listdir(path)
            fileLst.sort()
            print(fileLst)

            for ss in fileLst:
                filePath =  path + '/' + ss
                print(filePath)
                text += readFile(filePath)

        f = open('/media/joyce/DC30008D300070B6/homework.txt', 'r+')
        f.write(text)
        f.close()

    except (TypeError, NameError) as e:
        print(e)

    finally:
        f.close()

import MySQLdb

db = MySQLdb.connect('localhost', 'root', '1', 'Words')
cursor = db.cursor()

ss = 'SELECT * FROM Word_lenDESC;'
cursor.execute(ss)
results = cursor.fetchall()


def isInDict(word):
    ss = "SELECT * FROM Word_lenDESC WHERE word = '{0}';".format(word)
    cursor.execute(ss)
    result = cursor.fetchall()
    if result is ():
        return False
    else:
        return True


def isTarget(word):
    print(word)
    wordLst = [word[:_]+word[_+1:] for _ in range(len(word)) if isInDict(word[:_]+word[_+1:])]

    if wordLst == [] and len(word) == 1:
        return True
    else:
        for myWord in wordLst:
            return isTarget(myWord)

lst = []
# ss = 'INSERT INTO Target(word, len) VALUES '
for word in results:
    myWord = word[0]
    # print(myWord)
    if isTarget(myWord):
        lst.append(myWord)
        # sql = ss+"('{0}', {1});".format(myWord, len(myWord))
        # cursor.execute(sql)
# db.commit()

print(lst)

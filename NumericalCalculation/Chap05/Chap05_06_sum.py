def mySum(lst):
    ret = 0
    for i in lst:
        if type(i) == type(1) or type(i) == type(1.1):
            ret += i
    return ret

if __name__ == '__main__':
    try:
        print(mySum([1, 2, 3, 4, 5]))
        print(mySum([0.1, 2.2]))
    except e:
        print(e)

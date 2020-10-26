#/usr/bin/python

acoollist = [30,60,30,40]
"""
if 20 in acoollist :
    print(acoollist.count(30))
else:
    acoollist.insert(2,50)
    print(acoollist)
"""
if 30 in acoollist:
    acoollist.append(10)
    acoollist.insert(5,'Manohar')
    print("list result:",acoollist)
else:
    print("no not exist")








a = input("enter a string")

list=a.split()


if (len(list)==1):
    dict={}

    temp_str=", ".join(list)

    for i in temp_str :
        count=temp_str.count(i)
        dict.update({i:count})
    print(dict)

else:
    (len(list)!=1)
    dict={}

    for i in list:
        count=list.count(i)
        dict.update({i:count})
    print(dict)    




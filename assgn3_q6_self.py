n = int(input("enter a number"))
dict={}
for i in range(1,n):
    Y = input("enter students name")
    N = input("enter SID")
    my_dict = {Y:N}
    dict.update(my_dict)

print(dict)   

# sorting dict by keys
# my_keys = list(dict.keys())

# my_keys.sort()

# dict1 = {i:dict[i] for i in my_keys}

# print(dict1)

#sorting dict by SID

# my_values = list(dict.values())

# my_values.sort()

# dict2 = {dict[i]:i for i in my_values}

# print(dict2)


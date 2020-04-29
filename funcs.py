def get_name(name1,name2):
    fi=name1[0:1]
    la=name2[0:1]
    return fi,la
first=input('enter first name\n')
last=input('enter last name\n')
re=get_name(first,last)
print(re)
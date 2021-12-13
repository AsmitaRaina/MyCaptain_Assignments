
d={}
d1={}
def most_frequent(string):
    for i in string:
        c=1
        if (i not in d):
            d[i]=c
        else:
            d[i]=d[i]+1
    key=list(d.keys())
    val=sorted(list(d.values()), reverse=True)
    for j in val:
        d1[key[val.index(j)]]=j
    print(d1)
    
string=input("Enter word")
most_frequent(string)

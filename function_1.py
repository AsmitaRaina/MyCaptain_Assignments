d={}
def most_frequent(string):
    for i in string:
        c=1
        if (i not in d):
            d[i]=c
        else:
            d[i]=d[i]+1
    print(d)
   
string=input("Enter word")
most_frequent(string)

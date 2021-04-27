f=input('enter the file name')
try:
    fh=open(f)
except:
    print('file cannot be opened')
    exit()
d=dict()
for line in fh:
    a=line.strip().rstrip()
    words=a.split()
    for word in words:
        if word not in d:
            d[word]=1
        else:
            d[word]+=1
print(d)
f1=open('coun.txt','w')
f1.write("d")
f2=open('Polish_20201130_010009334.jpg','rb')









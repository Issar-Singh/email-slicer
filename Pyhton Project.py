a=int(input('No. of Emails: '))
n=[]
d=[]
for i in range(a):
    l=input('Email: ').split('@')
    for j in range(len(l)):
        if j%2==0:
            n.append(l[j])
        else:
            d.append(l[j])
for k in range(len(n)):
    print('username:',n[k],'and domain:',d[k].upper())

    
    
    
    

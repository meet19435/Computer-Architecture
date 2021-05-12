def XOR(a,b):
    if(a=="1" and b=="0"):
        return "1"
    elif(a=="0" and b=="0"):
        return "0"
    elif(a=="0" and b=="1"):
        return "1"
    elif(a=="1" and b=="1"):
        return "0"
    elif(a==""):
        return str(b)
def AND(a,b):
    if(a=="0" or b=="0"):
        return "0"
    else:
        return "1"
def OR(a,b):
    if(a=="1" or b=="1"):
        return "1"
    else:
        return "0"
def sumbin(s1,s2):
    carry="0";
    finalres=""
    s1rev=s1[::-1]
    s2rev=s2[::-1]
    finalresrev=""

    for i in range(len(s1)):
        a=s1rev[i]
        b=s2rev[i]
        c=XOR(a,b)
        d=XOR(carry,c)
        finalresrev=finalresrev+d
        e=AND(a,b)
        f=AND(carry,b)
        g=AND(carry,a)
        z=OR(e,f)
        carry=OR(z,g)

    finalres=finalresrev[::-1]
    return finalres
def bincon(s,n):
    if(s[0]=="-"):
        return s[3:].zfill(n)
    else:
        return s[2:].zfill(n)
def com(s):
    n=len(s)
    a="1".zfill(n)
    q=""
    for x in range(n):
        if(s[x]=="1"):
            q=q+"0"
        else:
            q=q+"1"
    w=sumbin(q,a)
    return w
n1=int(input())
n2=int(input())
n3=bin(n1)
n4=bin(n2)
n5=len(n3)-1
n6=len(n4)-1
multiplicand=""
multipilcand1=""
multiplier=""
a="0"
q0="0"
n=0
if(n1>=0 and n2>=0):
    if(n5>=n6):
        x=bincon(n3,n5)
        y=bincon(n4,n5)
        a=bincon(a,n5)
        n=n5
    else:
        x=bincon(n3,n6)
        y=bincon(n4,n6)
        a=bincon(a,n6)
        n=n6
elif(n1<0 and n2>=0):
    if(n5>n6):
        x=bincon(n3,n5)
        y=bincon(n4,n5)
        a=bincon(a,n5)
        n=n5
    elif(n6>n5):
        x=bincon(n3,n6)
        y=bincon(n4,n6)
        a=bincon(a,n6)
        n=n6
    else:
        x=bincon(n3,n5+1)
        y=bincon(n4,n5+1)
        a=bincon(a,n5+1)
        n=n6+1
elif(n1>=0 and n2<0):
    if(n5>n6):
        x=bincon(n3,n5)
        y=bincon(n4,n5)
        a=bincon(a,n5)
        n=n5
    elif(n6>n5):
        x=bincon(n3,n6)
        y=bincon(n4,n6)
        a=bincon(a,n6)
        n=n6
    else:
        x=bincon(n3,n6+1)
        y=bincon(n4,n6+1)
        a=bincon(a,n6+1)
        n=n6+1
else:
    if(n5>n6):
        x=bincon(n3,n5)
        y=bincon(n4,n5)
        a=bincon(a,n5)
        n=n5
    elif(n6>n5):
        x=bincon(n3,n6)
        y=bincon(n4,n6)
        a=bincon(a,n6)
        n=n6
    else:
        x=bincon(n3,n5+1)
        y=bincon(n4,n5+1)
        a=bincon(a,n6+1)
        n=n6+1
if(n1<0):
    multiplicand=com(x)
    multiplicand1=x
else:
    multiplicand=x
    multiplicand1=com(x)
if(n2<0):
    multiplier=com(y)
else:
    multiplier=y
##print("n    a   q   q0     steps")
temp=str(n)+" "+a+" "+multiplier+" "+q0+" Initial"
print(temp)
while(n>0):
    if((multiplier[-1]=="1" and q0=="1") or (multiplier[-1]=="0" and q0=="0")):
        q0=multiplier[-1]
        multiplier=a[-1]+multiplier[0:len(multiplier)-1]
        if(a[0]=="1"):
            a="1"+a[0:len(a)-1]
        else:
            a="0"+a[0:len(a)-1]
        n=n-1
        print(str(n)+" "+a+" "+multiplier+" "+q0+" RightShift")
    elif(multiplier[-1]=="1" and q0=="0"):
        a=sumbin(a,multiplicand1)
        print(str(n)+" "+a+" "+multiplier+" "+q0+" A=A-M")
        q0=multiplier[-1]
        multiplier=a[-1]+multiplier[0:len(multiplier)-1]
        if(a[0]=="1"):
            a="1"+a[0:len(a)-1]
        else:
            a="0"+a[0:len(a)-1]
        n=n-1
        print(str(n)+" "+a+" "+multiplier+" "+q0+" RightShift")
    else:
        a=sumbin(a,multiplicand)
        print(str(n)+" "+a+" "+multiplier+" "+q0+" A=A+M")
        q0=multiplier[-1]
        multiplier=a[-1]+multiplier[0:len(multiplier)-1]
        if(a[0]=="1"):
            a="1"+a[0:len(a)-1]
        else:
            a="0"+a[0:len(a)-1]
        n=n-1
        print(str(n)+" "+a+" "+multiplier+" "+q0+" RightShift")
final=a+multiplier
print("Binary Output = "+final)
sum=0
if(final[0]=="1"):
    z=com(final)
    revz=z[::-1]
    for x in range(len(revz)):
        if(revz[x]=="1"):
            sum=sum+pow(2,x)
        else:
            sum=sum
    print("Decimal Output = - "+str(sum))       
else:
    z=final
    revz=z[::-1]
    for x in range(len(revz)):
        if(revz[x]=="1"):
            sum=sum+pow(2,x)
        else:
            sum=sum
    print("Decimal Output = "+str(sum))

    


        





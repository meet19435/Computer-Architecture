##Assumption that the assembly code is given in acuumulator architecture
l_c=0
count=0
opcode_1={"ADD":"0011","CLA":"0000","LAC":"0001","SAC":"0010","SUB":"0100","BRZ":"0101","BRN":"0110","BRP":"0111","INP":"1000","DSP":"1001","MUL":"1010","DIV":"1011","STP":"1100"}
symbol=[]
operands=[]
flabel1=[]
foperands1=[]
file1=input()
f1=open(file1,"r")
label=[]
more_input=True
looptemp=[]
opl=["CLA","LAC","SAC","ADD","SUB","BRZ","BRN","BRP","INP","DSP","MUL", "DIV","STP"]
opl1=["CLA","STP"]
opl2=["SAC","LAC","ADD","SUB","BRZ","BRN","BRP","INP","DSP","MUL","DIV"]
def type1(s):
    l=s.split(" ")
    if(len(l)==1):
        return 1
    elif(len(l)==2):
        return 2
    elif(len(l)==3):
        return 3
def stpval():
    f2=open(file1,"r")
    z=""
    count=-1
    while(z!="STP"):
        z=f2.readline()
        z=z.strip()
        count=count+1
    return count
def findvar(s):
    f3=open(file1,"r")
    f4=open(file1,"r")
    z=f3.read()
    a=z.find("STP")
    y=z.find(s,a)
    if(y==-1):
        return -1
    else:
        q=0
        e=""
        l=[" "]
        while(l[0]!=s):
            r=f4.readline()
            l=r.split(" ")
            q=q+1
        return [l[0],bin(int(l[1])),q-1]
def valop(s):
    l=s.split(" ")
    a=type1(s)
    if(a==1):
        if(l[0] in opl):
            return 1
        else:
            return -1
    elif(a==2):
        if(l[0][-1]==":"):
            if(l[1] in opl):
                return 1
            else:
                return -1
        else:        
            if(l[0] in opl ):
                return 1
            else:
                return -1
    elif(a==3):
        if(l[1] in opl):
            return 1
        else:
            return -1
def exvar(s):
    l1=s.split(" ")
    y=type1(s)
    if(y==1):
        if(l1[0] in opl2):
            return -1
        else:
            return 1
    elif(y==2):
        if(l1[1] in opl2 or l1[0] in opl1):
            return -1
        else:
            return 1
    elif(y==3):
        if(l1[0] in opl1):
            return -1
        elif(l1[1] in opl1):
            return -1;
        elif(l1[0] in opl2):
            return -1
        else:
            return 1

def binf(s):
    if(len(s)==3):
        return "0000000"+s[2:]
    if(len(s)==4):
        return "000000"+s[2:]
    if(len(s)==5):
        return "00000"+s[2:]
    if(len(s)==6):
        return "0000"+s[2:]
    if(len(s)==7):
        return "000"+s[2:]
    if(len(s)==8):
        return "00"+s[2:]
    if(len(s)==9):
        return "0"+s[2:]
    if(len(s)==10):
        return ""+s[2:]
def binn(s):
    if(s[0]=="-"):
        if(len(s)==4):
            return "-0000000"+s[3:]
        elif(len(s)==5):
            return "-000000"+s[3:]
        elif(len(s)==6):
            return "-00000"+s[3:]
        elif(len(s)==7):
            return "-0000"+s[3:]
        elif(len(s)==8):
            return "-000"+s[3:]
        elif(len(s)==9):
            return "-00"+s[3:]
        elif(len(s)==10):
            return "-0"+s[3:]
        elif(len(s)==11):
            return "-"+s[3:]

def listloop():
    f6=open(file1,"r")
    t=0
    y=""
    while(y!="STP"):
        y=f6.readline()
        y=y.strip()
        z=type1(y)
        l=y.split(" ")
        if(z==2):
            if(l[0][-1]==":"):
                looptemp.append(l[0][0:len(l[0])-1])
        elif(z==3):
            looptemp.append(l[0][0:len(l[0])-1])
        t=t+1
f10=open(file1,"r")
p1=f10.read()
q1=p1.find("STP")
if(q1==-1):
    print("NO END STATEMENT PROVIDED")
else:
    listloop()   
    while(more_input):
        y=f1.readline()
        y=y.strip()
        a=type1(y)
        if(y=="STP"):
            more_input=False
            l_c=l_c+1
            count=count+1

        else:
            if(y[0]=="#"):
                count=count+1
                continue 
            if(a==1 and  y!="STP"):
                q=valop(y)
                p=exvar(y)
                if(q==-1 or  p==-1):
                    print("Invalid Opcode Cannot be compiled or excess or less operands provided at line " +str(count))
                    l_c=l_c+1
                    count=count+1
                    continue
                else:
                    print("")
                    l_c=l_c+1
                    count=count+1
            elif(a==2):
                q=valop(y)
                p=exvar(y)
                if(q==-1  or p==-1):
                    print("Invalid Opcode Cannot be compiled or excess or less operands provided at line "+ str(count))
                    l_c=l_c+1
                    count=count+1

                    continue
                else:    
                    l1=y.split(" ")
                    if(l1[0][-1]==":"):
                        symbol.append(["Label",l1[0][0:len(l1[0])-1],l_c])
                        label.append([l1[0][0:len(l1[0])-1],l_c])
                        l_c=l_c+1
                        count=count+1

                        
                    else:
                        if(l1[0]=="BRP" or l1[0]=="BRN" or l1[0]=="BRP"):
                            if(l1[1] in looptemp):
                                print()
                            else:
                                print("Label not defined but used at line " + str(l_c))
                        else:    
                            symbol.append(["Variable ",l1[1]])
                            z=findvar(l1[1])
                            
                            if(z==-1):
                                print("variable not defined")
                            else:
                                operands.append(z)
                        l_c=l_c+1
                        count=count+1

                        
            elif(a==3): 
                q=valop(y)
                p=exvar(y)
                l1=y.split(" ")
                if(q==-1 or p==-1):
                    print("Invalid Opcode Cannot be compiled or excess or less operands provided at line " + str(count))
                    l_c=l_c+1
                    count=count+1
                    continue
                else:
                    symbol.append(["Label",l1[0][0:len(l1[0])-1],l_c])
                    symbol.append(["Variable",l1[2]])
                    z=findvar(l1[2])
                    
                    if(z==-1):
                        print("variable not defined")
                    else:
                        operands.append(z)
                    label.append([l1[0][0:len(l1[0])-1],l_c])
                    l_c=l_c+1
                    count=count+1

            else:
                print("Invalid Opcode Cannot be compiled or excess or less operands provided at line " + str(count))
                l_c=l_c+1
                count=count+1
            if(l_c>255):
                print("Exceeded the available bits")
    fsymbol=[]
    foperands=[]
    flabel=[]
    for x in label:
        if x not in flabel:
            flabel.append(x)
    for x in symbol:
        if x not in fsymbol:
            fsymbol.append(x)
    for x in operands:
        if x not in foperands:
            foperands.append(x)
    for x in flabel:
        flabel1.append(x[0])
    error1=0
    for x in flabel1:
        a=flabel1.count(x)
        if(a>1):
            error1=-1
            break
        else:
            continue
    if(error1==-1):
        print("Labels with different address but same name have been used")
    else:
        f7=open(file1,"r")
        b=f7.read()
        b=b.replace("ADD",opcode_1["ADD"])
        b=b.replace("CLA",opcode_1["CLA"])
        b=b.replace("LAC",opcode_1["LAC"])
        b=b.replace("SAC",opcode_1["SAC"])
        b=b.replace("SUB",opcode_1["SUB"])
        b=b.replace("BRZ",opcode_1["BRZ"])
        b=b.replace("BRN",opcode_1["BRN"])
        b=b.replace("BRP",opcode_1["BRP"])
        b=b.replace("INP",opcode_1["INP"])
        b=b.replace("DSP",opcode_1["DSP"])
        b=b.replace("MUL",opcode_1["MUL"])
        b=b.replace("DIV",opcode_1["DIV"])
        b=b.replace("STP",opcode_1["STP"])
        for x in flabel:
            b=b.replace(x[0],binf(bin(x[1])))


        for x in foperands:
            b=b.replace(x[0],binf(bin(x[2])))
        """for x in range(-128,-1):
            s=" "+str(x)
            b=b.replace(s," "+binn(bin(x)))
        for x in range(3,128):
            s=" "+str(x)
            if(x!=1 or x!=0):
                b=b.replace(s," "+binf(bin(x)))"""
    
        
        with open("Output.txt",'w',encoding = 'utf-8') as f:
            f.write(b)
print(symbol)
print(flabel1)
print(foperands)
        



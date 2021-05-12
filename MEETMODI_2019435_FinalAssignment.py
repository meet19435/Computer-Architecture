import math
def power_2(a,p):
    if(a==1):
        return p
    else:
        return power_2(a/2,p+1)
def to_bin(s1,s):
    if(len(s1)==1):
        if(s1[0]=="0"):
            return s+"0000"
        if(s1[0]=="1"):
            return s+"0001"
        if(s1[0]=="2"):
            return s+"0010"
        if(s1[0]=="3"):
            return s+"0011"
        if(s1[0]=="4"):
            return s+"0100"
        if(s1[0]=="5"):
            return s+"0101"
        if(s1[0]=="6"):
            return s+"0110"
        if(s1[0]=="7"):
            return s+"0111"
        if(s1[0]=="8"):
            return s+"1000"
        if(s1[0]=="9"):
            return s+"1001"
        if(s1[0]=="A"):
            return s+"1010"
        if(s1[0]=="B"):
            return s+"1011"
        if(s1[0]=="C"):
            return s+"1100"
        if(s1[0]=="D"):
            return s+"1101"
        if(s1[0]=="E"):
            return s+"1110"
        if(s1[0]=="F"):
            return s+"1111"
    else:
        if(s1[0]=="0"):
            return to_bin(s1[1:],s+"0000")
        if(s1[0]=="1"):
            return to_bin(s1[1:],s+"0001")
        if(s1[0]=="2"):
            return to_bin(s1[1:],s+"0010")
        if(s1[0]=="3"):
            return to_bin(s1[1:],s+"0011")
        if(s1[0]=="4"):
            return to_bin(s1[1:],s+"0100")
        if(s1[0]=="5"):
            return to_bin(s1[1:],s+"0101")
        if(s1[0]=="6"):
            return to_bin(s1[1:],s+"0110")
        if(s1[0]=="7"):
            return to_bin(s1[1:],s+"0111")
        if(s1[0]=="8"):
            return to_bin(s1[1:],s+"1000")
        if(s1[0]=="9"):
            return to_bin(s1[1:],s+"1001")
        if(s1[0]=="A"):
            return to_bin(s1[1:],s+"1010")
        if(s1[0]=="B"):
            return to_bin(s1[1:],s+"1011")
        if(s1[0]=="C"):
            return to_bin(s1[1:],s+"1100")
        if(s1[0]=="D"):
            return to_bin(s1[1:],s+"1101")
        if(s1[0]=="E"):
            return to_bin(s1[1:],s+"1110")
        if(s1[0]=="F"):
            return to_bin(s1[1:],s+"1111")
def to_dec(s):
    temp=s[::-1]
    sum=0
    for x in range(len(temp)):
        t=int(temp[x])
        if(t==1):
            sum=sum+pow(2,x)

    return  sum
def search(s,l1):
    for x in range(len(l1)):
        if(l1[x][0]==1 and l1[x][1]==s):
            return x
            break
    return -1
        
#Words are assumed to be 16 bit
print("Enter number of cache lines")
cl=int(input())
print("Enter the block size")
bs=int(input())
#cl=int(cs/bs)
bb=power_2(bs,0)
cc=power_2(cl,0)
tb=16
offset_bits=bb
blocklength=16-bb
if(blocklength<0):
    print("NOT A VALID INPUT BLockLength cannot be negative")
tag_bit=16-offset_bits-cc
if(tag_bit<0):
   print("THE INPUT ARE NOT VALID  TagBits cannot be negative ")
testf=open("text1.txt",'r')
testf1=testf.readline()
testv=0
while(testf1!=""):
    testf1=testf1[:-1]
    ltest=testf1.split(" ")
    if(len(ltest[1])>4):
        testv=-1
        break
    testf1=testf.readline()
if(testv==-1):
    print("INVALID INPUT ADDRESS GREATER THAN 16 BITS")
else:
    print("DIRECT MAPPING Of Cache Memory")
    print("NUMBER OF CACHE LINES BITS "+str(cc))
    print("NUMBER OF OFFSET(WORD) BITS "+str(offset_bits))
    print("NUMBER OF TAG-BITS "+ str(tag_bit))
    cache_str=[]
    for x in range(cl):
        new_l1=[]
        for y in range(bs):
            new_l1.append(-1)
        cache_str.append([0,"",new_l1])
    y2=open("text1.txt",'r')
    y3=y2.readline()
    while(y3!=""):
        y3=y3[:-1]
        l2=y3.split(" ")
        if(l2[0]=="WRITE"):
            a=to_bin(l2[1],"")
            linebits=a[tag_bit:tag_bit+cc]
            tagbits=a[0:tag_bit]
            line=to_dec(linebits)
            off_bit=a[tag_bit+cc:]
            c=to_dec(off_bit)
            if(cache_str[line][0]==1):
                cache_str[line][0]=1
                cache_str[line][1]=tagbits
                cache_str[line][2][c]=l2[2]
                print("Cache is replaced by "+tagbits+" At line "+str(line))
            else:
                cache_str[line][0]=1
                cache_str[line][1]=tagbits
                cache_str[line][2][c]=l2[2]
                
        elif(l2[0]=="READ"):
            a=to_bin(l2[1],"")
            b=to_dec(a)
            linebits=a[tag_bit:tag_bit+cc]
            tagbits=a[0:tag_bit]
            line=to_dec(linebits)
            off_bit=a[tag_bit+cc:]
            c=to_dec(off_bit)
            if(cache_str[line][0]==0):
                print("Address Missing")
                cache_str[line][0]=1
                cache_str[line][1]=tagbits
                cache_str[line][2][c]="null"
                print("Address "+tagbits+" is stored at line "+str(line)+ " With default data null ")
            else:
                if(cache_str[line][1]==tagbits and cache_str[line][2][c]!=-1):
                    print("It's A HIT")
                    print(cache_str[line][2][c])
                else:
                    print("Address Missing")
                    cache_str[line][1]=tagbits
                    cache_str[line][2][c]="null"
                    print("Cache is replaced by "+tagbits+" At line "+str(line)+" With default data null ")
                    
        y3=y2.readline()
    print("LINE","DATA_P","TAGBITS","     DATA",sep=" | ")
    for x in range(cl):
        if(cache_str[x][0]==1):
            print(x,cache_str[x][0],cache_str[x][1],cache_str[x][2],sep="   |   ")
    tag_bits_set=16-offset_bits
    cache_str1=[]
    print("FULLY ASSOCIATIVE MAPPING of cache Memory")
    print("Number of TAG-BITS are "+ str(tag_bits_set))
    for x in range(cl):
        new_l2=[]
        for y in range(bs):
            new_l2.append(-1)
        cache_str1.append([0,"",new_l2])
    a1=open("text1.txt",'r')
    f1=a1.readline()
    size=0
    while(f1!=""):
        f1=f1[:-1]
        t1=f1.split(" ")
        if(t1[0]=="WRITE"):
            d=to_bin(t1[1],"")
            tag_bits1=d[:tag_bits_set]
            e=d[tag_bits_set:]
            f=to_dec(e)
            if(size==cl):
                size=0
            z=search(tag_bits1,cache_str1)
            if(z!=-1):
                cache_str1[z][2][f]=t1[2]
                
            elif(cache_str1[size][0]==1):
                cache_str1[size][0]=1
                cache_str1[size][1]=tag_bits1
                cache_str1[size][2][f]=t1[2]
                print("Cache Has been replaced by address " +tag_bits1+" At line "+ str((size)))
                size=size+1
            else:
                cache_str1[size][0]=1
                cache_str1[size][1]=tag_bits1
                cache_str1[size][2][f]=t1[2]
                size=size+1
        elif(t1[0]=="READ"):
            d=to_bin(t1[1],"")
            tag_bits1=d[:tag_bits_set]
            z=search(tag_bits1,cache_str1)
            e=d[tag_bits_set:]
            f=to_dec(e)
            if(size==cl):
                size=0
            if(z==-1):
                print("ADDRESS MISSING")
                cache_str1[size][0]=1
                cache_str1[size][1]=tag_bits1
                cache_str1[size][2][f]="null"
                print("Cache Has been replaced by address " +tag_bits1+" At line "+ str((size))+" With default data null")
                size=size+1
            elif(cache_str1[z][2][f]!=-1):
                print("It's A HIT")
                print(cache_str1[z][2][f])
            else:
                print("Address Missing")
                cache_str1[z][0]=1
                cache_str1[z][1]=tag_bits1
                cache_str1[z][2][f]="null"
                print("Cache Has been replaced by address " +tag_bits1+" At line "+ str((z))+" With default data null")
        f1=a1.readline()
    print("LINE","DATA_P","TAGBITS","                   DATA",sep=" | ")
    for x in range(cl):
        if(cache_str1[x][0]==1):
            print(x,cache_str1[x][0],cache_str1[x][1],cache_str1[x][2],sep="     |     ")
    print("ASSOCIATIVE MAPPING of cache Memory")
    print("Enter the value of n for n-set associative Mapping")
    n_set=int(input())
    if(n_set>cl):
        print("Invalid Input. Number of lines less than the set")
    else:
        nl_set=int(cl/n_set)
        cache_str2=[]
        for x in range(n_set):
            new_l4=[]
            for z in range(nl_set):
                new_l3=[]
                for y in range(bs):
                    new_l3.append(-1)
                new_l4.append([0,"",new_l3])
            cache_str2.append(new_l4)
        size_list=[]
        for x in range(n_set):
            size_list.append(0)
        file1=open("text1.txt",'r')
        fileline=file1.readline()
        tag_bits_fin=16-offset_bits
        while(fileline!=""):
            fileline=fileline[:-1]
            list_fin=fileline.split(" ")
            if(list_fin[0]=="WRITE"):
                k=to_bin(list_fin[1],"")
                i=k[:tag_bits_fin]
                j=to_dec(i)
                l=k[tag_bits_fin:]
                m=to_dec(l)
                set_number=j%n_set
                set1=cache_str2[set_number]
                z1=search(i,set1)
                if(size_list[set_number]==len(set1)):
                    size_list[set_number]=0
                if(z1!=-1):
                    set1[z1][2][m]=list_fin[2]
                elif(set1[size_list[set_number]]==1):
                    set1[size_list[set_number]][0]=1
                    set1[size_list[set_number]][1]=i
                    set1[size_list[set_number]][2][m]=list_fin[2]
                    print("Cache Has been replaced by address " + i +" At line "+ str((size_list[set_number]))+ " of Block "+ str(set_number))
                    size_list[set_number]=size_list[set_number]+1
                else:
                    set1[size_list[set_number]][0]=1
                    set1[size_list[set_number]][1]=i
                    set1[size_list[set_number]][2][m]=list_fin[2]
                    size_list[set_number]=size_list[set_number]+1
            elif(list_fin[0]=="READ"):
                k=to_bin(list_fin[1],"")
                i=k[:tag_bits_fin]
                j=to_dec(i)
                l=k[tag_bits_fin:]
                m=to_dec(l)
                set_number=j%n_set
                set2=cache_str2[set_number]
                z2=search(i,set2)
                if(size_list[set_number]==len(set2)):
                    size_list[set_number]=0
                if(z2==-1):
                    print("Address Missing")
                    set2[size_list[set_number]][0]=1
                    set2[size_list[set_number]][1]=i
                    set2[size_list[set_number]][2][m]="null"
                    print("Cache Has been replaced by address " + i +" At line "+ str((size_list[set_number]))+ " of Block "+ str(set_number)+" With default data null")
                    size_list[set_number]=size_list[set_number]+1
                elif(set2[z2][2][m]!=-1):
                    print("It's A HIT")
                    print(set2[z2][2][m])
                else:
                    print("Address Missing")
                    set2[z2][0]=1
                    set2[z2][1]=i
                    set2[z2][2][m]="null"
                    print("Cache Has been replaced by address " + i +" At line "+ str(z2)+ " of Block "+ str(set_number)+" With default data null")
                    
            fileline=file1.readline()
        for x in range(n_set):
            print("SET " + str(x))
            print("LINE","DATA_P","TAGBITS","                   DATA",sep=" | ")
            for y in range(nl_set):
                print(y,cache_str2[x][y][0],cache_str2[x][y][1],cache_str2[x][y][2],sep="   |    ")

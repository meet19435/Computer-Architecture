import math
def power_2(a,p):
    if(a==1):
        return p;
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
        
#Words are assumed to be 16 ++++`bit
print("Enter number of cache lines for level 1")
cl1=int(input())
print("Enter the block size")
bs=int(input())
cl2=cl1*2
#cl=int(cs/bs)
bb=power_2(bs,0)
cc1=power_2(cl1,0)
cc2=power_2(cl2,0)
tb=16
offset_bits=bb
blocklength=16-bb
if(blocklength<0):
    print("NOT A VALID INPUT BLockLength cannot be negative")
tag_bit1=16-offset_bits-cc1
tag_bit2=16-offset_bits-cc2
if(tag_bit1<0 or tag_bit2<0):
   print("THE INPUT ARE NOT VALID  TagBits cannot be negative ")
file=open("text1.txt",'r')
file1=file.readline()
testv=0
while(file1!=""):
    file1=file1[:-1]
    file_test=file1.split(" ")
    if(len(file_test[1])>4):
        testv=-1
        break
    file1=file.readline()
if(testv==-1):
    print("INVALID INPUT ADDRESS GREATER THAN 16 BITS")
   
else:
    print("DIRECT MAPPING Of Cache Memory with Two levels of Cache")
    print("NUMBER OF CACHE LINES BITS for level1 "+str(cc1))
    print("NUMBER OF TAG-BITS for level1 "+ str(tag_bit1))
    print("NUMBER OF CACHE LINES BITS for level2 "+str(cc2))
    print("NUMBER OF TAG-BITS for level2 "+ str(tag_bit2))
    print("NUMBER OF OFFSET(WORD) BITS for both levels is "+str(offset_bits))
    cache_str_level1=[]
    cache_str_level2=[]
    for x in range(cl1):
        new_l1=[]
        for y in range(bs):
            new_l1.append(-1)
        cache_str_level1.append([0,"",new_l1])
    for x in range(cl2):
        new_l1=[]
        for y in range(bs):
            new_l1.append(-1)
        cache_str_level2.append([0,"",new_l1])
    y=open("text1.txt",'r')
    yline=y.readline()
    while(yline!=""):
        yline=yline[:-1]
        l_1=yline.split(" ")
        if(l_1[0]=="WRITE"):
            add1=l_1[1]
            binad=to_bin(add1,"")
            tagb1=binad[0:tag_bit1]
            tagb2=binad[0:tag_bit2]
            line1=binad[tag_bit1:tag_bit1+cc1]
            line2=binad[tag_bit2:tag_bit2+cc2]
            word1=binad[tag_bit1+cc1:]
            word2=binad[tag_bit2+cc2:]
            fline1=to_dec(line1)
            fline2=to_dec(line2)
            fword1=to_dec(word1)
            fword2=to_dec(word2)
            if(cache_str_level1[fline1][0]==0 and cache_str_level2[fline2][0]==0):
                cache_str_level2[fline2][0]=1
                cache_str_level2[fline2][1]=tagb2
                cache_str_level2[fline2][2][fword2]=l_1[2]
                cache_str_level1[fline1][0]=1
                cache_str_level1[fline1][1]=tagb1
                cache_str_level1[fline1][2][fword1]=l_1[2]
            elif(cache_str_level1[fline1][0]==0 and cache_str_level2[fline2][0]==1):
                cache_str_level1[fline1][0]=1
                cache_str_level1[fline1][1]=tagb1
                cache_str_level1[fline1][2][fword1]=l_1[2]
                cache_str_level2[fline2][0]=1
                cache_str_level2[fline2][1]=tagb2
                cache_str_level2[fline2][2][fword2]=l_1[2]
                cache_str_level1[fline1][0]=1
            elif(cache_str_level1[fline1][0]==1 and cache_str_level2[fline2][0]==0):
                cache_str_level2[fline2][0]=1
                cache_str_level2[fline2][1]=tagb2
                cache_str_level2[fline2][2][fword2]=l_1[2]
            elif(cache_str_level1[fline1][0]==1 and cache_str_level2[fline2][0]==1):
                cache_str_level2[fline2][0]=1
                cache_str_level2[fline2][1]=tagb2
                cache_str_level2[fline2][2][fword2]=l_1[2]
                cache_str_level1[fline1][0]=1
                cache_str_level1[fline1][1]=tagb1
                cache_str_level1[fline1][2][fword1]=l_1[2]
                print("Cache structure has been replaced by "+tagb2+" AT the respective lines in both the cache levels")
        elif(l_1[0]=="READ"):
            add1=l_1[1]
            binad=to_bin(add1,"")
            tagb1=binad[0:tag_bit1]
            tagb2=binad[0:tag_bit2]
            line1=binad[tag_bit1:tag_bit1+cc1]
            line2=binad[tag_bit2:tag_bit2+cc2]
            word1=binad[tag_bit1+cc1:]
            word2=binad[tag_bit2+cc2:]
        
            fline1=to_dec(line1)
            fline2=to_dec(line2)
            
            fword1=to_dec(word1)
            fword2=to_dec(word2)
            
            if(cache_str_level1[fline1][0]==1):
                if(cache_str_level1[fline1][1]==tagb1 and cache_str_level1[fline1][2][fword1]!=-1):
                    print(cache_str_level1[fline1][2][fword1])
                elif(cache_str_level2[fline2][0]==1):
                    if(cache_str_level2[fline2][1]==tagb2 and cache_str_level2[fline2][2][fword2]!=-1):
                        print(cache_str_level2[fline2][2][fword2])
                        temp=cache_str_level2[fline2][2][fword2]
                        cache_str_level1[fline1][2][fword1]=temp
                        cache_str_level1[fline1][0]=1
                        cache_str_level1[fline1][1]=tagb1
        
                    else:
                        print("ADDRESS MISSING")
                        
            elif(cache_str_level2[fline2][0]==1):
                if(cache_str_level2[fline2][1]==tagb2 and cache_str_level2[fline2][2][fword2]!=-1):
                    print(cache_str_level2[fline2][2][fword2])
                    temp=cache_str_level2[fline2][2][fword2]
                    cache_str_level1[fline1][2][fword1]=temp
                    cache_str_level1[fline1][0]=1
                    cache_str_level1[fline1][1]=tagb1
                    
                    
                else:
                    print("ADDRESS MISSING")
                    
            else:
                print("ADDRESS MISSING")
                
                
        yline=y.readline()
    print("LEVEL 2")
    for x in range(cl2):
        print(x,cache_str_level2[x][0],cache_str_level2[x][1],cache_str_level2[x][2],sep="  |  ")
    print("LEVEL 1")
    for x in range(cl1):
        print(x,cache_str_level1[x][0],cache_str_level1[x][1],cache_str_level1[x][2],sep="  |  ")

    tag_bit_21=16-offset_bits
    tag_bit_22=16-offset_bits
    print("FULLY ASSOCIATIVE MAPPING WITH 2 LEVELS Of CACHE")
    print("NUMBER OF TAG BITS FOR LEVEL 1 IS "+str(tag_bit_21))
    print("NUMBER OF TAG BTIS FOR LEVEL 2 IS "+str(tag_bit_22))
    cache_str1_level1=[]
    cache_str1_level2=[]
    for x in range(cl1):
        new_l1=[]
        for y in range(bs):
            new_l1.append(-1)
        cache_str1_level1.append([0,"",new_l1])
    for x in range(cl2):
        new_l1=[]
        for y in range(bs):
            new_l1.append(-1)
        cache_str1_level2.append([0,"",new_l1])
    y1=open("text1.txt",'r')
    yline1=y1.readline()
    size_l1=0
    size_l2=0
    while(yline1!=""):
        yline1=yline1[:-1]
        l_2=yline1.split(" ")
        if(l_2[0]=="WRITE"):
            testbit=l_2[1]
            bins=to_bin(testbit,"")
            tagb=bins[0:tag_bit_21]
            word21=bins[tag_bit_21:]
            fword21=to_dec(word21)
            z_1=search(tagb,cache_str1_level1)
            z_2=search(tagb,cache_str1_level2)
            if(z_2!=-1):
                cache_str1_level2[z_2][2][fword21]=l_2[2]
                print("CACHE HAS BEEN REPLACED BY THE  "+ tagb)
            if(z_1!=-1):
                cache_str_level2[z_1][2][fword21]=l_2[2]
                print("CACHE HAS BEEN REPLACED BY THE  "+ tagb)
            if(size_l2<cl2 and size_l1<cl1):
                cache_str1_level2[size_l2][0]=1
                cache_str1_level2[size_l2][1]=tagb
                cache_str1_level2[size_l2][2][fword21]=l_2[2]
                cache_str1_level1[size_l1][0]=1
                cache_str1_level1[size_l1][1]=tagb
                cache_str1_level1[size_l1][2][fword21]=l_2[2]
                size_l1=size_l1+1
                size_l2=size_l2+1
            elif(size_l2<cl2 and size_l1>=cl1):
                cache_str1_level2[size_l2][0]=1
                cache_str1_level2[size_l2][1]=tagb
                cache_str1_level2[size_l2][2][fword21]=l_2[2]
                size_l2=size_l2+1
            elif(size_l2==cl2 and size_l1==cl1):
                size_l2=0
                size_l1=0
                cache_str1_level2[size_l2][0]=1
                cache_str1_level2[size_l2][1]=tagb
                cache_str1_level2[size_l2][2][fword21]=l_2[2]
                print("Cache has been replaced by "+tagb)
                size_l2=size_l2+1
        elif(l_2[0]=="READ"):
                testbit=l_2[1]
                bins=to_bin(testbit,"")
                tagb=bins[0:tag_bit_21]
                word21=bins[tag_bit_21:]
                fword21=to_dec(word21)
                z_1=search(tagb,cache_str1_level1)
                z_2=search(tagb,cache_str1_level2)
                if(z_1!=-1):
                    if(cache_str1_level1[z_1][2][fword21]!=-1):
                        print(cache_str1_level1[z_1][2][fword21])
                elif(z_2!=-1):
                    if(cache_str1_level2[z_2][2][fword21]!=-1):
                        print(cache_str1_level2[z_2][2][fword21])
                        if(size_l1==cl1):
                            size_l1=0
                        temp=cache_str1_level2[z_2][2][fword21]   
                        cache_str1_level1[size_l1][0]=1
                        cache_str1_level1[size_l1][1]=tagb
                        cache_str1_level1[size_l1][2][fword21]=temp
                        size_l1=size_l1+1
                    else:
                        print("Address Missing")
                else:
                    print("Address Missing")
                        
            
        yline1=y1.readline()
    print("Level 1")
    for x in range(cl1):
        if(cache_str1_level1[x][0]==1):
            print(x,cache_str1_level1[x][0],cache_str1_level1[x][1],cache_str1_level1[x][2],sep="   |   ")
    print(" ")
    print("Level 2")
    for x in range(cl2):
        if(cache_str1_level2[x][0]==1):
            print(x,cache_str1_level2[x][0],cache_str1_level2[x][1],cache_str1_level2[x][2],sep="   |   ")
        

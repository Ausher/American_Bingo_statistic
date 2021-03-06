from itertools import combinations
from scipy.special import comb
import pandas as pd

totalbals=75
totaldraw=44
totalprob=comb(totalbals,totaldraw)
prob=[comb(totalbals-x,totaldraw-x)/totalprob for x in range(0,25)]
#print(prob)

AllList={
'whitecross':[[
    11111,
    11011,
    10001,
    11011,
    11111]],
'p4L1234':[[
    11111,
    11111,
    11011,
    11111,
    00000]],
'p4L1235':[[
    11111,
    11111,
    11011,
    00000,
    11111]],
'p4L1245':[[
    11111,
    11111,
    00000,
    11111,
    11111]],
'p4L1345':[[
    11111,
    00000,
    11011,
    11111,
    11111]],
'p4L2345':[[
    00000,
    11111,
    11011,
    11111,
    11111]],
'square':[[
    11111,
    10001,
    10001,
    10001,
    11111]],
'p3L123':[[
    11111,
    11111,
    11011,
    00000,
    00000]],
'p3L124':[[
    11111,
    11111,
    00000,
    11111,
    00000]],
'p3L125':[[
    11111,
    11111,
    00000,
    00000,
    11111]],
'p3L134':[[
    11111,
    00000,
    11011,
    11111,
    00000]],
'p3L135':[[
    11111,
    00000,
    11011,
    00000,
    11111]],
'p3L145':[[
    11111,
    00000,
    00000,
    11111,
    11111]],
'p3L234':[[
    00000,
    11111,
    11011,
    11111,
    00000]],
'p3L235':[[
    00000,
    11111,
    11011,
    00000,
    11111]],
'p3L245':[[
    00000,
    11111,
    00000,
    11111,
    11111]],
'p3L345':[[
    00000,
    00000,
    11011,
    11111,
    11111]],
'Xshape':[[
    10001,
    '01010',
    00000,
    '01010',
    10001]],
'Tshape':[[
    11111,
    '00100',
    00000,
    '00100',
    '00100']],
'p2L12':[[
    11111,
    11111,
    00000,
    00000,
    00000]],
'p2L13':[[
    11111,
    00000,
    11011,
    00000,
    00000]],
'p2L14':[[
    11111,
    00000,
    00000,
    11111,
    00000]],
"p2L15":[[
    11111,
    00000,
    00000,
    00000,
    11111]],
'p2L23':[[
    00000,
    11111,
    11011,
    00000,
    00000]],
'p2L24':[[
    00000,
    11111,
    00000,
    11111,
    00000]],
'p2L25':[[
    00000,
    11111,
    00000,
    00000,
    11111]],
'p2L34':[[
    00000,
    00000,
    11011,
    11111,
    00000]],
'p2L35':[[
    00000,
    00000,
    11011,
    00000,
    11111]],
'p2L45':[[
    00000,
    00000,
    00000,
    11111,
    11111]],
'fouredge':[[
    10001,
    00000,
    00000,
    00000,
    10001]],
'slash':[[
    '10000',
    '01000',
    00000,
    '00010',
    '00001']],
'slashR':[[
    '00001',
    '00010',
    00000,
    '01000',
    '10000']],
'full':[[
    '11111',
    '11111',
    '11011',
    '11111',
    '11111'
]]}

for name,pattern in AllList.items():#??????????????????????????????
    x=str()
    for lines in pattern[0]:
        x+=str(lines).zfill(5)
    AllList[name].append(x)

for name,pattern in AllList.items():#????????????????????????
    containlist=[]
    for name2,pattern2 in AllList.items():
        contain=0
        for x in range(0,25):#?????????????????????

            if pattern2[1][x]==pattern[1][x]:
                contain+=1
            elif pattern2[1][x]=='1' and pattern[1][x]=='0':
                contain+=1

        if contain==25 and name != name2:#5???????????????????????????2????????????????????????
            containlist.append(name2)
    AllList[name].append(containlist)

for name,pattern in AllList.items():
    if len(pattern[2]) >0:
        directcontain=pattern[2].copy()

    #print(directcontain)
        for p in pattern[2]:#??????????????????????????? p ???????????????
            #print('___________??????'+name)
            #print('????????????'+p)
            #print('????????????')
           #print( AllList[p][1])
            #print(directcontain)
            for q in AllList[p][2]:
                #print('??????????????????'+q)
                if q in directcontain:
                    #print('????????????'+q)
                    directcontain.remove(q)
                #print(directcontain)
        AllList[name].append(directcontain)
    else:
     AllList[name].append([])

#print(AllList)

for name,pattern in AllList.items():
    #print('_________________________________________________')
    #print(name)
    markrequire=str(AllList[name][1]).count('1')#?????????????????????????????????
    prob_of_name= prob[markrequire]#???????????????????????????
    prob_of_name_amend=prob_of_name#?????????????????????????????????????????????
    #print(prob_of_name)
    directcontainNumber=len(AllList[name][3])#?????????????????????????????????????????????
    if directcontainNumber>0:
        for patterncomb in range(directcontainNumber,0,-1): #???????????????????????????????????????
            if patterncomb%2==0:#??????????????????????????????
                amend=1
            else:
                amend=-1
            

            comblist=list(combinations(AllList[name][3],patterncomb))#????????????
            #print(comblist)

            for amendcombin in comblist:#????????????
                x=list('0000000000000000000000000')
                for sub_amendcombin in amendcombin:#???????????????
                    #print(sub_amendcombin)
                    #print(AllList[sub_amendcombin][3])
                    i=0
                    for strnumber in AllList[sub_amendcombin][1]:#????????????????????????
                        if strnumber=='1':
                            x[i]='1'
                        i+=1
                #print(x)
                markx=x.count('1')
                #print(markx)
                #print(amend)
                #print(prob[markx]*amend)
                prob_of_name_amend+=prob[markx]*amend
                #print(prob_of_name_amend)
    #print(prob_of_name_amend)
    AllList[name].append("{:.8f}%".format(prob_of_name*100))
    AllList[name].append("{:.8f}%".format(prob_of_name_amend*100))
AllList=pd.DataFrame.from_dict(AllList,orient='index').rename(columns={3:'direct_related',4:'probability',5:'Amend_probability'})
AllList=AllList.iloc[:,[3,4,5]]
print(AllList)
AllList.to_excel('??????????????????.xlsx')
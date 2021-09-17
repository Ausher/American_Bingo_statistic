# American_Bingo_statistic 美式賓果計算
## How to calculate probability American Bingo for special shapes 如何計算美式賓果特殊圖形的機率
## 算滿版以及各種圖形的發生機率  
### 概要  
這邊用X型程式碼做為介紹,基本上需要在圖形上任選8個點的圖形都適用一樣的規則僅需改變特定點的抽取位置,如T型或是傳過中間點的十字型  
表格位置編號game card square position
---

![image](https://user-images.githubusercontent.com/31215642/133708671-b1e2021a-c9cb-4997-8bb3-903ffa5e10ca.png)
---
The game card is composed of 5X5,but the central is free which means the one default of any number .  
Therefor, only 24 squares will be choose. If we consider each single square could be 2 kinds of status (1=bits,0=not bits)  
The number of combinations is 2^24=16777216, then we transfer the number from 0-16777215 into binary and filled the number into 24 digits.  
e.g. 2 could transfer into binary as 10, filled the digit into 24, thus 2 will become  00000000000000000000010  the first of right represent the position 0 of game card, second of right repesent position 1 etc.  
Thus 2 will represent except postion 22 is bits others are not bits as the image below  

![image](https://user-images.githubusercontent.com/31215642/133711427-ff8f43a6-9a48-4f1c-b346-270a0b45f9d7.png)

until 16777215 will become 111111111111111111111111  

Then we pick the position we want e.g for X shape will pick up positon 0,6,17,23,4,8,15,19 if all of the positions are 1, the combination is match the X shape  

The code will count the number of match under the number of bits,e.g. For X shape if bits 8 numbers will only 1 combination match, 9 bits will 16 combination etc. untill 24bits  

than divide the total combinations under the number of bits, e.g the probability X shape happened when bits 8 numbers will be 1/combin(24,8), combin(X,Y) means from X number pick up Y number without order,bit 9 will be 16/combine(24,9) etc. and sum up all of them will have the probility of this special shape.  

# its not over yet!!!  
this part is no include in the code, but its easy calculate by excel with conbin() formula
we still need to calculate the probility of bits, if total number is T, the number we pick up is P, the bits number is B, total squares need to choose on game card is 24  
the combination will be combin(24,B)/combin(T-24,P-B) and devide the total combination of pick up is combin(T,P)  
the formula will be {[combin(24,B)/combin(T-24,P-B)]/combin(T,P)}  
e.g. if we pick up 44 numbers from 75 numbers and with 8 bits  
{[combin(24,8)/combin(75-24,44-8)]/combin(75,44)}=2.34518E+18/1.13499E+21=0.00206626126  

# Now is the final part
we make multiply two posibilities shape and bits  
for example  
posibility of 8 bits with X shape will be 1/combin(24,8) * 0.00206626126=0.000000002809439475
posibility of 9 bits with X shape will be 16/combin(24,9) * {[combin(24,9)/combin(75-24,44-9)]/combin(75,44)}=0.0000001011398211
need to sun up all of bits till B=24

the websit is a good referance http://www.durangobill.com/BingoHowTo.html  


```



import pandas as pd
bitslist={}
for i in range(0,16777216):                   # generate number and change into binary and filled up to 24 digits, the number transferd is a combination of position
    x=bin(i).replace('0b','').zfill(24)         
    nbbits=x.count('1')                       #count the number of bits in this combination
    line=str(11111111)                        #the number need to match on the card,the X shape require 8 so str(11111111) if only need 4 ,like single diagonal, will be                                                      str(1111)

    try :
        combinnumber=bitslist[nbbits]         #since the bitslist is an empty dict, if its first match will set as 0, otherwise use the previous record
    except:
        combinnumber=0
    if x[0]+x[6]+x[17]+x[23]+x[4]+x[8]+x[15]+x[19]==line: #match the position of combination with the shape ,if equal means the combination matched, the position should be  
        combinnumber+=1                                    changed if use other shape X[0] means position 0
        bitslist[nbbits]=combinnumber                     # update the latest record fo bitslist
bitslist=pd.DataFrame.from_dict(bitslist,orient='index')
print(bitslist)    

```
the result will be first col1 is the number of bits, col2 is the number of combination which match the shape  
```
        0
8       1
9      16
10    120
11    560
12   1820
13   4368
14   8008
15  11440
16  12870
17  11440
18   8008
19   4368
20   1820
21    560
22    120
23     16
24      1
```

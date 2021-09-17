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
e.g. 2 could transfer into binary as 10, filled the digit into 24, thus 2 will become  00000000000000000000010  the first of right represent the position 0 of game card, second of right repesent position 1 etc. Thus 2 will represent except postion 22 is bits others are not bits as the image below

![image](https://user-images.githubusercontent.com/31215642/133711427-ff8f43a6-9a48-4f1c-b346-270a0b45f9d7.png)

until 16777215 will become 111111111111111111111111
```



import pandas as pd
bitslist={}
for i in range(0,16777216):                   
    x=bin(i).replace('0b','').zfill(24)         
    nbbits=x.count('1')
    line=str(11111111)

    try :
        combinnumber=bitslist[nbbits]
    except:
        combinnumber=0
    if x[0]+x[6]+x[17]+x[23]+x[4]+x[8]+x[15]+x[19]==line:
        combinnumber+=1
        bitslist[nbbits]=combinnumber
bitslist=pd.DataFrame.from_dict(bitslist,orient='index')
print(bitslist)    



```

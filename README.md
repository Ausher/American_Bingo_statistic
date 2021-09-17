# American_Bingo_statistic 美式賓果計算
## How to calculate probability American Bingo for special shapes 如何計算美式賓果特殊圖形的機率
## 算滿版以及各種圖形的發生機率
### 概要
這邊用X型程式碼做為介紹,基本上需要在圖形上任選8個點的圖形都適用一樣的規則僅需改變特定點的抽取位置,如T型或是傳過中間點的十字型
表格位置編號
---

![image](https://user-images.githubusercontent.com/31215642/133708671-b1e2021a-c9cb-4997-8bb3-903ffa5e10ca.png)
---
#the game card is composed of 5X5,but the central is free which means the free one can be any number.
Therefor, only 24 squares will be choose. If we consider each single square could be 2 kinds of status (1=bits,0=not bits)
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

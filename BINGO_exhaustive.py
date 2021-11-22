
from scipy.special import comb

bitslist={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0}
Pattern_list={}
sumup_list={}
total=comb(75,44)
motherpro=[comb(51,44-matchnb)/total for matchnb in range(25)]
for i in range(0,16777216):#represent all kinds of hit spaces with binary way, 1 is hit,0 is not hit. Totla kinds will be 2^24

    x=bin(i).replace('0b','').zfill(24)
    nbbits=x.count('1')
    if i in range(0,16777216,1000000):
        print(i*100/16777216)
    combinnumber=bitslist[nbbits]
    #each slice is for pattern to match hit or not, refer from Excel to know the position of space
    #the patterns after # is the complete related with Higher odds patterns	respectively
    full=x[0:5]+x[5:10]+x[10:14]+x[14:19]+x[19:24]
    whitecross=x[0:5]+x[5]+x[6]+x[8]+x[9]+x[10]+x[13]+x[14]+x[15]+x[17]+x[18]+x[19:24]#full
    p4L1234=x[0:5]+x[5:10]+x[10:14]+x[14:19]#full
    p4L1235=x[0:5]+x[5:10]+x[10:14]+x[19:24]#full
    p4L1245=x[0:5]+x[5:10]+x[14:19]+x[19:24]#full
    p4L1345=x[0:5]+x[10:14]+x[14:19]+x[19:24]#full
    p4L2345=x[5:10]+x[10:14]+x[14:19]+x[19:24]#full
    square=x[0:5]+x[5]+x[9]+x[10]+x[13]+x[14]+x[18]+x[19:24]#full,whitecross
    p3L123=x[0:5]+x[5:10]+x[10:14]#p4L1234,p4L1235,full
    p3L124=x[0:5]+x[5:10]+x[14:19]#p4L1234,p4L1245,full
    p3L125=x[0:5]+x[5:10]+x[19:24]#p4L1235,p4L1245,full
    p3L134=x[0:5]+x[10:14]+x[14:19]#p4L1234,p4L1345,full
    p3L135=x[0:5]+x[10:14]+x[19:24]#p4L1235,p4L1345,full
    p3L145=x[0:5]+x[14:19]+x[19:24]#p4L1245,p4L1345,full
    p3L234=x[5:10]+x[10:14]+x[14:19]#p4L1234,p4L2345,full
    p3L235=x[5:10]+x[10:14]+x[19:24]#p4L1235,p4L2345,full
    p3L245=x[5:10]+x[14:19]+x[19:24]#p4L1245,p4L2345,full
    p3L345=x[10:14]+x[14:19]+x[19:24]#p4L1345,p4L2345,full
    XShape=x[0]+x[4]+x[6]+x[8]+x[15]+x[17]+x[19]+x[23]#p4L1245,whitecross,full
    TShape=x[0:5]+x[7]+x[16]+x[21]#-p4L1245,full
    p2L12=x[0:5]+x[5:10]#-p3L123,p3L124,p3L125,p4L1234,p4L1235,p4L1245,full
    p2L13=x[0:5]+x[10:14]#-p3L123,p3L134,p3L135,p4L1234,p4L1235,p4L1345,full
    p2L14=x[0:5]+x[14:19]#-p3L124,p3L134,p3L145,p4L1234,p4L1245,p4L1345,full
    p2L15=x[0:5]+x[19:24]#-p3L125,p3L135,p3L145,p4L1235,p4L1245,p4L1345,square,whitecross,full
    p2L23=x[5:10]+x[10:14]#-p3L123,p3L234,p3L235,p4L1234,p4L1235,p4L2345,full
    p2L24=x[5:10]+x[14:19]#-p3L124,p3L234,p3L245,p4L1234,p4L1245,p4L2345,full
    p2L25=x[5:10]+x[19:24]#-p3L125,p3L235,p3L245,p4L1235,p4L1245,p4L2345,full
    p2L34=x[10:14]+x[14:19]#-p3L134,p3L234,p3L345,p4L1234,p4L1345,p4L2345,full
    p2L35=x[10:14]+x[19:24]#-p3L135,p3L235,p3L345,p4L1235,p4L1345,p4L2345,full	
    p2L45=x[14:19]+x[19:24]#-p3L145,p3L245,p3L345,p4L1245,p4L1345,p4L2345,full
    fouredge=x[0]+x[4]+x[19]+x[23]#XShape,whitecross,p2L15,p3L125,p3L135,p3L145,square,p4L1235,p4L1245,p4L1345,full
    Slash=x[0]+x[6]+x[17]+x[23]#XShape,whitecross,p4L1245,full
    SlashR=x[19]+x[15]+x[8]+x[4]#XShape,whitecross,p4L1245,full


        
    name='XShape'#fill the name
    checking=XShape#fill the pattern
    Pattern_list=[p4L1245,whitecross,full]#fill the complete related with Higher odds patterns

    if checking.count('1')==len(checking):#check the patterns matched
        incould=0
        for pattern in Pattern_list:#check complete related
            if pattern.count('1')==len(pattern):
                incould+=1
        if incould==0:
            combinnumber+=1
        bitslist[nbbits]=combinnumber

        sumup=0
        for n in range(25):
            sumup+=bitslist[n]*motherpro[n]

        sumup_list[name]='{:.10}'.format(sumup)



print(sumup_list) 

 

 
  
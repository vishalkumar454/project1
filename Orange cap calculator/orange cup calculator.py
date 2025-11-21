# mini project : Orange cap calculator

def orange_cap(d):
     total = {}
     for k in d.keys():
         for n in d[k].keys():
             if n in total.keys():
                 total[n] = total[n] + d[k][n]
             else:
                 total[n] = d[k][n]

     print('total Run scored by each player in 2 tests = ',total)

     print('player with highest score')
     maxtotal = -1
     for n in total.keys():
         if total[n] > maxtotal:
            maxname = n
            maxtotal = total[n]

     return (maxname,maxtotal)

d = orange_cap({'test1':{'Dhoni':74,'Kohli':150},'test2':{'Dhoni':29,'pujara':42}})
print(d)
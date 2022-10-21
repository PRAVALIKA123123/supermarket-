from datetime  import datetime
name=input("Enter your name:")
#lists
lists='''
Rice   Rs 40/kg
Sugar  Rs 30/kg
Salt   Rs 25/kg
Oil    Rs 100/kg
Panner Rs 60/kg
Noodles Rs 45/kg
Boost  Rs 90/kg
Dal    Rs 120/kg
'''
print(lists)
# declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
finalamount=0
ilist=[]
qlist=[]
plist=[]
 
#  rates of items
items={'Rice':40,
'Sugar':30,
'Salt':25,
'Oil':100,
'Panner':60,
'Noodles':45,
'Boost':90,
'Dal':120}
option=int(input("for list of items enter 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you want to buy press 1, to exit press 2:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter the items:")
        quantity=int(input("Enter  quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")
    inp=input("do you want to bill: yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(26*"=","sree super market",26*"=")
            print(26*" ","HYDERABAD")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ","quantity",5*" ","price")
            for i in range(len(pricelist)):
                print(i,8*" ",2*" ",ilist[i],8*" ",qlist[i],14*" ",plist[i])
            print(75*" ")
            print(40*" ","TotalAmount:","Rs",totalprice)
            print(75*" ")
            print("gst amount",42*" ","Rs",gst)
            print(75*" ")
            print(40*" " ,"finalamount:","Rs",finalamount)
            print(75*"-")
            print(28*" ","Thanks for Visiting")
            print(75*"-")
                
            
            


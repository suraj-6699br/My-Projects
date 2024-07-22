from datetime import datetime

name=input ("enter your name:")

lists='''
Rice Rs 20/kg
Sugr  Rs 30/kg
salt  Rs 20/kg
oil Rs 80/kg
paneer Rs 110/kg
Maggi Rs 50/kg
Boost Rs 90/each
colgate Rs 85/each
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalamount=0
ilist=[]
qlist=[]
plist=[]

# rates for items
items={'rice':20,
'sugar':30,
'salt':20,
'oil':80,
'panner':110,'Maggi':50,'Boost':90,'colgate':85}
option=int(input("for list of items press 1 "))
if option==1:
 print(lists)
for i in range(len(items)):
  inp1=int(input("if you want to buy 1 or 2 for exit:"))
  if inp1==2:
    break
  if inp1==1:
    item=input("enter your items:")
    quantity=int(input("enter quantity:"))
    if item in items.keys():
      price=quantity*(items[item])
      pricelist.append((item,quantity,items,price))
      totalprice+=price
      ilist.append(item)
      qlist.append(quantity)
      plist.append(price)
      gst=(totalprice*18)/100
      finalamount=gst+totalprice
    else:
      print("sorry you entered item is not availalbe")
  else:
      print("you enter wrong number")
  inp=input("can i bill the items yes or no")
  if inp=='yes':
    pass
  if finalamount!=0:
    print(25*"=","suraj supermarket",25*"=")
    print(28*"=","kolar",34*"=")
    print("Name:",name,30*" ","Date:",datetime.now())
    print(75*"-")
    print("sno",8*" ",'items',10*" ",'Quantity',5*" ",'price')
    for i in range(len(pricelist)):
      print(i,11*' ',ilist[i],15*' ',qlist[i],9*" " ,plist[i])
      print(75*"-")
      print(50*" ",'TotalAmount:','Rs = ',totalprice)
      print("Gst amount",40*" ",'Rs = ',gst)
      print(75*"-")
      print(50*" ",'finalAmount:','Rs = ',finalamount)
    print(75*"-")
    print(25*" ","Thanks for visiting")
    print(75*"-")
      
      
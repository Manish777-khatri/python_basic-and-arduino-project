print("!!!!WELCOME!!!! \nTO HOTEL MOUNT EVEREST")
menu={
    "momo":100,
    "pizza":150,
    "coffee":80,
    "Burger":75,
    "chowmin":60,
    "colddrinks":105
    } 
answer=input("Can I  show you menu sir/mam ? =") 
if answer=="yes":
 print(" 1.mommo = Rs.100 \n 2.pizza = Rs.150\n 3.coffee = Rs.80\n 4.Burger = Rs.75\n 5.chowmin = Rs.60\n 6.colddrinks = Rs.105")
 Bill_Amount=0
 order_1=input("Select what you want to eat?=")
 if order_1 in menu:
  Bill_Amount+= menu[order_1]
  print(f"Your first order {order_1} has been added !!")

 else:
  print("This item is not available at our hotel !!!\n !!!SORRY!!!")
 que=input("DO you need anything else??(yes/no) =")
 if(que=="yes"): 
    order_2=input("ENter 2nd order:")
    if order_2 in menu:
     Bill_Amount+= menu[order_2]
     print(f"Your second order {order_2} has been added !!")
    #  print(f"YOUR total Bill is RS.{Bill_Amount}")
    else:
     print("This is not available!!")
 else:
#    print("This item is not available at our hotel !!!\n !!!SORRY!!!")
    print("Thank You!!")
 print(f"YOUR total Bill is RS.{Bill_Amount}")     
else:
 print("Thank you!!")
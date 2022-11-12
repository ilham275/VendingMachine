## Menu



import os
from threading import Thread


def Show_Menu():
    print("                        ")
    print("        MENU              ")
    print("                        ")
    print("                        ")
    print("1. Coca Cola Rp 5.000 ")
    print("2. Pulpy Orange Rp 6.000")
    print("3. Teh Pucuk Rp 7.000")
    print("4. Pocari sweet Rp 8.000")
    print("5. Teh Botol Rp 9.000")
    print("6. Yoghurt Cimory Rp 10.000")
    print("7. Nescafe Rp 11.000")
    print("8. C1000 Rp 12.000")
    print("9. Bear Brand Rp 13.000")
    print("10. Bintang Rp 14.000")
Show_Menu()
item = int(input("Choose The item : "))
while(item > 10):
    print("Choose the right item")
    item = int(input("Choose The item : "))
os.system('cls||clear')
    
## Saldo

saldo = int(input("Input Your Money : "));


    ## Check

        
        
    ##1
##2
##3

if item == 1:
    price = 5000
elif item == 2:
    price = 6000
elif item == 3:
    price = 7000
elif item == 4:
    price = 8000
elif item == 5:
    price = 9000
elif item == 6:
    price = 10000
elif item == 7:
    price = 11000
elif item == 8:
    price = 12000
elif item == 9:
    price = 13000
else:
    price = 14000
    
while (price > saldo):
    Tsaldo = saldo
    print("Your Amount of money is not Enough")
    saldo = int(input("Input Your Money : "));
    saldo += Tsaldo
    os.system('cls||clear')
    print("Balance Now", + saldo)
    
else:
        if item == 1:
            saldo -= price
            print("Your Drink Is Coca Cola")
            print("Balance Remaining", + saldo)
        elif item == 2:
            saldo -= price
            print("Your Drink Is Pulpy Orange")
            print("Balance Remaining", + saldo)
        elif item == 3:
            saldo -= price
            print("Your Drink Is Teh Pucuk")
            print("Balance Remaining", + saldo)
        elif item == 4:
            saldo -= price
            print("Your Drink Is Pocari sweet")
            print("Balance Remaining", + saldo)
        elif item == 5:
            saldo -= price
            print("Your Drink Is Teh Botol")
            print("Balance Remaining", + saldo)
        elif item == 6:
            saldo -= price
            print("Your Drink Is Yoghurt Cimory")
            print("Balance Remaining", + saldo)
        elif item == 7:
            saldo -= price
            print("Your Drink Is Nescafe")
            print("Balance Remaining", + saldo)
        elif item == 8:
            saldo -= price
            print("Your Drink Is C1000") 
            print("Balance Remaining", + saldo)
        elif item == 9:
            saldo -= price
            print("Your Drink Is Bear Brand")
            print("Balance Remaining", + saldo)
        else:
            saldo -= price
            print("Your Drink Is Bintang")
            print("Balance Remaining", + saldo)
next = int(input("Want Make Transaction Again : 1. Yes 2. No "));
while(next == 1):
    Show_Menu()
    item = int(input("Choose The item : "))
    while(item > 10):
        print("Choose the right item")
        item = int(input("Choose The item : "))
    os.system('cls||clear')
    if item == 1:
        price = 5000
    elif item == 2:
        price = 6000
    elif item == 3:
        price = 7000
    elif item == 4:
        price = 8000
    elif item == 5:
        price = 9000
    elif item == 6:
        price = 10000
    elif item == 7:
        price = 11000
    elif item == 8:
        price = 12000
    elif item == 9:
        price = 13000
    else:
        price = 14000
        
        
    while (price > saldo):
        Tsaldo = saldo
        print("Balance Remaining", + saldo)
        print("Saldo Belum Mencukupi")
        saldo = int(input("Input Your Money : "));
        saldo += Tsaldo
        os.system('cls||clear')
        print("Balance Remaining", + saldo)
        
    else:
        if item == 1:
            saldo -= price
            print("Your Drink Is Coca Cola")
            print("Balance Remaining", + saldo)
        elif item == 2:
            saldo -= price
            print("Your Drink Is Pulpy Orange")
            print("Balance Remaining", + saldo)
        elif item == 3:
            saldo -= price
            print("Your Drink Is Teh Pucuk")
            print("Balance Remaining", + saldo)
        elif item == 4:
            saldo -= price
            print("Your Drink Is Pocari sweet")
            print("Balance Remaining", + saldo)
        elif item == 5:
            saldo -= price
            print("Your Drink Is Teh Botol")
            print("Balance Remaining", + saldo)
        elif item == 6:
            saldo -= price
            print("Your Drink Is Yoghurt Cimory")
            print("Balance Remaining", + saldo)
        elif item == 7:
            saldo -= price
            print("Your Drink Is Nescafe")
            print("Balance Remaining", + saldo)
        elif item == 8:
            saldo -= price
            print("Your Drink Is C1000")
            print("Balance Remaining", + saldo)
        elif item == 9:
            saldo -= price
            print("Your Drink Is Bear Brand")
            print("Balance Remaining", + saldo)
        else:
            saldo -= price
            print("Your Drink Is Fibe Mini")
            print("Balance Remaining", + saldo)
    
    next = int(input("Want Make Transcaction Again? : 1. Yes 2. No "));
else:
    print("Thank You")

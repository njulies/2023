menulist=[]
pricelist=[]
def showbill():
    total=0
    for i in range(len(menulist)):
        print("เมนู %s ราคา %d "%(menulist[i],pricelist[i]))
        total+=pricelist[i]
    print(f"ราคารวม {total} บาท")
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower()=="exit":
        print("End Program")
        break
    else:
        menuPrice = int(input("Price : "))
        menulist.append(menuName)
        pricelist.append(menuPrice)
showbill()
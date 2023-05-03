menulist=[]
def showbill():
    total=0
    for i in range(len(menulist)):
        print(f"สินค้า {menulist[i][0]} ราคา {menulist[i][1]}")
while True:
    menuName = input("Please Enter Menu : ")
    if menuName.lower()=="exit":
        print("End Program")
        break
    else:
        menuPrice = int(input("Price : "))
        menulist.append([menuName,menuPrice])
showbill()
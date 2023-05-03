systemmenu={"ข้าวหมกไก่":50 ,"ข้าวไก่ทอด":55 ,"ข้าวมันไก่":40 ,"ข้าวหน้าไก่":45}
menulist=[]
def showbill():
    total=0
    for i in range(len(menulist)):
        total+=menulist[i][1]
        print(f"สินค้า {menulist[i][0]} ราคา {menulist[i][1]}")
    print(f"รวมราคา {total}")
while True:
    print(systemmenu)
    menuName = input("Please Enter Menu : ")
    if menuName.lower()=="exit":
        print("End Program")
        break
    else:
        menulist.append([menuName,systemmenu[menuName]])
        print(menulist)
showbill()
print()
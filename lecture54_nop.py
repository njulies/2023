def login():
    usernameinput=input("Username : ")
    passwordinput=input("Password : ")
    if usernameinput=="admin" and passwordinput=="1234":
        print("Login success")
        return showmenu()
    else:
        print("username or password is wrong")
        return login()
def showmenu():
    print("--- ABC Shope ---")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    return menuselect()
def menuselect():
    userselect=int(input("1 & 2 : "))
    if userselect==1:
        return vatcal()
    elif userselect==2:
        return pricecal()
    else:
        print("press 1 or 2")
        return menuselect()
def vatcal():
    price1=int(input("Price 1 : "))
    price2=int(input("Price 2 : "))
    vat=7
    result=(f"ราคารวม Vat : {(price1+price2)+((price1+price2)*7/100)} บาท")
    return result
def pricecal():
    price1=int(input("Price 1st Product : "))
    price2=int(input("Price 2nd Product : "))
    return vatcal(price1+price2)

print(login())




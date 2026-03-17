#define the menu of resturantant

menu = {
    'pizza': 40,
    'pasta':50,
    'burger':60,
    'sasled':70,
    'coffee':80,
}
print("welcome to python restaurant")
print("pizza:Rs40\npasta:Rs50\nburger:Rs60\nsasled:Rs70\ncoffee:Rs80",)

order_total=0

item1 = input("enter the name of item you want to order=")
if item1 in menu:
    order_total += menu[item1] 
    print("your item",item1,"has been added to your order")

else:
    print("ordered item",item1,"is not available yet")

another_order = input("do you want to add another item? (yes/no)")

if another_order == "yes":
    item2 = input("enter the name of second item=")
    if item2 in menu:
        order_total += menu[item2]
        print("item",item2,"has been added to order")
    else:
        print("odered item",item2,"is not available")

print("the total amount of item to pay",order_total)
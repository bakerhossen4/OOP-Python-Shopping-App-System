from user import Seller, Customer
from item import Item
from products import Product
from order import Order
from ordermanage import OrderManager

proob = Product( )
while True :
    print("........................................................")
    print("                    Shopping cart System                ")
    print(" 1 : Login as Seller ")
    print(" 2 : Login as Customer ")
    print(" 3 : View all Products ")
    print(" 4 : Exit ")
    print("........................................................")
    val = int(input("Enter Option : "))
    if val == 1 :
        selname = input("Enter Seller Name : ")
        selob = Seller( selname )
        while True :
            print("................................")
            print(f"    Welcome {selname}          ")
            print(" 1 : Add a product ")
            print(" 2 : View all Products ")
            print(" 3 : Edit Product Info ")
            print(" 4 : Back ")
            print("................................")
            data = int(input("Enter choice : "))
            if data == 1 :
                pname = input("Enter Product Name : ")
                pprice = 100 # default
                pqty = 50 # default
                itemob = Item(pname, pprice, pqty)
                proob.add_a_product( itemob )
            elif data == 2 :
                proob.show_all_products()
            elif data == 4:
                break
    elif val == 4:
        break
    elif val == 3:
        proob.show_all_products()
    elif val == 2 :
        cusname = input("Enter Customer Name : ")
        cusob = Customer( cusname )
        ordermanagerob = OrderManager( )
        while True :
            print("...............................")
            print(f"    Welcome {cusname}          ")
            print(" 1 : Buy a product ")
            print(" 2 : View all Products ")
            print(" 3 : View Cart ")
            print(" 4 : Back ")
            print("................................")
            data = int(input("Enter choice : "))
            if data == 1 :
                pname = input("Enter Product Name : ")
                pprice = proob.find_pprice( pname )
                if pprice < 0 :
                    print("......... Out of Stock ............")
                else :
                    pqty = int(input("Enter Product Qty : "))
                    orderob = Order( pname, pprice, pqty)
                    ordermanagerob.add_to_cart( orderob )
                    proob.update_product_qty(pname,pqty)
            elif data == 2 :
                proob.show_all_products()
            elif data == 3:
                ordermanagerob.my_cart()
            elif data == 4:
                break
            
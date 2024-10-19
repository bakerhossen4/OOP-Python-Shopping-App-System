
from order import Order
from products import Product

class OrderManager :
    def __init__(self):
        self.orderlist = []
    def add_to_cart ( self, ob ) :
        print("...............................")
        self.orderlist.append(ob)
        print(" Order Placed ")
        print("...............................")
    def my_cart( self ):
        print("...............................")
        print(" My cart  ")
        tot = 0
        print( f" Pname:  \t Unit Price \t  Qty  \t SubTotal " )
        for i in self.orderlist :
            print(f"{i.name}\t\t{i.price}\t\t{i.qty}\t\t {i.price * i.qty}")
            tot = tot + ( i.price * i.qty )
        print(f"---------------------------------- Total : \t\t { tot }")
        print("...............................")
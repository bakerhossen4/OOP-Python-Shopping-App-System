
class Product :
    def __init__(self):
        self.product_list = []
    def add_a_product( self, itemob ):
        print("................................")
        self.product_list.append(itemob)
        print(" Product Added ")
        print("................................")
    def show_all_products(self) :
        print("................................")
        print("       All Products         ")
        print(" Name \t\t Price \t\t Qty ")
        for i in self.product_list:
            print(f"{i.name}\t\t{i.price}\t\t{i.qty}")
        print("................................")
    def update_product_qty( self, name, qty ) :
        print("................................")
        for i in self.product_list:
            if i.name == name :
                i.qty = i.qty - qty
                print("Information Updated ")
        print("................................")
    def find_pprice( self, name ) :
        for i in self.product_list :
            if i.name == name :
                if i.qty == 0 :
                    return -1
                else :
                    return i.price
                    
class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item": item, "price": price, "quantity": quantity}
        self.cart.append(product)

    def checkOut(self):
        total = 0
        for item in self.cart:
            total += item["price"] * item["quantity"]
        return total

    def remove_item(self, item_name):
        for item in self.cart:
            if item["item"] == item_name:
                self.cart.remove(item)
        print(self.cart)        
        
Juel = Shopping("Juel")

Juel.add_to_cart("Shirt", 2, 100)
Juel.add_to_cart("Juta", 3, 200)
Juel.add_to_cart("Pant", 5, 600)


# total_shopping = Juel.checkOut()
# print(total_shopping)
Juel.remove_item("Shirt")

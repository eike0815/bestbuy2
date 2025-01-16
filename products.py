class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        if name == "":
            raise ValueError("Every product needs valid name")
        self.price = price
        if price <=0:
            raise ValueError("Every product needs price higher than zero")
        self.quantity = quantity
        if quantity < 0:
            raise ValueError("A negative quantity is physically impossible")
        self.active = True

    def __str__(self):
        return self.name, self.price, self.quantity



    def get_quantity(self)-> float:
        return self.quantity


    def set_quantity(self, quantity):
        try:
            self.quantity = quantity
            return quantity
        except ValueError:
            return
        except TypeError:
            print("this product doesn´t exist")

    def is_active(self):
        if self.quantity <=0:
            self.deactivate()
        else:
            self.activate()
        return self.active


    def activate(self):
        self.active = True
        return self.active


    def deactivate(self):
        self.active = False
        return self.active


    def show(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"


    def buy(self, quantity):
        """
        the function buy calculates the total price for the order of one product.
        it monitors the quantity and returns an error-message,
         if the quantity of order is higher than the stock in the shop.
        """
        if quantity > self.quantity:
            print(f"there is not enough {self.name} in stock")
        else:
            total_price = self.price * quantity
            new_quantity = self.quantity - quantity
            self.set_quantity(new_quantity)
            if self.quantity == 0:
                self.deactivate()
            return total_price

class NonStockedProduct(Product):
    def __init__(self, name, price, quantity = 0):
        self.name = name
        if name == "":
            raise ValueError("Every product needs valid name")
        self.price = price
        if price <=0:
            raise ValueError("Every product needs price higher than zero")
        self.quantity = 0
        self.active = True


    def show(self):
        return f"Name: {self.name}, Price: {self.price}"


    def is_active(self):
        return self.active

class LimitedProduct(Product):
        def __init__(self, name, price, quantity, maximum):
            self.name = name
            if name == "":
                raise ValueError("Every product needs valid name")
            self.price = price
            if price <= 0:
                raise ValueError("Every product needs price higher than zero")
            self.quantity = quantity
            if quantity < 0:
                raise ValueError("A negative quantity is physically impossible")
            self.maximum = maximum
            self.active = True

        def show(self):
            return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"

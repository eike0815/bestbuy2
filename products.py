import promotions

class Product:
    def __init__(self, name, price, quantity):
        """
        this function initialises the object belonging to the class,
         as parameter it needs a name, a price and a quantity.
       when an object is created, it is automatically activated
        """
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
        self.promotion = None

    def __str__(self):
        return self.name, self.price, self.quantity


    def get_quantity(self):
        """
        the function returns the quantity of the given object.
        """
        return self.quantity


    def set_quantity(self, quantity):
        """
         the function sets a new quantity to a given object.
         """
        try:
            self.quantity = quantity
            return quantity
        except ValueError:
            return
        except TypeError:
            print("this product doesn´t exist")

    def is_active(self):
        """
        the function checks if an object has  enough quantity to be/stay  activated.
        otherwise it deactivates the object.
        """
        if self.quantity <=0:
            self.deactivate()
        else:
            self.activate()
        return self.active


    def activate(self):
        """
        the function sets the object to active.
        """
        self.active = True
        return self.active


    def deactivate(self):
        """
        this function deactivates the object
        """
        self.active = False
        return self.active


    def show(self):
        """
        the function returns the object name, price and quantity
        """
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
            if self.promotion:
                total_price = self.promotion.apply_promotion(self, quantity)
                print(total_price)
                new_quantity = self.quantity - quantity
                self.set_quantity(new_quantity)
            else:
                total_price = self.price * quantity
                new_quantity = self.quantity - quantity
                self.set_quantity(new_quantity)
                if self.quantity == 0:
                    self.deactivate()
            return total_price

    def set_promotion(self, promotion):
        """
        the function sets a promotion to a given product.
        """
        self.promotion = promotion
        print(promotion)

    def remove_promotion(self):
        """
        the function takes a promotion from a given product away.
        """
        self.promotion  = None


class NonStockedProduct(Product):
    def __init__(self, name, price, quantity = 0):
        """
        this function initialises the object belonging
        to the class of "products without quantity",
        as parameter it needs a name, a price.
       when an object is created, it is automatically activated
        """
        self.name = name
        if name == "":
            raise ValueError("Every product needs valid name")
        self.price = price
        if price <=0:
            raise ValueError("Every product needs price higher than zero")
        self.quantity = 0
        self.active = True
        self.promotion = None


    def show(self):
        """
         the function returns the object name, price and quantity
         """
        return f"Name: {self.name}, Price: {self.price}"


    def is_active(self):
        """this function returns the status active, because the only way to be deactivate is
         by being out of stock"""
        return self.active


    def buy(self, quantity):
        """
        the function buy calculates the total price for the order of one product.
        it monitors the quantity and returns an error-message,
         if the quantity of order is higher than the stock in the shop.
        """
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
          #  print(total_price)
        else:
            total_price = self.price * quantity
        return total_price

    def set_promotion(self, promotion):
        """
        the function sets a promotion to a given product.
        """
        self.promotion = promotion
        print(promotion)

    def remove_promotion(self):
        """
        the function takes a promotion from a given product away.
        """
        self.promotion  = None

class LimitedProduct(Product):
    """
    this function initialises the object belonging to the class,
     as parameter it needs a name, a price and a quantity.
   when an object is created, it is automatically activated
    """
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
        self.promotion = None


    def show(self):
        """
        the function returns the object name, price and quantity
        """
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum: {self.maximum}"


    def is_active(self):
        """
        the function checks if an object's quantity (in the shoppinglist)
        is under the maximum allowed ito be/stay  activated.
        otherwise it deactivates for the process of shopping.
        """
        if self.quantity <= self.maximum:
            self.deactivate()
        else:
            self.activate()
        return self.active


    def activate(self):
        """
        the function sets the object to active.
        """
        self.active = True
        return self.active


    def deactivate(self):
        """
        this function deactivates the object
        """
        self.active = False
        return self.active

    def buy(self, quantity):
        """
        the function buy calculates the total price for the order of one product.
        it monitors the quantity and returns an error-message,
        if the quantity of order is higher than the stock in the shop.
        """
        if quantity >= self.maximum:
            print(f"you can maximal purchase {self.maximum} of {self.name}")
        else:
            if self.promotion:
                total_price = self.promotion.apply_promotion(self, quantity)
                print(total_price)
                new_quantity = self.quantity - quantity
                self.set_quantity(new_quantity)
            else:
                total_price = self.price * quantity
                new_quantity = self.quantity - quantity
                self.set_quantity(new_quantity)
                if self.quantity == 0:
                    self.deactivate()
            return total_price

    def set_promotion(self, promotion):
        """
        the function sets a promotion to a given product.
        """
        self.promotion = promotion
        print(promotion)

    def remove_promotion(self):
        """
        the function takes a promotion from a given product away.
        """
        self.promotion = None

from abc import ABC, abstractmethod



class Promotion(ABC):
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name="Second Item Half Price"):
        super().__init__(name)


    def apply_promotion(selfself, product, quantity):
        discounted_price =  ((quantity // 2) * product.price * 0.5) + ((quantity - (quantity //2))* product.price)
        return discounted_price
"""
    def apply_promotion(product):
        products.product = product
        #product.quantity = quantity
        print("here second half free")
        print()
        help(product)
       # print((product.quantity - (product.quantity // 2)) * products.Product.price + (product.quantity // 2) * products.price / 2)
        print("here second half 3free")
"""

class ThirdOneFree(Promotion):
    def __init__(self, name= "Buy 2, Get 1 Free"):
        super().__init__(name)
        #Buy2, get 1 free


    def apply_promotion(self, product, quantity):
        discounted_price = ((quantity - (quantity //3))*product.price)
        return discounted_price
"""
    def apply_promotion(product, quantity, price):
        product.quantity = quantity
        print("here third free")
        return product.quantity - (product.quantity // 3) * product.price
"""

class PercentDiscount(Promotion):
    def __init__(self ,name= "Percentage Discount", percent = 20):
        super().__init__(name)
        self.percent = percent
        #Percentagediscount(i.e.20 % off)

    def apply_promotion(self, product, quantity):
        discounted_price = product.price * quantity *(1 - self.percent/100)
        return discounted_price
"""
    def apply_promotion(self, product, quantity, percent, price):
        product.quantity = quantity
        self.percent =  percent
        product.price = price
        print("here are percentages")
        return product.price - (product.price * 100* percent/100)
        print("here are percentages")
"""



from abc import ABC, abstractmethod


class Promotion(ABC):
    """
    this function initialises the class of promotions
    """
    def __init__(self, name):
        self.name = name


    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name="Second Item Half Price"):
        """
        this function initialises the class of second product half price.
        it is a child class of the promotion class.
        """
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        """
        this function applies the promotion individually to each given product.
        it returns the reduced total price for the given product with its quantity
        """
        discounted_price =  ((quantity // 2) * product.price * 0.5) + ((quantity - (quantity //2))* product.price)
        return discounted_price


class ThirdOneFree(Promotion):
    def __init__(self, name= "Buy 2, Get 1 Free"):
        """
        this function initialises the class of third product for free.
        it is a child class of the promotion class.
        """
        super().__init__(name)


    def apply_promotion(self, product, quantity):
        """
        this function applies the promotion individually to each given product.
        it returns the reduced total price for the given product with its quantity
        """
        discounted_price = ((quantity - (quantity //3))*product.price)
        return discounted_price


class PercentDiscount(Promotion):
    def __init__(self ,name= "Percentage Discount", percent = 20):
        """
        this function initialises the class of percentage for each product.
        it is a child class of the promotion class.
        it needs to be given a float for percentage.
        """
        super().__init__(name)
        self.percent = percent


    def apply_promotion(self, product, quantity):
        """
        this function applies the promotion individually to each given product.
        it returns the reduced total price for the given product with its quantity
        """
        discounted_price = product.price * quantity *(1 - self.percent/100)
        return discounted_price

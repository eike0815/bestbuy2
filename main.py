import products
import promotions
import store

#products, productlist and shop class are initialised.
pro_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250),
                 products.NonStockedProduct("Windows License", price=125),
                 products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
               ]
best_buy = (store.Store(pro_list))

second_half_price = promotions.SecondHalfPrice("Second Half price!")
third_one_free = promotions.ThirdOneFree("Third One Free!")
thirty_percent = promotions.PercentDiscount("30% off!", percent=10)

pro_list[2].set_promotion(second_half_price)

def menu():
    """
    the function just prints the menu to the ui.
    """
    print("     Store Menu")
    print("     ----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def ordering():
    """
    this function communicates with the store class and handles the order of the user.
    as input there are just numbers, they refer than to products which are added to a shoppinglist
    the function in the class than returns the total price.
    """
    best_buy.get_all_products()
    shopping_list = []
    print("When you want to finish order, enter empty text.")
    while True:
            article = input("which product # do you want? ")
            amount = input("what amount do you want? ")
            if amount == "" and article == "":
                print(shopping_list[0][0].name)
                best_buy.order(shopping_list)
                break
            else:
                article = int(article)
                amount = int(amount)
                try:
                    prod = best_buy.product_list[article-1]
                    product = (prod, amount)
                    shopping_list.append(product)
                    print("Product added to list!")
                except IndexError:
                    print("Error adding product!")



def manual():
    """
    the manual is connected with functions in the Store class.
    the user can choose between 4 options.
    """
    decision_list = [best_buy.get_all_products, best_buy.get_total_quantity, ordering]
    while True:
        menu()
        try:
            user_wish = int(input("Please choose a number: "))
            if user_wish == 4:
                break
            else:
                forefill_user_wish = decision_list[user_wish - 1]
                forefill_user_wish()
        except IndexError:
            print("please enter a valid number between 1 and 4.")


def main():
    manual()


if __name__ == '__main__':
    main()

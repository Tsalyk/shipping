"""
Interface for a user
"""
import orders_creating, order_data

def interface():
    vehicles = list(map(lambda element: order_data.Vehicle(int(element)),
                    input("Enter vehicles separeted by spaces: ").split()))
    choice = input("Would you like to make an order? (y/n): ")
    logSystem = orders_creating.LogisticSystem(vehicles)

    while choice == "y":
        name = input("Enter your name: ")
        city = input("Enter your city: ")
        postoffice = int(input("Enter your postoofice: "))


        choice_2 = ""
        items = []
        while choice_2 != "n":
            item = input("Enter an item and its price (UAH, "
                          "space is separator): ").split()
            items.append(order_data.Item(item[0], int(item[1])))
            choice_2 = input("Anything else? (y/n): ")

        order = orders_creating.Order(name, city, postoffice, items)
        logSystem.placeOrder(order)

        choice = input("Would you like to make another order? (y/n): ")

    choice_3 = input("Would you like to track your order? (y/n): ")
    while choice_3 == "y":
        orderId = int(input("Enter ID of your order: "))
        print(logSystem.trackOrder(orderId))

        choice_3 = input("Would you like to track another order? (y/n): ")

    print("Thank you for your order!")


if __name__ == "__main__":
    interface()
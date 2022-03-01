orders_list=[]
welcoming_msg = """
************************************
**    Welcome to the Snakes Cafe! **  
**   Please see our menu below.   ** 
 To quit at any time, type "quit" 
************************************
"""
print(welcoming_msg)

def menu():
    Appetizers=["Wings","Cookies","Spring Rolls"]
    Entrees=["Salmon","Steak","Meat Tornado","A Literal Garden"]
    Desserts=["Ice Cream","Cake","Pie"]
    Drinks=["Coffee","Tea","Unicorn Tears"]
    menu_list=Appetizers+Entrees+Desserts+Drinks
    print("""
 Appetizers
---------- 
    """)
    for Appetizer in Appetizers:
      print(Appetizer)
    print("""

 Entrees
---------- 
    """)

    for Entree in Entrees:
        print(Entree)
    print("""

 Desserts
---------- 
    """)
    for Dessert in Desserts:
        print(Dessert)

    print("""

 Drinks
---------- 
    """)
    for Drink in Drinks:
        print(Drink)

    print("""

***********************************
** What would you like to order? **
*********************************** """)
    for i in range(1000) :
        order=input("> ")
        if order == "quit":
            print(f"your orders is {orders_list} will be ready in {5*len(orders_list)} minutes")
            quit()
        order_count=0
        orders_list.append(order)
        order_count= orders_list.count(order)



        if order in menu_list:
                print(f" {order_count} order of {order} have been added to your meal ")
        elif order not in menu_list:
            print(f"you added {order_count} of {order} to your meal :)")
        elif order not in menu_list:
            print("")


menu()
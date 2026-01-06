grocery_inventory = {"Milk": ("Dairy", 3.50, 8) ,"Eggs": ("Dairy", 5.50, 30) ,"Bread": ("Bakery", 2.99, 15) ,
                     "Apples": ("Produce", 1.50, 50)}
price_of_Eggs = grocery_inventory["Eggs"][1]
if price_of_Eggs > 5:
    print("Eggs are too expensive, reducing the price by $1.")
else: None
new_price_of_Eggs = price

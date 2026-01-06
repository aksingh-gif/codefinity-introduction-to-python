grocery_inventory = {"Milk": ("Dairy", 3.50, 8) ,"Eggs": ("Dairy", 5.50, 30) ,"Bread": ("Bakery", 2.99, 15) ,
                     "Apples": ("Produce", 1.50, 50)}
price_of_Eggs = grocery_inventory["Eggs"][1]
if grocery_inventory["Eggs"][1] > 5:
    print("Eggs are too expensive, reducing the price by $1.")
else: 
    print("The price of Eggs is reasonable.")
new_price_of_Eggs = ("Dairy", 4.50, 30)
grocery_inventory["Eggs"] = new_price_of_Eggs
grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
print(grocery_inventory.get("Milk")[2])
if grocery_inventory["Milk"][2] < 10:
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")
new_stock_of_milk = ("Dairy", 3.50, 28)
grocery_inventory["Milk"] = new_stock_of_milk
if grocery_inventory["Apples"][1] > 2:
    grocery_inventory.pop("Apples")
else:
    print("Updated inventory:", grocery_inventory)

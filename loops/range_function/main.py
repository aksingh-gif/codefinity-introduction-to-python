# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for promo_items in range(5):
    weekday = weekdays[promo_items]
    promo_topic = daily_promotions[promo_items]
    print(f"{weekday}: Promotion on {promo_topic}")
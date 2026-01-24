prices = [29.99, 45.50, 12.75, 38.20]
for discount in range(len(prices)):
    if discount == 0:
        prices[discount] -= prices[discount] * 0.10
    elif discount == 1:
        prices[discount] -= prices[discount] *0.20
    elif discount == 2:
        prices[discount] -= prices[discount] *0.15
    elif discount == 3:
        prices[discount] -= prices[discount] *0.05
    print(f"Updated price for item {discount}: ${prices[discount]:.2f}")
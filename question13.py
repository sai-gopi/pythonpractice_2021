buying_pure_milk_rate = 3.25

print(f"pure milk cost: {buying_pure_milk_rate}")

pure_milk = int(input("pure milk in liters:"))

buying_price = (buying_pure_milk_rate * pure_milk)

print(f"milk buying price: {buying_price}")

selling_price = 4.15

adding_water_per_liter = 0.25

water_in_milk = (pure_milk * adding_water_per_liter)

total_milk = (pure_milk + water_in_milk)

print(f"total milk with water: {total_milk}")

milk_selling_price = total_milk * selling_price

print(f"milk selling price: {selling_price}")

gain = milk_selling_price - buying_price

print(f"gain of selling milk: {gain}")


#Shopping Bill Program
products = {
    "Pen": 100,
    "Book": 300,
    "Bag": 500,
    "Pencil": 50,
    "Bottle": 200
}

for name, price in products.items():
    print(name, price)

def calculate_total(products):
    return sum(products.values())

total = calculate_total(products)

if total >= 1000:
    discount = total * 10 / 100
else:
    discount = 0

final_bill = total - discount

print("Total Price:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)
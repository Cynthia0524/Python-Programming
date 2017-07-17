import code
import time

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]

##input identifiers
#when you input DONE, it will break
#when you input a integer:
#   if such id exits, recorded.
#   if it is no more than 0, it is a wrong identifier, and will be warned
#   if it is out of the exiting identifiers, it will tell you: no so many products
#when you input "DONE" wrongly, such as "done" and other English letters, it will remind you of inputing "DONE"
ids = []
while True:
    id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    if id == "DONE": break
    elif id[0].capitalize() in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']: print("Did you want to input DONE? Please try again!")
    elif eval(id) > len(products): print("We don't have so many products >_<")
    elif eval(id) <= len(products) and eval(id) > 0: ids.append(int(id))
    elif eval(id) <= 0: print("Wrong identifier! Please try again!")
    else:pass

##print the receipt on computer
print("-------------------------------")
print("BUYME Grocery")
print("-------------------------------")
print("Web: www.buyme.com")
print("Phone: 1.123.456.7890")
from time import strftime
checkout_time = strftime("%Y-%m-%d %H:%M:%S")
receipt_time = checkout_time.replace(" ","-")
receipt_time = receipt_time.replace(":","-") + "-" + str(int(round(time.time() * 1000)))
print("Checkout Time:  " + checkout_time)
print("-------------------------------")
print("Shopping Cart Items: ")
prices = []
for id in ids:
    print(" +",products[id-1]['name'],"($%.2f)" % products[id-1]['price'])
    prices.append(products[id-1]['price'])
print("-------------------------------")
print("Subtotal: $%.2f" % sum(prices))
print("Plus NYC Sales Tax "+"("+"8.875%"+")"+": $%.2f" % float(sum(prices)*0.08875))
print("Total: $%.2f" % float(sum(prices)*1.08875))
print("-------------------------------")
print("Thank you for your business! Welcome to BUYME again!")
#professor's hint
#product_ids = []

#while True:
#    product_id = input("Please input a valid product identifier:")
#    if product_id == "DONE":
#        print("THANKS ALL DONE HERE")
#        break
#    else:
#        print("THE PRODUCT IDENTIFIER IS: " + str(product_id))
#        product_ids.append(product_id)

#print("OUTSIDE THE LOOP")
#print(product_ids)


##output the receipt to a text for printing purpose
#remember to change the file path!!!
file_name = "/Users/cynthia/Desktop/Github/python-practice/shopping_cart_receipts/"+receipt_time+".txt"
receipt = open(file_name,"w")
receipt.write("-------------------------------\n")
receipt.write("BUYME Grocery\n")
receipt.write("-------------------------------\n")
receipt.write("Web: www.buyme.com\n")
receipt.write("Phone: 1.123.456.7890\n")
receipt.write("Checkout Time:  " + checkout_time + "\n")
receipt.write("-------------------------------\n")
receipt.write("Shopping Cart Items: \n")

for id in ids:
    shopping = " + "+products[id-1]['name']+" ($%.2f) \n" % products[id-1]['price']
    receipt.write(shopping)

receipt.write("-------------------------------\n")
receipt.write("Subtotal: $%.2f \n" % sum(prices))
tax = "Plus NYC Sales Tax "+"("+"8.875%"+")"+": $%.2f \n" % float(sum(prices)*0.08875)
receipt.write(tax)
receipt.write("Total: $%.2f \n" % float(sum(prices)*1.08875))
receipt.write("-------------------------------\n")
receipt.write("Thank you for your business! Welcome to BUYME again!\n")
receipt.close()

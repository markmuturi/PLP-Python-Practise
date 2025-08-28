# The function calculates the final price after applying a discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        finalPrice = price * (discount_percent/100)
        return finalPrice
    else:
        return price
    
price = int(input("Enter the Original Price here: "))
discount_percent = int(input("Enter the Discount Percentage here: "))
final_price = calculate_discount(price, discount_percent)
print(final_price)
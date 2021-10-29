money = int(input("Enter your money: "))
apple_price = int(input("Enter apple price: "))

qty = money / apple_price
convert_qty = int(qty)

apple = apple_price * convert_qty
convert_apple = int(apple)

change = money - convert_apple

print("You can buy ", convert_qty , " apples and your change is ", change ,"pesos .")

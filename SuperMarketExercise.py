def supermarket():
    products = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
    total_sum = 0

    print("Supermarket")
    print("===========")

    while True:
        product_number = int(input("Please select product (1-10) 0 to Quit: "))

        if product_number == 0:
            break
        elif 1 <= product_number <= 10:
            price = products[product_number - 1]
            total_sum += price
            print(f"Product: {product_number} Price: {price}")
        else:
            print("Invalid product number. Please select a number between 1 and 10.")

    print(f"Total: {total_sum}")

    payment = int(input("Payment: "))
    change = payment - total_sum
    print(f"Change: {change}")


supermarket()

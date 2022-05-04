import math


if __name__ == '__main__':

    total = 0
    sandwich_total = 0
    fries_total = 0
    soda_total = 0
    sandwich_price = 10
    fries_price = 5
    soda_price = 2
    sandwich_discount_price = 8
    fries_discount_price = 3
    soda_discount_price = 1
    final_sand_amount = 0
    final_fry_amt = 0
    final_soda_amt = 0
    print("Welcome to the food kiosk!!")
    print("If you order more then 10 sandwiches, each will cost $8 \n"
          "If you order more then 7 fries, each will cost $3 \n"
          "If you order more then 5 sodas, each will cost $1")

    ans = True
    while ans:
        print("""
        Please select from the following:
        1.Sandwich
        2.Fries
        3.Soda
        4.Exit/Quit
            """)
        entry = input("Enter your selection(Number value): ")
        if entry == "1":
            sand_amount = int(input("Enter the amount of sandwiches you want: "))
            total += (sand_amount * sandwich_price)
            final_sand_amount += sand_amount
            print("The subtotal is $" + format(total, '.2f'))

        elif entry == "2":
            fry_amount = int(input("Enter the amount of sandwiches you want: "))
            total += (fry_amount * fries_price)
            final_fry_amt += fry_amount
            print("The subtotal is $" + format(total, '.2f'))

        elif entry == "3":
            soda_amount = int(input("Enter the amount of soda you want: "))
            total += (soda_amount * soda_price)
            final_soda_amt += soda_amount
            print("The subtotal is $" + format(total, '.2f'))

        elif entry == "4":
            if final_sand_amount > 10:
                total -= ((final_sand_amount * sandwich_price) - (final_sand_amount * sandwich_discount_price))
            if final_fry_amt > 7:
                total -= ((final_fry_amt * fries_price) - (final_fry_amt * fries_discount_price))
            if final_soda_amt > 5:
                total -= ((final_soda_amt * soda_price) - (final_soda_amt * soda_discount_price))
            print("The final total is $" + format(total, '.2f') + "\nThank you and have a great day")

            ans = None
        else:
            print("Enter a valid entry!")






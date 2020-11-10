# return statements used with functions



def tillSlip(price):
   
    price = float(input('what is the sales price: '))
    tax = 1.25
    tax_amount = price * tax
    total_price = tax_amount + price
    return price, tax_amount, total_price

    print(f'''
            Price = {price}
            Tax   = {tax_amount}
        ---------------------
            Total =  {total_price}
        ---------------------- ''')

    return tillSlip()



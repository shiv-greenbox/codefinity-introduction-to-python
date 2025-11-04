def apply_discount(price,discount=0.05):
    disc_price = price * (1-discount)
    return disc_price

def apply_tax(price, tax = 0.07):
    price_afr_tax = price * (1 + tax)
    return price_afr_tax

def calculate_total(price, discount = 0.05, tax = 0.07):
    total_price_afr_disc = apply_discount(price, discount)
    total_price_afr_disc_tax = apply_tax(total_price_afr_disc,tax)
    return total_price_afr_disc_tax

total_price_default = calculate_total(120)
print(f"Total cost with default discount and tax : ${total_price_default}")

total_price_custom = calculate_total(100, discount = 0.10, tax = 0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")







    
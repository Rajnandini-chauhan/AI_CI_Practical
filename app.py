def calculate_total(price, quantity):
return price * quantity

def calculate_discount(total, discount):
return total - (total * discount / 100)
if __name__ == &quot;__main__&quot;:
total = calculate_total(100, 2)
final_amount = calculate_discount(total, 10)
print(&quot;Total Amount:&quot;, total)
print(&quot;Final Amount:&quot;, final_amount)
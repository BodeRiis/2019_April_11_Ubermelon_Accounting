def customer_pay(customer, melons, did_pay):
  melon_cost = 1.00
  count = 0
  customer_expected = melons * melon_cost
  if customer_expected != did_pay:
      count += 1
      print(f"{customer} paid ${did_pay:.2f},",
            f"expected ${customer_expected:.2f}"
            )


the_file = open("customer-orders.txt")
for line in the_file:
    line = line.rstrip()
    words = line.split('|')

    customer = words[1]
    melons = words[2]
    amount = words[3]

    final_count = str(customer_pay(customer, float(melons), float(amount)))

print(final_count + " customers have not paid the corrent amount.")
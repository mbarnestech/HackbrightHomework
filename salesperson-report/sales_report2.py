"""Generate sales report showing total melons each salesperson sold."""

# create empty dictionary
sales = {}

# open the sales report file
with open('sales-report.txt') as report:

    # iterate over each line in sales report
    for line in report:

        # assign each item in line an appropriate variable
        salesperson, order_amount, melons_sold = line.rstrip().split('|')
        
        # turn numbers info floats/ints from strings
        order_amount = float(order_amount)
        melons_sold = int(melons_sold)

        # check if salesperson is in dictionary; if not set up a nested dictionary for order amount and melons sold 
        sales[salesperson] = sales.get(salesperson, {'order amount': 0.00, 'melons sold': 0})
        
        # update nested dictionary with order amount and melons sold
        sales[salesperson]['order amount'] += order_amount 
        sales[salesperson]['melons sold'] += melons_sold


    # iterate over sales key:value pairs
    for salesperson, stats in sales.items():

        # print statement for how many melons each salesperson sold and total order amount
        print(f"{salesperson} sold {stats['melons sold']} melons for ${stats['order amount']:.2f}")
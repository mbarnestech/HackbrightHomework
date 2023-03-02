#create function to run report
def run_report(melon_cost, file_name):
    """ create report on underpaid customers given a price and an order file. """

    # open file
    with open(file_name) as file:

        # iterate over each line in file
        for line in file:

            # remove trailing spaces
            line = line.rstrip()

            # create list of items by splitting line at each '|'
            order_info = line.split('|')

            # assign each item a variable name
            order_num =  int(order_info[0])
            customer = order_info[1]
            melons = int(order_info[2])
            price_paid = float(order_info[3])

            # expected cost is the number of melons times the cost per melon
            expected = melons * melon_cost
            
            # if expected is different than the price paid 
            if expected != price_paid:

                # print a line explaining the situation
                print(f"Order {order_num}: {customer} paid ${price_paid:.2f}. Expected ${expected:.2f}")
    
    # this function returns 'None'
    return
                      
                      
# run the report for a melon cost of $1.00 on the customer orders file
run_report(1, 'customer-orders.txt')
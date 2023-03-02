def run_report(melon_cost, file_name):
    with open(file_name) as file:
        for line in file:
            line = line.rstrip()
            order_info = line.split('|')
            order_num =  int(order_info[0])
            customer = order_info[1]
            melons = int(order_info[2])
            price_paid = float(order_info[3])
            expected = melons * melon_cost
            if expected != price_paid:
                print(f"Order {order_num}: {customer} paid ${price_paid:.2f}. Expected ${expected:.2f}")
    return 'done'
                      
run_report(1, 'customer-orders.txt')
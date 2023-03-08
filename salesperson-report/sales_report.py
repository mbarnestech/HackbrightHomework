"""Generate sales report showing total melons each salesperson sold."""

# create empty global lists for salespeople and number of melons sold
salespeople = []
melons_sold = []

# open the sales report file
f = open('sales-report.txt')

# iterate over each line in sales report
for line in f:
    # remove space from end of line
    line = line.rstrip()
    # create 'entries' list by splitting line at '|'
    entries = line.split('|')
    # create salesperson variable for first item in entries list
    salesperson = entries[0]
    # create melons variable for third item in entries list, converted from string to int
    melons = int(entries[2])

    # check if the salesperson is in the salespeople list
    if salesperson in salespeople:
        # if yes, get the index number of that person in the salespeople list and store it in 'position'
        position = salespeople.index(salesperson)
        # use index number found in previous line to get index number of melons sold, add number of melons from this line
        melons_sold[position] += melons
    
    # if salesperson is not in the salespeople list
    else:
        # add salesperson to the salespeople list
        salespeople.append(salesperson)
        # add number of melons sold to the melons list; this should be at the same index
        melons_sold.append(melons)

# iterate over salespeople index
for i in range(len(salespeople)):
    # print statement for how many melons each salesperson sold
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
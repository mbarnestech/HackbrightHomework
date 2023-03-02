# use for loop to loop over 3 days
for days in range(1,4):
    # print day number
    print(f"Day {days}")
    # open corresponding file for a limited time
    with open(f"um-deliveries-day-{days}.txt") as the_file:
        # loop over lines in the file
        for line in the_file:
            # remove trailing spaces
            line = line.rstrip()
            # create list split by '|'
            words = line.split('|')

            # assign first list item to 'melon'
            melon = words[0]
            # assign second list item to 'count'
            count = words[1]
            # assign third list item to 'amount'
            amount = words[2]

            # print delivery information
            print(f"Delivered {count} {melon}s for total of ${amount}")

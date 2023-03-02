# same as produce_summary.py but using a function instead of a for loop

# define function
def generate_produce_report(day):
    """ print report based off .txt file for a given day """

    # print day number
    print(f"Day {day}")
    # open corresponding file for a limited time
    with open(f"um-deliveries-day-{day}.txt") as the_file:
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

# generate produce reports for days 1, 2, and 3
generate_produce_report(1)
generate_produce_report(2)
generate_produce_report(3)
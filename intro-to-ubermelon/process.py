# put data from um-server-01.txt file into log_file variable
log_file = open("um-server-01.txt")

# create a function to generate a sales report for a given log file
def generate_sales_reports(log_file):
    # review every line in the data
    for line in log_file:
        # remove any trailing characters from the line
        line = line.rstrip()
        # define variable 'day' as the first through third characters in a line
        day = line[0:3]
        # print line IF day is the abbreviated form of Tuesday
        # if day == "Tue":
        # print line IF day is the abbreviated form of Monday
        if day == "Mon":
            print(line)

# run the function defined above on the data stored in log_file
generate_sales_reports(log_file)

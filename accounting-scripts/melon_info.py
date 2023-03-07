from melons import melon_dict 


def print_melon(data = melon_dict):
    """Print each melon with corresponding attribute information."""
    
    # go through each melon and corresponding dict
    for name, melon_info  in data.items():
        
        # print the name of the melon in all caps
        print(name.upper())

        # go through each data category / value in dict for melon
        for attribute, value in melon_info.items():

            # print the key: value pair, indented
            print(f'\t{attribute}: {value}')

# run function to print melons in default melon_dict
print_melon()

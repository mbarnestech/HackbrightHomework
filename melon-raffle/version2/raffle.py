"""Randomly pick customer and print customer info"""

from random import choice

import customers

def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = choice(customers)

    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")

def run_raffle():

    customer_list = customers.get_customers_from_file('customers.txt')
    pick_winner(customer_list)

if __name__ == '__main__':
    run_raffle()
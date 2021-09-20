#!/usr/bin/env python3

# Created by: Igor
# Created on: Sept 2021
# This is pizza cost program

import constans


def main():
    # input
    radius = int(input("Enter a radius of pizza: "))

    # process
    cost = constans.labor + constans.rent + radius * constans.materials
    tax = cost * 0.15
    total_cost = cost + tax

    # output
    print("The cost of pizza (without tax) is: ${0:,.2f}".format(cost))
    print("The tax is: ${0:,.2f}".format(tax))
    print("Total cost of pizza is: ${0:,.2f}".format(total_cost))


if __name__ == "__main__":
    main()

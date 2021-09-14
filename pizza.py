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
    # output
    print("The cost of pizza is: {}".format(cost))


if __name__ == "__main__":
    main()

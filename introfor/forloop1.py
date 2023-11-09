#!/usr/bin/env python3
"""RZFeeser | Alta3 Research
   learning about for logic"""
import time

# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
# loop across the list vendors
for x in vendors:
    print("The vendor is:" + x)  # each time through the loop print value of x
    time.sleep(1)
print("\nOur loop has ended.")  # when the loop ends print this


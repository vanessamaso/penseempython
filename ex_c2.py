#!/usr/env/python3

from math import pi
import datetime

# Ex 2.2.1
# vol = 4/3 * pi * r ** 3
r = 5
vol = 4/3 * pi * r ** 3
print('volume: ' +  str(vol))

# Ex 2.2.2
cover_price = 24.95
discount = 0.4
store_price =  cover_price * (1 - discount)
shipping_first = 3.00
shipping_addicional = 0.75
number_exemplars = 60

total_cost = store_price + (number_exemplars - 1) * shipping_addicional + shipping_first

print('total cost: ' +  str(total_cost))


# Ex 2.2.3
# t0 = 6:52am 
# t1 = t0 + 8m15s
# t2 = t1 + 3 * 7m12s
# t3 = t2 + 8m15s
# t3 = xx:xx h?

t0 = 60 * 60 * 6 + 52 * 60
t1 = t0 + 8 * 60 + 15
t2 = t1 + 3 * (7  * 60 + 12)
t3 = t2 + (8 * 60 + 15) # seconds since 00:00h

print('hour: ' + str(datetime.timedelta(seconds=t3)))
prices = {"apple": 1, "orange": 2, "pear": 3}
stock = {"apple": 2, "orange": 4, "pear": 5}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
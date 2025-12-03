prices1 = {'apple': 200, 'banana': 150}
prices2 = {'orange': 180, 'banana': 130}
prices3 = dict()

for key in prices1.keys():
    if key in prices2:
        prices3[key] = int((prices1[key] + prices2[key]) / 2)
    else:
        prices3[key] = prices1[key]

for key in prices2.keys():
    if key in prices1:
        prices3[key] = int((prices1[key] + prices2[key]) / 2)
    else:
        prices3[key] = prices2[key]
print(prices3)

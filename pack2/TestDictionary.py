import Dictionary as d

dic = d.Dictionary()
print ("dic", dic)
dic["key"] = "value"
dic["key2"] = "value2"
print ("dic", dic)
dic2 = d.Dictionary(dic)
print ("dic2", dic2)
dic["key3"] = "value3"
del(dic["key"])
dic2["key4"] = "value4"
print ("dic", dic)
print ("dic2", dic2)
dic3 = d.Dictionary(key5="value5", key6="value6")
print ("dic3", dic3)
dic4 = d.Dictionary(dic3, key7="value7")
print ("dic4", dic4)
dic4["key6"] = "value6bis"
print ("dic4", dic4)
dic4["key1"] = "value1"
dic4["key2"] = "value2"
dic4.sort()
print ("dic4", dic4)
dic4["key3"] = "value3"
dic4["key4"] = "value4"
dic5 = dic4.sorted(reverse=True)
print ("dic4", dic4)
print ("dic5", dic5)
dic5.reverse()
print ("dic5", dic5)
print (" --------- ITER --------- ")
for key in dic5:
    print(key + " - " + dic5.get(key))
print (" --------- KEYS --------- ")
for key in dic5.getKeys():
    print(key + " - " + dic5.get(key))
print (" --------- VALUES --------- ")
for values in dic5.values():
    print(values)
print (" --------- ITEMS --------- ")
for item in dic5.items():
    print (item[0] + " - " + item[1])
    
dic6 = dic2 + dic3
print ("dic6", dic6)



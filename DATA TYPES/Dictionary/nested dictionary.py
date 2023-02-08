#NESTED DICTIONARY

dict1={"child1":{"name":"emi","year":12},"child2":{"name":"keyan","year":2}}
print(dict1)
# print(dict1.keys())
# print(dict1.values())
# print(dict1.items())
 #change value
# dict1["name"]="sanvika" ##DOUBT HOW TO CHNGE EMI TO SANVIKA?
# print(dict1)
#multiple items update
# dict1.update({"child3":{"name":"chinnu","year":8}})
# print(dict1)

 #add new keyword
# dict1.update({"child3":{"height":"tall","size":"medium"}})
# print(dict1)

 #remove
# dict1.pop("child2")
# print(dict1)

#remove last item
dict1.popitem()
print(dict1)

# # #remove using del
# # del dict1["year"]
# # print(dict1)

# dict2=dict1.copy()
# print(dict2)

# #remove all items
# #dict2.clear()
# #print(dict2)
# del dict2
# print(dict2)
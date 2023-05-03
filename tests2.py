names = ["justice", "julius", "gideon", "habiba", "jane"]
surnames = ["james", "john", "peter", "usman", "livingstone"]

# def converter(names1, names2, **dic):
# 	for name1 in names1:
# 		for name2 in names2:
# 			dic[name1] = names2


# 		# val1 = names1.pop() 
# 		# val2 = names2.pop() 

# 		# dic[val1] = val2

# 		# for name1 in names1:
# 		# 	for name2 in names2:
# 		# 		[name1] = name2


# print(converter(names, surnames))


def converter(names1, names2, **dic):
	dic = {}
	while names1:  
		val1 = names1.pop() 
		val2 = names2.pop() 

		dic[val1] = val2
	return dic    

		# for name1 in names1:
		# 	for name2 in names2:
		# 		[name1] = name2


p = converter(names, surnames)
print(p)
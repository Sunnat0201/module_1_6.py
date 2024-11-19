my_dict = {'Family' : 'mother', 'year of birth': 1985}
print (my_dict)
print (my_dict ['Family'])
my_dict['Street'] = 'friend'
print (my_dict)
my_dict['School'] = 'classmates'
my_dict['Market'] = 'cashier'
print (my_dict)
del my_dict ['Market']
print (my_dict)
my_set = {"apple", "orange", 10, 20, 10, "banana", "apple"}
print(set(my_set))
my_set.update(["carrot", "mango"])
my_set.remove("apple")
print(set(my_set))
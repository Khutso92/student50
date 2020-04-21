
#types of collections
name_list = ["Khutso","Rori","Ditheto"] # list
name_variable = "Khutso"
name_tuple = ("Khutso","Matlala")

di_set = set() # wont repeat duplicates in a set
di_set.add(1)
di_set.add(4)
di_set.add(1)
di_set.add(3)

mapping = {"Khutso":27,"Pono":30,"Dad":65} # dictionaries/mapping

mapping["Khutso"] += 1 # increment

mapping["Ben"] = 26

print(mapping)

exit()

for name in name_tuple:
    print(name)

my_list =[] # Create an empty list called my_list
my_list.append(10) # Append 10 to my_list
my_list.append(20) # Append 20 to my_list
my_list.append(30) # Append 30 to my_list
my_list.append(40) # Append 40 to my_list

my_list.insert(1,15) # Insert 15 at the second position in the list
another_list =[50,60,70] #create another_list
my_list.extend(another_list) # Extend my_list to another_list
my_list.pop() # remove the last element from my_list
my_list.sort() # sort my_list in ascending order

index_of_30 = my_list.index(30) # Find the index of the value 30 in my_list
print(f"The index of 30 in my_list is: {index_of_30}")
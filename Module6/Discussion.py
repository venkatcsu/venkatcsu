print("**************List**********")
multilist = [5, 3, 4, 1,"orange", "banana","apple","apple"]
print("Initial List:",multilist)
#pop() deletes last element
multilist.pop()
print("List after pop:",multilist)
#append() add at last element
multilist.append("apple")
print("List after append:",multilist)
#remove() will delete the value in the list
multilist.remove(1)
print("List after remove:",multilist)
#insert() will delete the element in the index 
multilist.insert(3, 1)  
print("List after insert @index 3:",multilist)
#sort() will sort the list with same data type
multilist = [5, 3, 4, 1]
multilist.sort()  
print("List after sort:",multilist)
print("**************Dictionary**********")
# Creating a dictionary with initial elements
dict = {
    "name": "John",
    "age": 30,
    "city": "Philadelphia"
}
print("Initial dictionary:",dict)
#add new key-value pair 
dict["email"] = "john@eabcxample.com"
print("After adding email in dictinary:",dict)
#updating  new key-value pair 
dict["name"] = "Venkat"
dict["email"] = "venkat@eabcxample.com"
print("After updating name and email in dictinary:",dict)
# Deleting a key-value pair using pop() and capturing the removed value removed_value = dict.pop("email")
removed_value = dict.pop("email")
print("After removing " ,removed_value,  " in dictinary:",dict)

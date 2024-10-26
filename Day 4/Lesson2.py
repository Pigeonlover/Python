# Syntax :
# list_name = ["item1", "item2", "item3"]

# To print first item, it's at index 0 :
# print(list_name[0]) --> item1

# To print items backwards from the end of the list, use negative index positions :
# print(list_name[-1]) --> item3

# Add new item at the end :
# list_name.append("item4")

# Add more than one new item :
# list_name.extend("item5", "item6", "item7")

# A list can contain more lists :
items = ["strawberries", "apples", "potatoes", "kale"]

fruits = ["strawberries", "apples"]
vegetables = ["potatoes", "kale"]

items = [fruits, vegetables]

print(items)  # --> [['strawberries', 'apples'], ['potatoes', 'kale']]

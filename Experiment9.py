fruitlist = ["apples", "oranges", "bananas", "pear", "watermelon"]
fruitlistcopy = fruitlist.copy()
fruitlist.append("kiwi")
print(f"Default fruit list: {fruitlist}")
print(f"Copy fruit list: {fruitlistcopy}")
print(f"Length of the list is: {len(fruitlist)}")
boolval = "pear" in fruitlist
print(f"Is pear in the fruitlist?: {boolval}")
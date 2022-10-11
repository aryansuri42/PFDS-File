dictcars ={
    "Ford": "1990 Fastback",
    "Toyota": "1994 Trueno AE86"
}
print(f"length of the dictionary is : {len(dictcars)}")
dictcars.update({"Honda": "1997 NSX"})
print(f"Dictionary after adding an element: {dictcars}")
dictcars.pop("Ford")
print(f"Dictionary after removing an element: {dictcars}")

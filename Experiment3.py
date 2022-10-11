string = input("Enter a String: ")
string += " "
temp = ""
list1 = []
for i in string:
    if i != " ":
        temp += i
    elif i == " ":
        list1.append(temp)
        temp = ""
for j in range(0, len(list1)):
    if j == 5:
        break
    else:
        for k in list1[j]:
            print(k)

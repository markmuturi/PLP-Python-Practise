my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.insert(1, 15)
newList = [50, 60, 70]
my_list.extend(newList)
my_list.pop(7)

my_list.sort()

thirtyIndex = my_list.index(30)
print(thirtyIndex)
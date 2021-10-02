massive =[]
massive.append("a")
massive.append("v")
massive.append("b")
massive.append("n")
massive.append("m")
massive.append("z")
print(massive)
del massive[1]
print(massive)
massive.insert(1,"den")
print(massive)
del massive[1]
print(massive)
massive.insert(1,"Sasah")
print(massive)
del massive[3]
print(massive)
del_item= massive.pop()
print(massive)
print(del_item)


print("Hello Mister!")
cars = ["suzuki", "ferrari","porshe","mersedes"]
print(cars)
den = f"Я хочу посмотеть такую машину {cars[2].title()}"
print(den)
del_corzina = cars.pop(2)
print(cars)
print(del_corzina)

mashin = ["suzuki", "ferrari","porshe","mersedes"]
mashin.sort()
print(mashin)
mashin.sort(reverse=True)
print(mashin)
a= len(mashin)
print(a)

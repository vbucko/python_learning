name = "abc"
print(name[0])
print(name[1])
print(name[2])

name = "Veronika"

for char in name:
    print(char)
    print(char) 
print(char)

counter = 0
for letter in name:
    counter += 1
    
print(counter)

name2 = "aba  babccc"
a_counter = 0
b_counter = 0
other_counter = 0

for char in name2:
    if char == "a":
        a_counter +=1
    elif char == "b":
        b_counter +=1
    else:
        other_counter +=1


print(a_counter)
print(b_counter)
print(other_counter)

name = "Veronika"
position = 0

for char in name:
    if char == "n":
        print(position)
    position+=1




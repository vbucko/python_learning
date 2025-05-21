name = "Michalc"

counter = 0
for c in name:
    if c == "c":
        print(counter)
        break
    counter += 1

print("End!")




counter2 = 0

while counter2 < len(name):
    if name[counter2] == "c":
        print(counter2)
        break
    counter2+=1


counter=0
while True:
    print(counter)
    if counter == 100:
        break
    counter+=1

counter=0
while True:
    if counter %2 == 1:
        counter+=1
        continue
    print(counter)
    if counter == 100:
        break
    counter +=1

name = "Michal"
for c in name:
    if c == "c":
        continue
    print(c)

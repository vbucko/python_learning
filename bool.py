is_smaller = 4!=5.5
print(is_smaller)

veronika_age = 30
brother_age = 28
friends_age = 30

is_veronika_older = veronika_age > brother_age
print(is_veronika_older)

#logic operations
is_veronika_oldest = veronika_age > brother_age and veronika_age > friends_age
print(is_veronika_oldest)

is_veronika_oldest = veronika_age > brother_age or veronika_age > friends_age
print(is_veronika_oldest)

is_veronika_cool = True
x = not(is_veronika_cool)

print(x)

# Priklady na doma aka je vysledna pravdivostna hodnota tychto vyrazov 
z = not(3 < 5) and 4 < 5
y = 4 > 3 and 5 < 4
x = 14 
a = not(x < -x) and 14 > 11 or 1 < 2

print(z)
print(y)
print(x)
print(a)

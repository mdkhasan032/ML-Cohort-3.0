#task 2
x = float(input("Enter the value of x = "))
y = float(input("Enter the value of y = "))
z = float(input("Enter the value of z = "))
if x>y and x>z:
    print("x is the largest number")
elif y>x and y>z:
    print("y is the largest number")
else:
    print("z is the largest number")


#Task 3
CGPA_of_zisan = float(input("Enter zisan's CGPA: "))
zisan = round(CGPA_of_zisan,2)
CGPA_of_shakil = float(input("Enter shakil's CGPA: "))
shakil = round(CGPA_of_shakil,2)
CGPA_of_ifty = float(input("Enter ifty's CGPA: "))  
ifty = round(CGPA_of_ifty)

if zisan<shakil and zisan<ifty:
    print("CGPA of zisan is the lowest")
elif shakil<zisan and shakil<ifty:
    print("CGPA of shakil is the lowest")
else:
    print("CGPA of ifty is the lowest")

avg = (zisan+shakil+ifty)/3
value = round(avg,2)
print("average CGPA is", value)

#Task 1
list = [10,20,30,40,50]
list.append(60)
list.remove(20)
sum = sum(list)
print(list)
print(sum)


#task 2
tuple_1 = ("Dhaka", "Khulna", "Comilla", "Chandpur", "Sylhet")
print(tuple_1[2])
newlist = list(tuple_1)
newlist.append("Noakhali")
tuple_2 = tuple(newlist)
print(tuple_2)



#task 3
HSC_marks = {
         "Math" : 90,
         "Science" : 85,
        "English" : 80
}
HSC_marks['Bangla'] = 86
HSC_marks['Math'] = 95
print("Dictionary =",HSC_marks)
average = sum(HSC_marks.values())/len(HSC_marks)
print("Average = ", average)


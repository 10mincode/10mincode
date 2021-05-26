list=[]
noofnum=int(input("Enter the number of numbers you want to compare: "))
for i in range(noofnum):
    ui=input(f"Enter the {i+1} number")
    list.append(ui)
max=list[0]
for i in range(len(list)):
    if list[i] >max:
        max=list[i]
print(f"The maximum number is {max}")
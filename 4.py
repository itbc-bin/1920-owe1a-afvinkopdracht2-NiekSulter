print("Please enter the values of the selected items")

i1 = float(input())
i2 = float(input())
i3 = float(input())
i4 = float(input())
i5 = float(input())

TotalBT = i1 + i2 + i3 + i4 + i5
print("Total before taxes:", TotalBT)

TotalAT = TotalBT * 1.07
TO = TotalAT - TotalBT

print("Sales tax:", TO)
print("Total with tax:", TotalAT)



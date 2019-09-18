#Base value 48
#1.5 sugar
#1 butter
#2.75 flour

ac = float(input("What's the amount of cookies that you want to bake? "))

bsuiker = 1.5/48
bboter = 1 /48
bflour = 2.75/48

fsuiker = bsuiker * ac
fboter = bboter * ac
fflour = bflour * ac

print("You will need", fsuiker, "cup(s) of sugar")
print("You will need", fboter, "cup(s) of butter")
print("You will need", fflour, "cup(s) of flour")

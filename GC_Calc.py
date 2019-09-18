#Open the sequence file.
f = open("test.txt", "r")

#Reads the contents of the file from left to right into a variable.
seq = f.read()


#Total length of the sequence.
T = (len(seq))

#Counts the number of Gs and Cs and puts them in respecting variables.
G = seq.count("G")
C = seq.count("C")
A = seq.count("A")
TT = seq.count("T")

#GC% calculation: (G + C)/(total number of characters)

Total = ((G + C) / T) * 100
TotalAT = ((A + TT) / T) * 100

print("Sequence has a GC% of:", (Total.__round__(2)))
print("Sequence has a AT% of:", (TotalAT.__round__(2)))
print("Total %:", Total + TotalAT)


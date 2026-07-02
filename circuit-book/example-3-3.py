I0 = 2
R1 = 2
R3 = 10
V2 = 2
R4 = 4
I5 = 7


G1 = 1/R1
G3 = 1/R3
G4 = 1/R4


N1 = (I5 - I0 + G4*V2)/(-G1-G4)
N2 = N1 + V2

print(N1)
print(N2)

print(N1/R1)

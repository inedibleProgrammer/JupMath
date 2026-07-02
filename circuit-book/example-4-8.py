V0 = 32
R1 = 4
R2 = 12
R4 = 1
I3 = 2

N1 = V0
G1 = 1/R1
G2 = 1/R2
G4 = 1/R4

def first_attempt():
    N2 = (-I3 - G1*N1)/(-G1-G2)

    V_TH = N2
    print(N2)

    R_TH = R4 + (1/R1 + 1/R2)**-1
    print(R_TH)

    R_L1 = 6
    R_L2 = 16
    R_L3 = 36

    G_L1 = 1/R_L1
    G_L2 = 1/R_L2
    G_L3 = 1/R_L3

    G_TH = 1/R_TH


    N3_1 = -G_TH*V_TH / (-G_TH - G_L1)
    N3_2 = -G_TH*V_TH / (-G_TH - G_L2)
    N3_3 = -G_TH*V_TH / (-G_TH - G_L3)

    I_L1 = N3_1 / R_L1
    I_L2 = N3_2 / R_L2
    I_L3 = N3_3 / R_L3

    print(I_L1)
    print(I_L2)
    print(I_L3)

def second_attempt():
    N2 = (-I3 - G1*N1)/(-G1 - G2 - G4)
    print(N2)
    I_N = N2/R4
    print(I_N)

    R_TH = R4 + (1/R1 + 1/R2)**-1
    print(R_TH)

    V_TH = R_TH * I_N
    print(V_TH)

second_attempt()


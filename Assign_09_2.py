import numpy as np

# Problem 2: Unit Operations

# Yield of Biomass and Product from Glucose (B / S, P / S)
YB_S = 0.48 * (180) / (24.97) # g/g -> mol/mol
YP_S = 0.2 * 0.48 * (180) / (22.01)
print(YB_S, YP_S)
# YP_S = 0.2 * YB_S

# NH3 as N source
NH3 = np.array([0,  # Carbon (mol C/mol NH3)
                3,  # Hydrogen  (mol H/mol NH3)
                0,  # Oxygen
                1,  # Nitrogen
                0,  # g protein / g Glucose
                0])  # g biomass / g Glucose

# Product = protein:
Protein = np.array([1,
                   1.55,
                   0.31,
                   0.25,
                   1,
                   0])


# Biomass = E. coli
Biomass = np.array([1,
                    1.77,
                    0.49,
                    0.24,
                    0,
                    1])

# Carbon Source = Glucose
Glucose = np.array([6,
                    12,
                    6,
                    0,
                    YP_S,
                    YB_S])

Oxygen = np.array([0,
                   0,
                   2,
                   0,
                   0,
                   0])

CO2 = np.array([1,
                0,
                2,
                0,
                0,
                0])

H2O = np.array([0,
                2,
                1,
                0,
                0,
                0])

# Find Oxygen demand and NH3 requirement
# Equation:
# Glucose (S) + O2 (O) + NH3 (N) -> Biomass (B) + Product (P) + CO2 + H2O
# Rearrange: O + N - B - P - CO2 - H2O = S
#    [-H20, O, N, -B, -P, -CO2] [x] = [-S]
A = np.array([Oxygen, NH3, Protein, Biomass, CO2, H2O]).transpose()
print(A)
B = Glucose

X = np.linalg.solve(A, B)
print(X)

# # matrices might be wrong
# print('NH3: ', X[2][0] * 17/180)
# print('O2: ', X[1][0] * 32/180)

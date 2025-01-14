import numpy as np

# Матрица преобразования φ в базисе (a1, a2)
A = np.array([[0, 1],
              [1, -1]])

# Матрица перехода от базиса (a1, a2) к базису (b1, b2)
P = np.array([[2, -1],
              [-1, 1]])

# Вычисляем обратную матрицу P
P_inv = np.linalg.inv(P)

# Вычисляем матрицу преобразования φ в базисе (b1, b2)
B = P_inv.dot(A).dot(P)

# Вычисляем матрицу преобразования φoφ в базисе (b1, b2)
B_squared = B.dot(B)

print("Матрица преобразования φ в базисе (b1, b2):")
print(B)

print("Матрица преобразования φoφ в базисе (b1, b2):")
print(B_squared)

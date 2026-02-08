import numpy as np

# Input Matrices
A = np.array([[5,6],
              [7,8]])

B = np.array([[1,2],
              [3,4]])

print("Matrix A:\n",A)
print("Matrix B:\n",B)

# 1. Addition
add = A + B
print("\nAddition of Two Matrices:\n",add)

#2. Subtraction
sub = A - B
print("\nSubtraction of Two Matrices:\n",sub)

#3.Multiplication
multiply = np.dot(A,B)
print("\nMultiplication of Two Matrices:\n",multiply)
# np.dot(matrix 1 name,matrix 2 name....) the np.dot() is a built in function of numpy used for matrix multiplication

# 4. Transpose
transpose_A = np.transpose(A)
print("\n The Transpose of Matrix A is :\n",transpose_A)
# np.transpose() for finding tranpose of matrix 
#transpose means converting rows and columns and columns into rows

#5. Determinant
det_A = np.linalg.det(A)
print("\n The Determinant of Matrix A is :\n",round(det_A,2))
# np.linalg.det(matrix name) = gives directly determinant value
# determinant = a single numeric value calculated from a square matrix used to check matrix have inverse or not ,to solve linear equations and used in graphics,AI,ML,engineering
#matrix is a box of number and determinant is the value of that box




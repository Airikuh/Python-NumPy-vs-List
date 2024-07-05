# Erika Valle-Baird, Summer 2024
# Q2 Homework 1 ECE 5831
# Notebook comparing the time for each of the 3 different expressions done for NumPy Arrays and Python Lists

import numpy as np
import time

# Matrix X
X = np.array([[2, 4],
          	[1, 3]])

# Vector y
y = np.array([[1],
          	[3]])

# Vector z
z = np.array([[2],
          	[3]])

#start the timer
start_time = time.time()

# loop to test this calculation 10,000 times
for i in range(10000):
	# Must first transpose y
	t = y.T
	# Then do the dot product with z
	t.dot(z)

# Calculate the difference between start and end time to determine how long it took.
end_time = time.time() - start_time

# Print results to screen
print(f"Time it took for Numpy to Transpose y, then do the dot product with z 10,000 times: {end_time} seconds")

#start the timer
dot_start = time.time()

# loop to test this calculation 10,000 times
for i in range(10000):
# Dot Product Xy, results in [14, 10]
	# Do Xy calculations
	X.dot(y)

dot_end = time.time() - dot_start

# Print results to screen
print(f"Time it took for Numpy to do the dot product of Xy 10,000 times: {dot_end} seconds")

#start the timer
inverse_start = time.time()

# loop to test this calculation 10,000 times
for i in range(10000):
	np.linalg.inv(X)

inverse_end = time.time() - inverse_start

# Print results to screen
print(f"Time it took for Numpy to compute the inverse matrix of X 10,000 times: {inverse_end} seconds")


overall_time = end_time + dot_end + inverse_end

print(f"Overall time for Numpy Arrays to compute all 3 expressions 10,000 times: {overall_time} seconds ")





#Python Lists Times
import time

# vector y as list
y = [1, 3]
#vector z as list
z = [2, 3]


#start the timer
start_timeList = time.time()

for j in range(10000):
    # Multiply elements
    result = [y[i] * z[i] for i in range(len(y))]
# Calculate the Addition portion of the dot product
    final = result[0] + result[1]

# Calculate the difference between start and end time to determine how long it took.
end_timeList = time.time() - start_timeList

# For error checking the solution
# print("Solution: ", final)


# Print results to screen
print(f"Time it took for Python List to calculate y^T times z 10,000 times: {end_timeList} seconds")



# Matrix X as a list
X = [[2, 4], [1, 3]]
y_v = [[1], [3]]


# start the timer
X_y_start = time.time()

for j in range(10000):
    result = [[sum(a * b for a, b in zip(X_row, y_col)) for y_col in zip(*y_v)] for X_row in X]

# Error Checking
#print("Xy = [")
#for r in result:
    #print(r)
#print("]")

# Calculate the difference between start and end time to determine how long it took.
X_y_end_time = time.time() - X_y_start



# Print results to screen
print(f"Time it took for Python List to calculate X time y 10,000 times: {X_y_end_time} seconds")





#start the timer
X_inv_start_time = time.time()

for j in range(10000):
    # Determine the inverse matrix
    a = X[0][0]
    b = X[0][1]
    c = X[1][0]
    d = X[1][1]

    # Check values are correct
    #print("a = ", a)
    #print("b = ", b)
    #print("c = ", c)
    #print("d = ", d)

    # Get the det value
    det = 1 / ((a * d) - (b * c))

    # Check values are correct
    #print("det = ", det)

    New_X = [[0, 0], [0, 0]]

    New_X[0][0] = d
    New_X[0][1] = b * (-1)
    New_X[1][0] = c * (-1)
    New_X[1][1] = a

    # Loop over to multiply X by the determinant
    for k in range(len(New_X)):
            for m in range(len(New_X[k])):
                         New_X[k][m] = det * New_X[k][m]


# Error checking for results
#for res in New_X:
    #print(res)


# Calculate the difference between start and end time to determine how long it took.
X_inv_end_time = time.time() - X_inv_start_time


# Print results to screen
print(f"Time it took for Python List to calculate X^-1 10,000 times: {X_inv_end_time} seconds")


overall_list_time = X_y_end_time + X_inv_end_time + end_timeList
# Print results to screen
print(f"Overall time taken for computation for the 3 different expressions 10,000 times {overall_list_time} seconds")

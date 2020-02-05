
# # NumPy Exercises 

# Import NumPy as np
import numpy as np


# Create an array of 10 zeros 
np.zeros(10)


# Create an array of 10 ones
np.ones(10)


# Create an array of 10 fives
arr = np.ones(10)
arr[:10] = 5
print(arr)


# Create an array of the integers from 10 to 50
np.arange(10,51)


# Create an array of all the even integers from 10 to 50
arr = np.arange(10,51)
print(arr[arr%2==0])


# Create a 3x3 matrix with values ranging from 0 to 8
np.arange(9).reshape(3,3)


# Create a 3x3 identity matrix
np.identity(3)


# Use NumPy to generate a random number between 0 and 1
np.random.rand(1)


# Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
np.random.randn(25)


# Create the following matrix:
#np.arange(1,101).reshape(10,10)/100
np.linspace(0.01,1,100).reshape(10,10)


# Create an array of 20 linearly spaced points between 0 and 1:
np.linspace(0,1,20)


# ## Numpy Indexing and Selection
# 
# Now you will be given a few matrices, and be asked to replicate the resulting matrix outputs:
mat = np.arange(1,26).reshape(5,5)
mat

# array([[ 1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10],
#        [11, 12, 13, 14, 15],
#        [16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])

# array([[12, 13, 14, 15],
#        [17, 18, 19, 20],
#        [22, 23, 24, 25]])
mat[2:,1:]



# 20
mat[3,4]


# array([[ 2],
#        [ 7],
#        [12]])
mat[:3,1:2]

# array([[21, 22, 23, 24, 25]])
mat[4:]

# array([[16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
mat[3:]


# Now do the following

# Get the sum of all the values in mat
np.sum(mat)


# Get the standard deviation of the values in mat
np.std(mat)


# Get the sum of all the columns in mat
mat.sum(axis=0)

import numpy as np

# orignal arrays
a = np.array([1,2,3])
b = np.array([4,5,6])
# reshape arrays to 2-D
c = a.reshape(1,3)
d = b.reshape(1,3)
# show original arrays
print('Array a: ', a)
print('Array b: ', b)
# show reshaped arrays
print('\n')
print('Array a 1-D to 2-D: ', c)
print('Array b 1-D to 2-D: ', d)
# show array shapes
print('\n')
print('Shape of array c: ', c.shape)
print('Shape of array d: ', d.shape)
# show array sizes
print('\n')
print('Size of array a: ', a.size)
print('Size of array b: ', b.size)
print('Size of array c: ', c.size)
print('Size of array d: ', d.size)
# show array lengths
print('\n')
print('Length of a: ', len(a))
print('Length of b: ', len(b))
print('Length of c: ', len(c))
print('Length of d: ', len(d))
# addition 
print('\n')
print('Addition:')
print('a[1] + b[2]: ', a[1] + b[2])
print('a[1] + c[0][0]: ', a[1] + c[0][0])
# subtraction
print('\n')
print('Subtraction:')
print('c[0][2] - d[0][0]: ', c[0][2] - d[0][0])
print('a[2] - c[0][2]: ', a[2] - 
     c[0][2])
# division
print('\n')
print('Division:')
print('a[2] / d[0][2]: ', a[2] / d[0][2])
print('c[0][0] / d[0][0]: ', c[0][0] / d[0][0])
# multiplication
print('\n')
print('Multiplication:')
print('c[0][2] * a[1]: ', c[0][2] * a[1])
print('d[0][0] * c[0][2]: ', d[0][0] * c[0][2])
# comparison ==, <, >, <=, >=, !=
print('\n')
print('Comparison:')
print('a == b: ', a == b)
print('a == a: ', a == a)
print('c <= d: ', c <= d)
x = np.array([3, 2, 6])
y = np.array([1, 2, 4])
print ('[3, 1, 6] >= [1, 2, 4]: ', x >= y)
print ('[[3, 1, 6]] >= [[1, 2, 4]]: ', x.reshape(1,3) >= y.reshape(1,3))
print ('[[3, 1, 6]] <= [[1, 2, 4]]: ', x.reshape(1,3) <= y.reshape(1,3))
print('a != b: ', a != b)
print('c != d: ', c != d)
print('x != y: ', x != y)
# sum, min, max, mean, median
print('\n')
print('Aggregate Functions:')
print('Sum of a[0] and b:[2] ', a[0] + b[2])
print('Sum of a[1] + a[2]: ', a[1] + a[2])
print('Min of a: ', min(a))
print('Min of c: ', min(c))
print('Mean of a: ', a.mean())
print('Mean of c: ', c.mean())
print('Median of b: ', np.median(b))
print('Median of d: ', np.median(d))
# create a copy of the arrays
print('\n')
print('Array copies:')
print('Copy of a: ', np.copy(a))
print('Copy of d: ', np.copy(d))
# sort the arrays, ascending
print('\n')
print('Sorting arrays:')
print('B sorted ascending: ', np.sort(b))
# sort the arrays, descending
print('A sorted descending: ', np.sort(a)[::-1])
# append, insert, and delete
print('\n')
print('8 inserted to array a: ', np.insert(a, 3, 8))
print('[4, 5, 6] appended to a: ', np.append(a, [4, 5, 6]))
print('Delete 3 from a: ', np.delete(a, 2, 0))
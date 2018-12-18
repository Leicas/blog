---
author: gbmhunter
date: 2018-06-25 21:28:41+00:00
draft: false
title: Numpy
type: page
url: /programming/languages/python/packages/numpy
---

# The Array

The main object that you throw around in NumPy is called a multidimensional array. Typically you store numbers in it. Each "dimension" is called an axes. For example, a single co-ordinate in 3D space could be stored as:

```py    
V = [2, 4, 3]
```

This has one axis (one dimension).

A 2D rotation transformation could be described with:

```py    
R = [
    [2, 3, 5],
    [1, 7, 2]
] 
```

This has two axes.

# Creating An Array

NumPy arrays can be created with standard Python lists:

```py    
>>> import numpy as np
>>> a = np.array([2,1,5])
>>> a
array([2, 5, 1])
```

If we wanted to create a 2 axis array we could pass in a list of lists:

```py    
>>> import numpy as np
>>> a = np.array([[1,2,3],[4,5,6])
>>> a
array([[1, 2, 3],
        [4, 5, 6]])
```

You can continue to nest lists within lists to create an array with any number of axes (dimensions).

You can also create arrays with special values, such as arrays full of 1's, arrays full of zero's, arrays full of random numbers and arrays with 1's on the diagonal (like identity matrices).

An array of 1's:

```py    
>>> a = np.ones([2,3])
>>> a
array([[1., 1., 1.],
        [1., 1., 1.]])
```

An array with 1's on the diagonal:

```py    
>>> a
array([[1., 0., 0.],
        [0., 1., 0.],
        [0., 0., 1.]])
```

Another really useful way of creating arrays is with np.arange(). This does exactly what is says, it creates an array with a range of values:

```py    
>>> np.arange(4)
array([0, 1, 2, 3])

>>> a = np.arange(9)
>>> np.reshape(a, [3, 3])
array([[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]])
```

`np.linspace()` is another great array creating tool, which creates an array of linearly spaced numbers. The following example creates 5 numbers, linearly spaced from 4.0 to 10.0:

```py    
>>> np.linspace(4.0, 10.0, 5)
array([ 4. ,  5.5,  7. ,  8.5, 10. ])
```

# Indexing And Reading/Writing

NumPy arrays have one index per axis, forming a tuple. The indexed are zero-indexed, like all sensible languages/libraries :-D.

Reading from a 1 axis array:

```py    
>>> a = np.array([2,1,5])
>>> a[2]
5
```

Reading from a 2 axis array:

```py    
>>> a = np.array([[2,5],[1,3]])
>>> a[0,1]
5
```

Writing to a 2-axis array:

```py    
>>> a = np.array([[2,5],[1,3]])
>>> a[1,1] = 10
>>> a
array([[ 2,  5],
        [ 1, 10]])
```

# Doing Basic Operations With Arrays

NumPy arrays can be added element wise with the `+` operator:

```py    
>>> a = np.array([[1,2,3],[4,5,6]])
>>> b = np.array([[1,1,2],[2,2,1]])
>>> a+b
array([[2, 3, 5],
        [6, 7, 7]])
```

They can be multiplied element-wise with the `*` operator (this is the same as `np.multiply`):

```py    
>>> a = np.array([[2,5],[1,3]])
>>> b = np.array([[1,4],[2,1]])
>>> a*b
array([[ 2, 20],
        [ 2,  3]])
```

A dot-product of two arrays can be done with `np.dot()`:

```py    
>>> a = np.array([[2,5],[1,3]])
>>> b = np.array([[1,4],[2,1]])
>>> np.dot(a, b)
array([[12, 13],
        [ 7,  7]])
```

The cross-product of two arrays can be done with `np.cross()`:

```py
>>> a = np.array([4,5,1])
>>> b = np.array([3,1,2])
>>> np.cross(a, b)
array([ 9, -5, -11])
```

# Slicing

One of the powerful features of Numpy arrays is the simple and terse slicing syntax (which is built upon Python's slicing syntax). A slice is when you extract just a portion of the array for further use:

## Simple Slicing

Very simple slicing is really the same as indexing:

```py
my_array = np.array([4, 5, 6])
my_slice = my_array[1]
# my_slice = 5
```

Extract the first two elements:

```py
my_array = np.array([4, 5, 6])
my_slice = my_array[0:2]
# my_slice = array([4, 5])
```

## Multidimensional Slicing

Some of the real power of slicing is seen when you slice multidimensional arrays (arrays with more than 1 axis).

`my_array[:, 0]` tells Numpy to make a slice using all elements from the 1st axis (`:`), and only the first element from the second axis (`0`). An example of this slice is shown below:

```py
my_array = np.array([[1, 2, 3], [4, 5, 6])
my_slice = my_array[:, 0] # Take all from 1st axis, and element 0 from second axis
# my_slice = array([1], [4])
```

Note that `:` is the same as `0:<len - 1>`, and captures all data.

This is commonly used to extract columns from data. For example, if you had the following array of x, y pairs:

```py
xy_pairs = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
```

You could extract all the x values and all the y values with:

```py
x_values = xy_pairs[:, 0]
y_values = xy_pairs[:, 1]

# x_values = array([[1], [3], [5], [7]])
# y_values = array([[2], [4], [6], [8]])
```

You can also use this to extract "rows" from an array:

```py
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
two_rows = data[1:3, :]
# two_rows = array([[4, 5, 6], [7, 8, 9]])
```

## Adding A Step

You can also add a step size while slicing Numpy arrays, just as you can when using standard Python slicing. The step size is the third argument in the slice syntax, i.e. `start:stop:step`.

```py
data = np.arange(10)
# data = array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
my_slice = data[3:8:2] # Slice from 3 to 8, with a step size of 2
# my_slice = array([3, 5, 7])
```

# Reading A CSV File

You can use Numpy's `genfromtxt()` method to read in CSV files and convert the data into a Numpy array:

```py
data = np.genfromtxt('my_file.csv', delimiter=',')
```

Each line will be a different element in axis 1 of the array. Each CSV value on a line will be a different element in axis 2 of the array.

For example, if your CSV looked like:

```csv
0, 1, 2
10, 11, 12
```

The array would look like:

```
[ [0 1 2], [10 11 12] ]
```

## Skip Header Rows

You can skip a header line/row in the CSV file by providing `skip_header=1` to `genfromtxt()`:

```py
data = np.genfromtxt('my_file.csv', delimiter=',', skip_header=1)
```

This is good when you have column data names in the first row (which is a common practice), e.g.:

```
Time (s), Depth (m), Width (m)
0, 1, 2
10, 11, 12
```

# Functions

**dot()**

```py    
np.dot(a, b, out=none)
```

Dot product of two arrays.

**np.eye()**

Returns an array with 1's on the diagonal and 0's elsewhere (also known as an identity matrix).

```py    
my_array = np.eye(3)
# my_array = array([
#   [1, 0, 0],
#   [0, 1, 0],
#   [0, 0, 1]])
```

**np.ravel()**

Returns a flattened array.
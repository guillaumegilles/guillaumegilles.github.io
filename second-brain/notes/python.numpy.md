---
id: dlw9y7kopo10ebmm8azhyct
title: NumPy
desc: >-
  Python package for working with arrays, or large collections of homogenous
  data
updated: 1697400534466
created: 1649016213406
---

You can think of an array like a spreadsheet, where numbers are stored in columns and rows.

Background: Python wasn’t originally intended for numerical computation when it was launched in 1991. Still, its ease of use caught the scientific community’s attention early on. Over the years, the open source community developed a succession of packages for numerical computing. In 2005, developer Travis Oliphant combined over a decade’s worth of open source developments into a single library for numerical computation, which he called NumPy. 

Features: The core feature of NumPy is support for arrays, which allows you to quickly process and manipulate large collections of data.

Arrays in NumPy can be n-dimensional. This means the data can be a single column of numbers, or many columns and rows of numbers.

NumPy has modules for performing some linear algebra functions. 
It also has modules for graphing and plotting numerical arrays. 
Data in NumPy arrays is homogenous, which means it must all be defined as the same type (numbers, strings, Boolean values, etc.). This means data gets processed efficiently.

Best for: Manipulating and processing data for more advanced data science or machine learning operations. If you are crunching numbers, you need NumPy. 

Downsides: Because NumPy arrays are homogeneous, they are a bad fit for mixed data. You are better off using Python lists. Also, NumPy’s performance tends to drop off when working with more than 500,000 columns.
Best place to learn: [Linear Regression with NumPy and Python](https://www.coursera.org/projects/linear-regression-numpy-python) from Coursera.








Il n’est pas possible de réaliser des calculs sur des [[listes|python.list]] 
python.

```python
height = [1.73, 1.68, 1.71, 1.89, 1.79]
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
weight / height ** 2
>   TypeError: unsupported operand type(s) for ** or pow(): 'list' and 'int'
```

La solution se trouve dans le package **NumPy**, *Numeric Python* grâce au 
[[py.dt.numpy-array]]. Les calculs sur les arrays sont simples et rapides.

```python
import numpy as np
np_height = np.array(height)
np_height
>    array([1.73, 1.68, 1.71, 1.89, 1.79])

np_weight = np.array(weight)
np_weight
>    array([65.4, 59.2, 63.6, 88.4, 68.7])

bmi = np_weight / np_height ** 2
bmi
>    array([21.85171573, 20.97505669, 21.75028214, 24.7473475 , 21.44127836])
```

### Remarques

1. Pour réaliser des opérations sur des arrays, il faut qu’elles ne contiennent 
   qu’un type de données.
2. Les arrays constituent un [[type de données|py.dt]], elles possèdent donc des 
   comportents propres.

## Fichiers NumPy
- `.npy` : NumPy array
- `.npz` : plusieurs NumPy array non compressé

To determine the number of arrays in a NumPy `.npz` file, you can use the `npzfile` object's `.files` attribute. This attribute returns a list of the names of the arrays or data structures stored within the `.npz` file. Each item in the list corresponds to a different array in the file. Here's how you can determine the number of arrays:

```python
import numpy as np

# Load the .npz file
data = np.load('your_data.npz')

# Get the list of array names
array_names = data.files

# Determine the number of arrays
num_arrays = len(array_names)

# Print the number of arrays and their names
print(f"Number of arrays: {num_arrays}")
print("Array names:", array_names)
```

In this code, replace `'your_data.npz'` with the path to your `.npz` file. The `np.load()` function loads the data from the file, and `data.files` gives you a list of the array names. The length of this list (`num_arrays`) will give you the number of arrays stored in the `.npz` file.

## ChatGPT
To find the number of clusters in a dataset stored in a NumPy `.npz` file, you typically need to perform clustering analysis on the data. NumPy `.npz` files store one or more arrays or data structures, so you first need to load the data from the file and then apply a clustering algorithm to it.

Here's a general outline of the steps to find the number of clusters:

1. **Load the Data**: Load the data from the `.npz` file using NumPy. You may have one or more arrays stored in the file, and you should select the one you want to perform clustering on.

```python
import numpy as np

data = np.load('your_data.npz')
array = data['array_name']  # Replace 'array_name' with the name of your array
```

2. **Data Preprocessing**: Depending on your data and the clustering algorithm you plan to use, you may need to preprocess the data. This may include standardizing the data or other preprocessing steps relevant to your specific dataset.

3. **Choose a Clustering Algorithm**: There are various clustering algorithms available, such as K-Means, DBSCAN, hierarchical clustering, etc. Choose an algorithm that suits your data and problem.

4. **Cluster the Data**: Apply the chosen clustering algorithm to the data. For example, if you're using K-Means, you can do the following:

```python
from sklearn.cluster import KMeans

# You need to specify the number of clusters (K) or use methods to determine it.
kmeans = KMeans(n_clusters=3)  # Specify the number of clusters
kmeans.fit(array)
```

5. **Determine the Number of Clusters**: There are various methods to determine the optimal number of clusters. One common approach is the "Elbow Method" or "Silhouette Score." For the Elbow Method, you can plot the cost (inertia) of K-Means for different values of K and look for an "elbow" in the plot, which indicates the optimal number of clusters. For Silhouette Score, you aim to maximize the average silhouette score.

Here's an example of using the Elbow Method to find the optimal number of clusters:

```python
import matplotlib.pyplot as plt

cost = []
for k in range(1, 10):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(array)
    cost.append(kmeans.inertia_)

plt.plot(range(1, 10), cost)
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Cost')
plt.show()
```

In the resulting plot, you can visually inspect for the "elbow" point where the cost starts to level off. That point indicates the optimal number of clusters for your data.

Remember that the choice of the clustering algorithm and the method for determining the number of clusters can vary depending on your data and specific problem. You may need to experiment with different algorithms and methods to find the most suitable solution for your data.

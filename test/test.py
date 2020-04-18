#Import Python libraries and packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import timeit
import random
from random import random

#--------------------------------------------------------------------------------------------
# Create an array for generating ten random numbers between 100 and 500. 
#--------------------------------------------------------------------------------------------

array10 =  [int(i) for i in np.sort(np.random.randint(100, 500, 10))]

#--------------------------------------------------------------------------------------------
# Calculate factorial for each number in array10 using a for loop.
# Store factorial and time results in separate arrays.
#--------------------------------------------------------------------------------------------

def forloop_factorial(x):
    result = 1
    start_time = time.perf_counter()
    for i in range(x+1):
        if i == 0:
            continue
        result = result * i
    end_time = time.perf_counter()
    return ((end_time-start_time)*1000, result)

import decimal
def array_assignment_1(array):    
    factorial_results = []    
    factorial_time_results = []
    for i in range(len(array)):
        (time, result) = forloop_factorial(array[i])
        factorial_results.append(str(result))
        factorial_time_results.append(time)
    return (factorial_results, factorial_time_results)
        
(forloop_results, forloop_time_results) = array_assignment_1(array10)

#--------------------------------------------------------------------------------------------
# Calculate factorial for each number in array10 using recursion.
# Store factorial and time results in separate arrays.
#--------------------------------------------------------------------------------------------

def recursive_factorial(x):    
    if x == 1:
        return 1
    else:
        return x * recursive_factorial(x-1)

def array_assignment_2(array):    
    factorial_results = []    
    factorial_time_results = []
    for i in range(len(array)):
        start_time = time.perf_counter()
        result = recursive_factorial(array[i])
        end_time = time.perf_counter()
        t = (end_time-start_time)*1000
        factorial_results.append(str(result))
        factorial_time_results.append(t)
    return (factorial_results, factorial_time_results)
        
(recursive_results, recursive_time_results) = array_assignment_2(array10)

# Create table for sorted array10 values, factorials, for loop and recursion time results and time difference.

def SubtracList(a,b):
    result = []
    for i in range(len(a)):
        result.append(a[i]-b[i])
    return result    
    
execution_data = pd.DataFrame({
    'Sorted Array Values': array10,
    'Factorial': recursive_results,
    'For Loop Time': forloop_time_results,
    'Recursive Time': recursive_time_results,
    'Recursive - For Loop': SubtracList(recursive_time_results, forloop_time_results)
})
execution_data_1 = execution_data[['Sorted Array Values','Factorial','For Loop Time','Recursive Time','Recursive - For Loop']]
execution_data_1

# Create plot for recursion and for loop execution times against each individual array10 value.

ax = plt.gca()

execution_data_1.plot(kind='line',x='Sorted Array Values',y='For Loop Time',ax=ax)
execution_data_1.plot(kind='line',x='Sorted Array Values',y='Recursive Time', color='green', ax=ax)

plt.xlabel('Array Value')
plt.ylabel('Execution Time')
plt.title('Figure 1: For Loop and Recursive Execution Runtime')
plt.plot()

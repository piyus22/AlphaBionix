#By- Piyus Mohanty
#Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays
import numpy as np
a=np.random.randint(100,size=(3,4))
b=np.random.randint(100,size=(3,4))
print("array 1 contents are:",a)
print("array 2 contents are: ",b)
print("The greater between the two array is: \n")
print(np.greater(a,b))
print("The position_value equal between the two array is: \n")
print(np.greater_equal(a,b))
print("The lower value between the two array is: \n")
print(np.less(a,b))
print("The lower position_value equal between the two array is: \n")
print(np.less_equal(a,b))

import sys 
  
# Function to return the sum of  
# the minimum pair from the array  
def smallest_pair(a, n) : 
      
    min = sys.maxsize 
    secondMin = sys.maxsize 
      
    for j in range(n) :  
  
        # If found new minimum  
        if (a[j] < min) : 
  
            # Minimum now becomes  
            # second minimum  
            secondMin = min
  
            #Update minimum  
            min = a[j] 
          # If current element is > min  
          # and < secondMin 
       												  
        elif ((a[j] < secondMin) and 
               a[j] != min) : 
  
            # Update secondMin  
            secondMin = a[j]  
      
    # Return the sum of the minimum pair  
    return (secondMin + min) 
  
# Main func code  
if __name__ == "__main__" :  
  
    arr = [ 1, 2, 3 ]  
    n = len(arr)  
  
    print(smallest_pair(arr, n)) 

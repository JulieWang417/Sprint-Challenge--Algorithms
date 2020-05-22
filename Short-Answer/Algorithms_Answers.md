#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)
The while loop will run (n^3) / (n^2) times, which is equal to n times.
Therefore the time complexity will be O(n)


b) O(nlogn) 
The outer loop will run n times, while the inner loop will run log(n) times. 
How many times you need multiply a number by itself to get n is the log[base](n) function. (i.e. log[2](256) = 8 because you need to multiply 2 by itself 8 times to get 256. )
(The default base number when log does not write a base number is 2.)

c) O(n)
Ignoring constants, this function recursively calls itself until hits 0, subtracting 1 from its value everytime, thus doing it n times.

## Exercise II

# Function to get minimum number of trials  
# needed in worst case with n eggs and k floors 

The solution is to try dropping an egg from every floor(from 1 to k) and recursively calculate the minimum number of droppings needed in the worst case.
Worst case scenario gives the user the surety of the threshold floor. 
When we drop an egg from a floor x, there can be two cases 
(1) The egg breaks 
(2) The egg doesn’t break.

If the egg breaks after dropping from ‘xth’ floor, then we only need to check for floors lower than ‘x’ with remaining eggs as some floor should exist lower than ‘x’ in which egg would not break; so the problem reduces to x-1 floors and n-1 eggs.
If the egg doesn’t break after dropping from the ‘xth’ floor, then we only need to check for floors higher than ‘x’; so the problem reduces to ‘k-x’ floors and n eggs.

Since we need to minimize the number of trials in worst case, we take the maximum of two cases. We consider the max of above two cases for every floor and choose the floor which yields minimum number of trials.

The time complexity is exponential O(2**n).
The Space complexity is:O(1). As there was no use of any data structure for storing values.



Here is my codes:


    import sys 
    def Drop(n, k): 
        """
        base case
        If there are no floors, then no trials needed. 
        OR if there is one floor, one trial needed. 
        """
        if (k == 1 or k == 0): 
            return k   # drop(n,1)=1,drop(n,0)=0
  
        # We need k trials for one egg and k floors 
        if (n == 1): 
            return k   # drop(1,k)=k
  
        min = sys.maxsize 
  
        # Consider all droppings from 1st floor to kth floor 
        # and return the minimum of these values plus 1. 
        for x in range(1, k + 1): 
  
            res = max(Drop(n - 1, x - 1),  
            Drop(n, k - x)) 
        # egg break, go down floor: drop(n-1,x-1)
        # no break, keep going up, k-x floor left: drop(n,k-x)
        if (res < min): 
            min = res 
  
        return min + 1 
    
    # add 1 since we need to add this currently operation.



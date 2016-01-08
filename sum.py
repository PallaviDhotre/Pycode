/* Program that sums all numbers within the range i = 1…1000 inclusive. If that number is a multiple of 3 or 5, double it and add it to the sum. For example, i = 1-10, the answer is 88.
*/

sum=0
for i in range(1,1001): #range 1-1000 (inclusive) 
    if((i % 3 == 0) or (i % 5 == 0)):
        sum = sum + (i * 2) #double the number if it is a multiple of 3 or 5
    else:
        sum = sum + i
        
print sum

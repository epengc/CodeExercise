# Dynamic Array
## Problem
- Declare a 2-dimensional array, arr , of n empty arrays. All arrays are zero indexed.
- Declare an integer, lastAnswer, and initialize it to 0.
- There are 2 types of queries, given as an array of strings for you to parse:
    1. Query: 1 \times y
        1. Let idx = ((x \oplus lastAnswer)%n).
        2. Append the integer y to arr[idx] .
    2. Query: 2 \times y
        1. Let idx = ((x \oplus lastAnswer)%n).      
        2. Assign the value arr[idx][y % size(arr[idx])] to lastAnswer.
        3. Store the new value of lastAnwer to an answer array.

**Note**: \oplus  is the bitwise XOR operation, which corresponds to the \^ operator in most languages.
Learn more about it on Wikipedia. \% is the modulo operator.
Finally, size(arr[idx]) is the number of elements in arr[idx]


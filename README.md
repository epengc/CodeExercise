# Data Structure and Algorithm Workout
This is a practice on data structure and algorithms for coding interveiw. The containts of the code challenge includes:
## Data Structures Contents:
1. **Array**
2. **Linked List**
3. **Trees**
   - Binary/Balanced
5. **Heap**
6. **Hash Table**
7. **Stack**
8. **Queue**
9. **Tire**
10. **Graph(both directed & undirected)**
## Algorithms:
1. **Sorting**
   - Bubble Sort
   - Merge Sort
   - Quick Sort
   - Radix/Bucket Sort
2. **Traversals or Graph Theory**
   - Depth First Search
   - Breadth First Search
   - Recursion
3. **Search**
   - Sequential Search (ex:Linear)
   - Interval Search (ex: Binary)
      - Jump Search
      - Interpolation

# Types of Data Structures:
## Primitive
- Integer
- Float
- Character
- String
- Boolean

## Non Primitive
- Linear
    - Static
        - Array
    - Dynamic
        - Linked List
        - Stack
        - Queue
- Non Linear
    - Tree
    - Graph

# Types of Algorithms:
- Simpple Recursive Algorithms
    ```cpp
    Algorithm Sum(A, n)
        if n = 1
            return A[0]
        s = Sum(A, n-1)
        s = s + A[n-1]
    return s
    ```
- Devide and Conquer Algorithms contains two parts:
    1. Divide the problem into smaller subproblems of the same type, and solve these subproblems recursively.
    2. Combine the solution to the subproblems into a solution to the original problem.
        - Examples: Quick Sort and Merge Sort
- Dynamic Programming Algorithms
    1. They work based on memoization, which means that these algorithms remember the past results and use them to find new results.
    2. To find the best solution.
    These types algorithms are generally used for optimization problems. The goal is to find the best solution among multiple solutions.
- Greedy Algorithms
    - We take the best we can without worrying about future consequences.
    - We hope that by choosing a local optimum solution at each step, we will end up at a global optimum solution.
- Brute Force Algorithms
    - It simply tires all possibilities until a satisfactory solution is found.
- Randomized Algorithms
    - Use a random number at least once during the computation to make decision.




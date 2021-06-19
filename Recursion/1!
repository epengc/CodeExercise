# Recursion
This is a personal learning note for Udemy course: The Complete Data Structures and Algorithms Course in Python -- Elshad Karimov, Software Developer
## What is Recursion?

**Recursion = a way of solving a problem by having a function calling itself.**
- Performing the same operation multiple times with different inputs.
- In every step we try smaller inputs to make the problem smaller.
- Base condition is needed to stop the recursion, otherwise infinite loop will occuri.
```python
def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)
```

## Why Recursion?

1. Recursive thinking is really important in programming and it helps you break down big problems into smaller ones and easier to use.
    - When to choose resursion?
        - If you can divine the problem into similar sub problems.
        - Design an algorithm to compute nth...
        - Write code to list the n...
        - Implement a method to compute all.
        - Practice.
2. The prominenent usage of recursion in date structures like treees and graphs. \( **So when you are dealing with trees, the recursion becomes almost mandatory to use.** \)
3. Interviews.
4. It is used in many algorithms \( devide and conquer, greedy and dynamic programming \)

## How Recursion Works?
1. A emthod calls it self.
2. Exit from infinite loop.
```python
    def recursionMethod(parameters):
        if exit from condition satisfied:
            return some value
        else:
            recursionMethod(modified parameters)
```

The 1st good example:

```python
    def firstMethod():
        secondMethod()
        print("I am the first method")

    def secondMethod():
        thirdMethod()
        print("I am the second method")

    def thirdMethod():
        fourthMethod()
        print("I am the third method")

    def fourthMethod()
        print("I am the fourth method")

```

The 2nd good example:

```python
    def recursiveMethod(n):
        if n<1:
            print("n is less than 1")
        else:
            recursiveMethod(n-1)
            print(n)
```

Stack memory is controlled by system to call the recursive method.


## Recursive VS Iterative Solutions
Recursive method example:
```python
    def powerOfTwo(n):
        if n == 0:
            return 1
        else:
            power = powerOfTwo(n-1)
            return power*2
```
Iterative method example:
```python
    def powerOfTwoIt(n):
        i = 0
        power = 1
        while i<n :
            power = power*2
            i = i+1
        return power
```

Table of Comparasion between **Recursive** and **Iterative** solutions
| Points           | Recursion    | Iteration    |                                              |
|-----------------:|-------------:|-------------:|---------------------------------------------:|
| Space efficient ?| No           | Yes          | No stack memory require in case of Iteration |
| Time efficient ? | No           | Yes          | In case of recursion system needs more time for pop and push elements to stack memory which makes recursion less time efficient|
| Easy to code ?   | Yes          | No           | We use recursion especially in the cases we know theat a problem can be divided into similar subproblems|


## When to Use/Aviod Recursion?

### When to use it?
- When we can easily breakdown a problem into similar subproblems.
- When we are fine with exatra overhead (both time and space) that comes with it.
    - If you are developing a mobile application, which should run on low memeory devices as well.



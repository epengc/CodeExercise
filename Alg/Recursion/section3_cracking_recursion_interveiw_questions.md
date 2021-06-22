# Interview Questions -1 

How to find the sum of digits of a positive integer number using recursion?

## Step 1: Recursive case - the flow

10 10/10 = 1 and Remainder = 0
54 54/10 = 5 and Remainder = 4
112 112/10 = 11 and Remainder = 2
and  11/10 = 1 and Remainder = 1

f(n) = n%10 + f(n/10)

## Step 2: Base case - the stopping criterion
- n = 0

## Step 3: Unintentional case - the constraint

- sumofDigits(-11) ??
- sumofDigits(1.5) ??

# Interview Questions - 2

How to calculate power of a number using recursion?

## Step 1 : Recursive case - the flow
x^n = x \times x \times x ..(n times)..\times x
2^4 = 2\times 2 \times 2 \times 2

# Interview Questions - 3
How to find GCD (Greatest Common Divisor) of two numbers using recursion?
GCD is also known as the Gre
## Step 1 : Recursive case - the flow

GCD is the largest positive integer that divides the numbers without a remainder

gcd(8, 12)=4
8 = 2 \times 2 \times 2
12 = 2 \times 2 \times 3

** Eucilidean Algorithm **
gcd(48, 18)
Step 1: 48/18 = 2 remainder 12      gcd(a, 0) = a
Step 2: 18/12 = 1 remainder 6       gcd(b, a) = gcd(b, a mod b)
Step 3: 12/6 = 2 remainder 0

## Step 2 : Base case - the stopping criterion
- b = 0

## Step 3 : Unintenional case - the constraint
- Positive integers
- Convert negative numbers to positive

# Interview Questions - 4
How to convert a number from Decimal to Binary using recursion

## Step 1 : Recursive Case - the flow
### Step 1 : Divide the number by 2
### Step 2 : Get the integer quotient for the next iteration
### Step 3 : Get the remainder for the binary digit
### Step 4 : Repeat the steps until the quotient is equal to 0

Table 1 Example of the Process
| Division by | Quotient | Remainder |
|------------:|---------:|----------:|
|10/2         |5         |0          |
|5/2          |2         |1          |
|2/2          |1         |0          |
|1/2          |0         |1          |

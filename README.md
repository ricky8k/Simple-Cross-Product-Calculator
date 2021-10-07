# Simple-Cross-Product-Calculator
Simple Cross-Product Calculator developed using Python.

This application allows you to multiply a pair of vectors by simply inputting `i`, `j`, and `k` to get a vector perpindicular to the two.

## Installation
You will need:
- Python 3.9.2 or later

Download `Simple.Cross-Product.Calculator.py` from the Releases tab. Run/open to start the script.

File was tested with Python 3.9.2 with Windows 10 19043.1237, may or may not work with older Windows version or with Linux-based distros.

## Usage
You will need the two rectangular forms of the two given vectors.

Type in the `i`, `j`, and `k` values for both vectors to get the answer.

### Example
Given a pair of vectors in rectangular form:
```
A = -2i - 3j - 5k
B =  3i + 5j - 7k
```
The input to the calculator for vector `A` is as follows:
```
Enter vector A:
-2
3
-5
```
The input to the calculator for vector `B` is as follows:
```
Enter vector B:
3
5
-7
```
To get an output of:
```
Input:
-2.0i 3.0j -5.0k
3.0i 5.0j -7.0k
```
which displays the input for the user to double-check.

Below you'll find:
```
Solution:
-21.0i -15.0j -10.0k
25.0i -14.0j -9.0k
--------------------
4.0i -29.0j -19.0k
```
which shows the simplified work of the two sides from the following equation:
```
[(Ay * Bz)i + (Az * Bx)j + (Ax * By)k] - [(Ax * Bz)j + (Az * By)i + (Ay * Bx)k]
```
and adds them together to form the solution.

## 
- https://github.com/ricky8k

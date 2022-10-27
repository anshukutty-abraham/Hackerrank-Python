"""
You are given a string .
Your task is to verify that  is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

 Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
 -+4.5

 Number must contain at least  decimal value.
For example:
✖
 12.
✔
12.0  

 Number must have exactly one . symbol.
 Number must not give any exceptions when converted using .

Input Format

The first line contains an integer , the number of test cases.
The next  line(s) contains a string .

Constraints

Output Format

Output True or False for each test case.

Sample Input 0

4
4.0O0
-1.00
+4.54
SomeRandomStuff
Sample Output 0

False
True
True
False"""

import re
T=int(input())
if T>0 and T<10:
    X=[]
    for i in range(T):
        N=input()
        try:
            if bool(re.search(".[0-9]+",N)):#to handle integers/no decimal value e.g. 0,12.
                X.append(isinstance(float(N),float))#check if convertible to float--handles signed and unsigned numbers
            else:#to handle strings
                X.append("False")
        except:#to handle float conversion errors
            X.append("False")
    for j in X:
        print(j)

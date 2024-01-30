# complex-numbers
Well, I wanted to make a python library for complex numbers.
Here it is i guess.

# ok so how do i use it then
1. Download the file (obvs) into the folder with your target python file
2. At the start of the file just:
   ```python
   import complex
   ```
   Or, to make your life easier and bring everything into the global namespace:
   ```python
   from complex import *
   ```
3. You can make a complex number object, print it and perform arithmetic on it as shown below with comments:
   ```python
   from complex import *
   num=Complex(2,3)  # Made a complex number object and stored the complex number 2+3i into num
   print(num, num.r, num.c)  # Prints 2+3i 2 3- the complex number, real component and coefficient of i
   print(num.add(Complex(a,b)))  # Adds num to a+bi
   print(num.subtract(Complex(a,b)))  # Subtracts num by a+bi
   print(num.multiply(Complex(a,b)))  # Multiplies num and a+bi
   print(num.divide(Complex(a,b)))  # Divides num by a+bi
   ```

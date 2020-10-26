# Assignment Operators
"""
LeftOperand = RightOperand
x           = 5

-------------------------------------------
Operator |          Example      |      Equivatent to
-------------------------------------------
1.   =                  x = 5           x = 5
2.  +=                  x += 5          x = x + 5       [+= Add AND]
3.  -=                  x -= 5          x = x - 5       [-= Subtract AND]
4.  *=                  x *= 5          x = x * 5       [*= Multiply AND]
5.  /=                  x /= 5          x = x / 5       [/= Divide AND]
6.  %=                  x %= 5          x = x % 5       [%= Modulus AND]
7.  //=                 x //= 5         x = x // 5      [//= Floor Division]
8.  **=                 x **= 5         x = x ** 5      [**= Exponent AND]
"""
x = 20
number = x + 10  # number=20+10 =30
print("Add number:",number)
number -= x  #number = 30-20=10
print("subtract number:",number)
number *=x  #(20*10)
print("multiplication of 2 numbers",number)
number /=x #number/x   (200/20)
print("divide of 2 numbers",number)
number %=x
print("modulus no's",number)
number //=x
print("floor divsion:",number)
x **=5
print("exponent of:",x)


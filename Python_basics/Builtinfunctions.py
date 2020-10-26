#string special operators

Assume string variables a holds "Hello" and variable b holds "python" then

1. Operator : +(will work for numbers and strings)
   Desciption: Concatentation - Adds values on either side of the operator
   Example : a+b will give Hello python

2. Operator : *(will work for numbers and strings)
   Desciption: Repetation - Create new strings
                concatenating multiple copies of the same string
   Example : a*2 will give HelloHello

3. Operator []
   Desciption: slice - Gives the character from the given index
   Example : a[0]-H and a[1]-e

   Indexing
   Left to Right Indexing: 0 1 2 3 4 5 ---nth
   Right to left Indexing :       -nth....-4-3-2-1
               -5   -4   -3   -2   -1 (right to left indexing)
                0    1    2    3    4 (left to right indexing)
    firstname = G    U    I    D    O
    print("left to right indexing:",firstname(0))
    print("right to left indexing:",firstname(-5))

4. Operator [:]
   Desciption: Range slice - Gives the character from the given range
   Example : a[1:4] will give ell

5. Operator : in
   Desciption: Membership : Returns true if a character exists in the given string
   Example : H in a will give 1


6. Operator : not in
   Desciption: Membership : Returns true if a character not exists in the given string
   Example : M not in a will give 1

7. Operator: %
   Desciption:Format -performs string formatting

1. + : Concatenation
2. * : Repetation
3.[]: Slice
4.[:]: Range Slice (prefix and suffix values need to provide)
5. [::]: Zero based indexing (prefix and suffix values need to provide)
6. % : Format (Remainder sign)
7. .format() : is method
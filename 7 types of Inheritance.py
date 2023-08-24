#single
class A:
     a = 10
 
class B(A):
    b=10

obj=B()
print(obj.a)


#Multi-level
class C:
    c= 11

class D(C):
    d=12

class E(D):
    e=13

obj=E()
print(obj.c)
print(obj.d)
print(obj.e)

#Hierarchical
class A:
     a = 14
 
class B(A):
    b=15

class C(A):
    c=11

obj= B()
print(obj.a)

#multiple
class B:
    b=15
    def __init__(self,number):
        self.number = number
        print(number)

class C:
    c=16
class D(B,C):
    d=17

obj=D(100)
# obj.__init__(100)
print(obj.b)
print(obj.c)
print(obj.d)

#hybrid
class A:
    a=5
class B(A):
    b=6
class C:
    c=7
class D(B,C):
    d=8

obj = D()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)

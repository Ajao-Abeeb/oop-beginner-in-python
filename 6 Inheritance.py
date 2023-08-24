class A:
    a =9
    def method_a(self):
        print("Inside method_a")


class B(A):
    b=10
    def method_b(self):
        print("Inside method_b")



ans = B()
print(ans.a)
print(ans.b)
ans.method_b()
ans.method_a()
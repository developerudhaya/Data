class A:
    def disp1(self):
        print("this is disp1()")

class B(A):
    def disp2(self):
        print("this is disp2()")

class C(A):
    def disp3(self):
        print("this is disp3()")

if __name__== "__main__":
    obj1=A()
    obj1.disp1()

    obj=B()
    obj.disp1()
    obj.disp2()

    obj=C()
    obj.disp1()
    obj.disp3()

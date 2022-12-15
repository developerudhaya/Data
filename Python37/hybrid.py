class A:
    def disp1(self):
        print("this is disp1()")

class B:
    def disp2(self):
        print("this is disp2()")

class C(A,B):
    def disp3(self):
        print("this is disp3()")

class D(C):
    def disp4(self):
        print("this is diap4()")


if __name__== "__main__":
    obj=D()
    obj.disp1()
    obj.disp2()
    obj.disp3()
    obj.disp4()
    
    

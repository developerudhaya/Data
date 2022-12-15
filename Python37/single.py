class A:
    def disp1(self):
        print("this is disp1()")

class B(A):
    def disp2(self):
        print("this is disp2()")
        
if __name__== "__main__":
    obj=B()
    obj.disp1()
    obj.disp2()

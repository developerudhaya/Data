class A:
    def disp1(self):
        print("this is disp1()")

class B:
    def disp2(self):
        print("this is disp2()")
        
class C(A,B):
    def disp3(self):
        print("this is disp3()")

if __name__== "__main__":
    obj=C()
    obj.disp1()
    obj.disp2()
    obj.disp3()
    

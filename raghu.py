class J(object):
    def method(self):
        print("U")
class I(object):
    def method(self):
        print("H")
        super().method()
class H(I):
    def method(self):
        print("G")
        super().method()
class G(object):
    def method(self):
        print("A")
        super().method()
class F(G):
    def method(self):
        print("R")
        super().method()
class E(object):
    def method(self):
        print("A")
        super().method()
class D(E):
    def method(self):
        print("D")
        super().method()
class C(object):
    def method(self):
        print("N")
        super().method()
class B(C,D):
    def method(self):
        print("O")
        super().method()
class A(B,D,F,H,J):
    def method(self):
        print("K")
        super().method()
a=A()
a.method()
        
        
        
        
        
        
        

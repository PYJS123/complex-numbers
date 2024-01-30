class Complex:
    def __init__(self, real=0, comp=0):
        self.r=real
        self.c=comp

    def __str__(self):
        r,c=str(self.r),str(self.c)
        if self.c>=0:
            c="+"+c
        return f"{r}{c}i"

    def add(self, toAdd):
        return Complex(self.r+toAdd.r, self.c+toAdd.c)

    def subtract(self, toSub):
        return Complex(self.r-toSub.r, self.c-toSub.c)

    def multiply(self, toMult):
        a1, b1, a2, b2= self.r, self.c, toMult.r, toMult.c
        return Complex(a1*a2-b1*b2, a1*b2+a2*b1)

    def divide(self, toDiv):
        a1, b1, a2, b2= self.r, self.c, toDiv.r, toDiv.c
        r=(a1*a2+b1*b2)/(a2**2+b2**2)
        c=(a2*b1-a1*b2)/(a2**2+b2**2)
        return Complex(r, c)
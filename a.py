class A:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "1st is smaller"
        else:
            return "2nd is smaller"
o1=A(20)
o2=A(30)
print(o1<o2)

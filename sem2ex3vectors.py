__author__ = 'Barry'
#sem2 ex3 vectors

class Vector:
    def __init__(self,vector1,vector2):
        print(vector1,vector2)
        self.v1 =vector1
        self.v2=vector2


    def __str__(self,result):
        pass #pass for now
        #return result

    def __add__(self):
        (self.v1[1] +self.v2[1]#self.v1[2] + self.v2[2])

    def __sub__(self, other):
        return v
    def __mul__(self, other):
        pass
    def magnitude(self,other):
        pass

def main():

    x1 = int(input("please enter x1"))
    y1 = int(input("please enter y1"))

    x2 = int(input("please enter x2"))
    y2 = int(input("please enter y2"))

    vector1= (x1,y1)

    vector2= (x2,y2)

    Myvector =Vector(vector1,vector2)

    add = Vector.__add__(self)

if __name__ =="__main__":
    main()
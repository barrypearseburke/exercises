__author__ = 'Barry'
#lab 4 sem 2
class Fraction():
    def __init__(self,frac):
        self.num = frac[0]
        self.den =frac[1]

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def gcd(self):
        """
        how the gcd works. Larger number mod smaller no.
        Then dividde the orginal smaller no and mod by orginal remainer
        The last no 0 remiander is the gcd
        """
        remaindertest = -1
        remainderfinal = 0
        larger_no =int("0")
        smaller_no =int("0")
        larger_no = self.den
        smaller_no =self.num
        while remaindertest != 0:
            #work out gcd

            remaindertest = larger_no%smaller_no

            if remaindertest == 0:
                break

            else:
                remainderfinal =remaindertest
                larger_no = smaller_no
                smaller_no =remaindertest



        self.gcd =remainderfinal


    def lcm(self):
        pass



def main():
    #asks for user input
    numerator = int(input("Please enter your Numerator"))
    denominator = int(input("Please enter the Denominator"))

    #place each num and den and put into a tuple
    frac = (numerator, denominator)
    a =Fraction(frac)
    a.gcd()



if __name__ == "__main__":
    main()



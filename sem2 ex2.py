__author__ = 'Barry'

class clock:
    def __init__(self, hour =0 ,minute =0 ,second =0):
        self.hour =hour
        self.minute =minute
        self.second =second


    def __str__(self):
        return "{}:{}:{}".format(self.hour,self.minute,self.second)

    def __repr__(self):
        return self.__str__()

    def addtime(self,hour , minute, second):
        if (hour <=-1):
            print("error")
        return



def main():

    myclock =clock()
    print(myclock)
    #myclock()

    houradd =input("Please enter the current hour")
    minuteadd = input("Please enter the current minute")
    secondadd =input(" please enter the current second")

    myclock.addtime(houradd,minuteadd,secondadd)

if __name__ == "__main__":
    main()
__author__ = 'Barry'
# lab2 of semister 2 making a clock
class clock:
    def __init__(self, hour =0 ,minute =0 ,second =0):
        self.hour =hour
        self.minute =minute
        self.second =second
        self.day =0


    def __str__(self):
        if self.day == 0:

            return "{}:{}:{}".format(self.hour,self.minute,self.second)
        else:
            return "{} Days , {}:{}:{}".format(self.day,self.hour,self.minute,self.second)

    def __repr__(self):
        return self.__str__()

    def addtime(self,houradd , minuteadd, secondadd):
        houradd = int(houradd)
        minuteadd =int(minuteadd)
        secondadd =int(secondadd)

        if (houradd < 0):
            print("error")
            returnvalue =int("2")
            return returnvalue
        else:

            #lets try adding now
            self.second = self.second +secondadd
            while self.second >int("60"):
                minuteadd += int("1")
                self.second =self.second -int("60")

            self.minute = self.minute+minuteadd
            while self.minute >int("60"):
                houradd += int("1")
                self.minute =self.minute - int("60")
            self.hour =self.hour+houradd
            while self.hour> int("24"):
                self.day += int("1")
                self.hour =self.hour- int("24")

            returnvalue =int("0")
            return returnvalue


def main():

    myclock =clock()
    print(myclock)
    #myclock()

    counter =1
    while (counter !=0):
        houradd =input("Please enter the current hour")
        minuteadd = input("Please enter the current minute")
        secondadd =input("please enter the current second")

        if counter ==1:
            counter = myclock.addtime(houradd,minuteadd,secondadd)
            print(myclock)

        if counter==2:
            print("There was an error entering you one of the values. would you please enter again")
            counter = 1

if __name__ == "__main__":
    main()
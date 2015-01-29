__author__ = 'Barry'

class clock:
    def __init__(self, hour,minute,second):
        self.hour =hour
        self.minute =minute
        self.second =second


    def __str__(self):
        return "{}:{}:{}".format(self.hour,self.minute,self.second)

    def repr(self):
        self.__str__()




def main():
    hour =1
    minute =30
    second =10
    myclock =clock(hour,minute,second)
    print(myclock)
    # myclock()
if __name__ == "__main__":
    main()
__author__ = 'Barry'
#classess

class song():
    def __init__(self,lyrics):
        self.lyrics =lyrics
    def sing(self):
        for line in self.lyrics:
            print(line)

songtosing = ( ["happybday",
             "is it me your looking for"])
happybday =song(songtosing)

happybday.sing()
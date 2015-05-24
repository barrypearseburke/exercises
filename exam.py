__author__ = 'Barry'
Class my_iter:
    def __init__(self,max,multiplier):
    self.current =0
    self.max =max
    self.multiplier =  multiplier

    def __iter__(self):
    return self
    def __next__(sef)
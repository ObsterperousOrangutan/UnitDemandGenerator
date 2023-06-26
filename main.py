##### Purpose: Generate Logistics Demand for the Following Classes of Supply: 1, 3, 5, 7, and 9.

##### Imports
import numpy
import math
import os
from matplotlib import pyplot



#### Global Variables (none yet)
#### Classes of Classes of Supply.{unsure if I actuall have to do this yet 20230626} 
# Note to self: {20230626} 
# Hey stupid, you have to define the classes of supply before you use them for the different states of the world.
#### State of the World
class Competition:
    def __init__(self, ClassOne, ClassThree, ClassFive):
        self.ClassOne = ClassOne
        self.ClassThree = ClassThree
        self.ClassFive = ClassFive
    def ClassOne(self):
        print = "1"
    def ClassThree(self):
        print = "3"
    def ClassFive(self):
        print = "5"    
class Crisis:
    def __init__(self, ClassOne, ClassThree, ClassFive):
        self.ClassOne = ClassOne
        self.ClassThree = ClassThree
        self.ClassFive  = ClassFive
    def ClassOne(self):
        print = "3"
    def ClassThree(self):
        print = "5"
    def ClassFive(self):
        print = "7"
class War:
    def __init__(self, ClassOne, ClassThree, ClassFive):
        self.ClassOne = ClassOne
        self.ClassThree = ClassThree
        self.ClassFive = ClassFive
    def ClassOne(self):
        print = "5"
    def ClassThree(self):
        print = "7"
    def ClassFive(self):
        print = "9"
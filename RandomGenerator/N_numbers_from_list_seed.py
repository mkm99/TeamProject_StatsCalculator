# Select N number of items from a list with a seed

import random
from RandomGenerator.N_numbers_from_list import PickNumbersNoSeed

class PickNumbersSeed():
    @staticmethod
    def pickNumbers(theSeed, aList, rangeNum):
        random.seed(theSeed)

        try:
            aList[0]

        #size = len(aList)
        #if size == 0:
        #    return "list is empty?"

            newList = PickNumbersNoSeed.pickNumbers(aList, rangeNum)

            return newList

        except IndexError:
            return("list is empty")
#print(Pick_with_seed.pickNumbers(3, [34,45,67,89,123,44], 4))
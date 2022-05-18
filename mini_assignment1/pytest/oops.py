from collections import Counter
from itertools import combinations


class StringClass:
    def __init__(self, value):
        self.str = value

    def length(self):
        return len(self.str)

    def tolist(self):
        list1 = list(self.str)
        return list1


class PairsPossible(StringClass):

    def __init__(self, value):
        self.str = value

    def pairs(self):
        pair = list(combinations(self.str, 2))
        return pair


class SearchCommonElements(StringClass):
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2

    def commonElements(self):
        dict1 = Counter(set(self.str1))
        dict2 = Counter(set(self.str2))
        dict_final = dict(dict1.items() & dict2.items())
        commonEle = []
        for(key, val) in dict_final.items():
            for i in range(0, val):
                commonEle.append(key)
        return commonEle


class EqualSumPairs:
    def count(self, list1):
        list2 = []
        for i in list1:
            pairSum = 0
            for j in i:
                pairSum = pairSum + int(j)
            list2.append(pairSum)
        return len(set(list2))


value1 = input("Enter String: ")
stringclass = StringClass(value1)
print("{}{}".format("Length of the String: ", (stringclass.length())))
print("{}{}".format("List of String: ", stringclass.tolist()))


value2 = input("Enter String: ")
pairsPossible = PairsPossible(value2)
list1 = pairsPossible.pairs()
print("{}{}".format("Pairs Possible are: ", list1))


searchCommenElements = SearchCommonElements(value1, value2)
print("{}{}".format("Common Elements are: ", searchCommenElements.commonElements()))


equalSumPair = EqualSumPairs()
length = equalSumPair.count(list1)
print("{}{}".format("Count of unique sums: ", length))
print(length)

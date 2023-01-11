import random
from statistics import mean


class Cat:
    def __init__(self, name=""):
        # To match the expected format 100% of part 1, set the default value of name to empty string to match the
        # print output
        self.name = name
        self.age = random.randint(5, 10)
        self.favoriteFood = None
        # In 2.5, it's not clear if the default value should be recorded to the list of names if the cat name is not
        # specified. Did not record anything if the cat was initially not named as it seemed it may mess with the
        # expected result of part 2.8 getAverageNameLength()
        if name == "":
            self.names = []
        else:
            self.names = [name]
        self.timesSpoken = 0

    def getName(self):
        # To match the expected format 100%, need to return an empty string here if name is None
        if self.name is None:
            return ""
        return self.name

    def getAge(self):
        return self.age

    def getFavoriteFood(self):
        return self.favoriteFood

    def setName(self, newName):
        self.name = newName
        self.names.append(newName)

    def setAge(self, newAge):
        self.age = newAge

    def setFavoriteFood(self, newFavoriteFood):
        self.favoriteFood = newFavoriteFood

    def speak(self, sound="meow"):
        print(sound)
        self.timesSpoken += 1
        if self.shouldIncreaseAge():
            self.age += 1

    def getNames(self):
        return self.names

    def shouldIncreaseAge(self):
        return self.timesSpoken % 5 == 0

    def getAverageNameLength(self):
        if not self.names:
            return 0
        averageNameLength = mean([len(i) for i in self.names])
        return averageNameLength

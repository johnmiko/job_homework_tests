class Cat:
    def __init__(self):
        # To match the expected format 100%, set the default value of name to empty string to match the print output
        self.name = ""
        self.age = None
        self.favoriteFood = None

    # This is the more pythonic way, but matches the pseudocode less
    # def __init__(self, name=None, age=None, favoriteFood=None):
    #     self.name = name
    #     self.age = age
    #     self.favoriteFood = favoriteFood

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getFavoriteFood(self):
        return self.favoriteFood

    def setName(self, newName):
        self.name = newName

    def setAge(self, newAge):
        self.age = newAge

    def setFavoriteFood(self, newFavoriteFood):
        self.favoriteFood = newFavoriteFood

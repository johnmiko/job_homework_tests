import cProfile
import pstats

from cat import Cat
from data import Data
from dog import Dog


def saveTest():
    cat1 = Cat('Snuffaluffagus')
    data = Data("database")
    data.beginTran()
    data.insert("Cat", cat1)
    data.commit()

    dog1 = Dog('Deeoogee')
    data.beginTran()
    data.insert("Dog", dog1)
    data.commit()


def savePetShop():
    cats = [Cat()] * 3
    dogs = [Dog()] * 3

    data = Data("database")
    data.beginTran()
    # Assuming you can do a bulk insert
    data.bulkInsert("Cat", cats)
    # If bulk insert is unavailable
    # for cat in cats:
    #     data.insert("Cat", cat)
    # Assuming you can do a bulk insert
    data.bulkInsert("Dog", dogs)
    # If bulk insert is unavailable
    # for dog in dogs:
    #     data.insert("Dog", dog)
    data.commit()


def logStats():
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()


def main():
    saveTest()
    savePetShop()


# saveTest()
# savePetShop()
logStats()

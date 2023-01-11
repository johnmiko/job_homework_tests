from cat import Cat

from data import Data

cat = Cat()
print(f"Name is currently {cat.getName()}")

cat.setName("Garfield")
print(f"Name has been changed to {cat.getName()}")

data = Data("database")

data.insert("Cat", cat)

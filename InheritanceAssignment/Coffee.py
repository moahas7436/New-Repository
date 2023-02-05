class Coffee: 
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def get_name(self):
    return self.name

  def get_price(self):
    return self.price

class Starbucks(Coffee):
  def __init__(self, name, price, size, espresso):
    Coffee.__init__(self,name,price)
    self.size = size
    self.espresso = espresso

  def get_size(self):
    return self.size

  def get_espresso(self):
    return self.espresso

class Dunkin(Coffee):
  def __init__(self, name, price, sugar, milk):
    Coffee.__init__(self,name,price)
    self.sugar = sugar
    self.milk = milk

  def get_sugar(self):
    return self.sugar

  def get_milk(self):
    return self.milk

class TimHortons(Coffee):
  def __init__(self, name, price, location, flavor):
    Coffee.__init__(self,name,price)
    self.location = location
    self.flavor = flavor

  def get_location(self):
    return self.location

  def get_flavor(self):
    return self.flavor

def get_coffee():
  starbucks_coffee = Starbucks("Latte", 4.99, "Grande", 2)
  dunkin_coffee = Dunkin("Dunkaccino", 2.99, "Light", "Skim")
  tim_hortons_coffee = TimHortons("Dark Roast", 3.49, "Buffalo", "Mocha")
  return starbucks_coffee, dunkin_coffee, tim_hortons_coffee

starbucks_coffee, dunkin_coffee, tim_hortons_coffee = get_coffee()

print("Starbucks Coffee:")
print("Name:", starbucks_coffee.get_name())
print("Price:", starbucks_coffee.get_price())
print("Size:", starbucks_coffee.get_size())
print("Espresso:", starbucks_coffee.get_espresso())

print("\nDunkin Coffee:")
print("Name:", dunkin_coffee.get_name())
print("Price:", dunkin_coffee.get_price())
print("Sugar:", dunkin_coffee.get_sugar())
print("Milk:", dunkin_coffee.get_milk())

print("\nTim Hortons Coffee:")
print("Name:", tim_hortons_coffee.get_name())
print("Price:", tim_hortons_coffee.get_price())
print("Location:", tim_hortons_coffee.get_location())
print("Flavor:", tim_hortons_coffee.get_flavor())

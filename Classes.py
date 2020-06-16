class Person:
  gender="Male"
  bloodgroup="O"
  skincolor="Dark"

  def cough(self):
    return f"{self.name} is coughing"

  def walk(self):
    return f"{self.name} is walking"

  def sleep(self):
    return f"{self.name} is sleeping"

  def eat(self):
    return f"{self.name} is eating"

  def drinking(self):
    return f"{self.name} is drinking"

  def drunk(self):
    return f"{self.name} is now drunk"

obj1=Person()
obj2=Person()
x=Person()

x.gender="Female"
obj1.age="12"
obj2.age="13"
x.age="14"
obj1.height=1.5
obj1.weight=45
obj2.height=2.5
obj2.weight=46
x.height=1
x.weight=50

print(x.gender)
print(obj1.age)
print(obj2.age)
print(x.age)
print(obj1.height)
print(obj1.weight)
print(obj1.bloodgroup)
print(obj1.skincolor)
print(obj2.height)
print(obj2.weight)
print(obj2.bloodgroup)
print(obj2.skincolor)
print(x.height)
print(x.weight)
print(x.bloodgroup)
print(obj1.skincolor)


obj1.name="Fareed"
obj2.name="Irfaan"
x.name="Goodman"


print(obj1.cough())
print(obj1.eat())
print(obj2.walk())
print(obj2.eat())
print(x.sleep())
print(x.eat())
print(x.drinking())
print(x.drunk())














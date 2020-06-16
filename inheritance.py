# multiple inheritance
# class Parent:
#     def first(self):
#         print("FIRST METHOD")

# class Parent2:
#     def second(self):
#         print("SECOND METHOD")

# class Child(Parent,Parent2):
#     def third(self):
#         print("THIRD METHOD")

# ch = Child()





# class Parent:
#     def test(self):
#         print("testing method")

# class Child1(Parent):
#     def chil1_method(self):
#         print("I am from child one")

# class Child2(Parent):
#     def child2_method(self):
#         print("I am from child two")


'''class Vehicle:
    color = None
    wheel = None
    model = None

    def __init__(self,color,wheel,model):
        self.color = color
        self.wheel = wheel
        self.model = model

    def upgrade(self):
        return f"{self.model} is upgrading"

    def ignition(self):
        return f"{self.model} has been ignited"

car = Vehicle("Red",4,"Toyota")
lorry = Vehicle("Black", 6, "FAO")

class Subaru(Vehicle):
    turbo = False
    muffler = False
    make = None

    def __init__(self,make,model,color,wheel):
        self.make  = make
        super().__init__(color,wheel,model)

outback = Subaru("outback","Subaru","Blue",4)
print(outback.make)
print(outback.ignition())
print(outback.upgrade())'''

class BasicPlan:
	can_stream = True
	can_download = True
	num_of_devices = 1
	has_SD = True
	has_HD = False
	has_UHD = False
	price = '$8.99'

# Write the classes for StandardPlan and PremiumPlan here!
class StandardPlan(BasicPlan):

	can_stream = True
	can_download = True
	has_SD = True
	has_HD = True
	has_UHD = False
	num_of_devices = 2
	price = '$12.99'

class PremiumPlan(BasicPlan):
	can_stream = True
	can_download = True
	has_SD = True
	has_HD = True
	has_UHD = True
	num_of_devices = 4
	price = '$15.99'





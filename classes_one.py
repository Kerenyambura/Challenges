class Building:

#a constructor is a special method that will be called when an instance/object is created

  def __init__(self,name,tr,oc,sg):
    self.name=name
    self.total_rooms=tr
    self.occupied_rooms=oc
    self.security_guards=sg

  def computevacantrooms(self):
    return self.total_rooms-self.occupied_rooms




b1=Building("Corner House",100,25,10)
b2=Building("Anniversary Towers",150,82,27)

#b1.name="Corner House"
#b2.name="Anniversary Towers"
print(b1.name)
print(b1.total_rooms)
print(b1.security_guards)
print(b2.name)
print(b1.computevacantrooms())

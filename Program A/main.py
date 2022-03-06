from Vehicle import Vehicle
from Ship import Ship
from Airplane import Airplane

#Inisialisi kelas Vehicle dan pengisian data dummy
print("[Class: Vehicle]")
vehicle1 = Vehicle()
vehicle1.setFuelType("Pertamax")
vehicle1.setMaxPassanger(10)
vehicle1.move()
vehicle1.printData()

vehicle2 = Vehicle()
vehicle2.setFuelType("Solar")
vehicle2.setMaxPassanger(20)
vehicle2.move()
vehicle2.move()
vehicle2.printData()

vehicle3 = Vehicle()
vehicle3.setFuelType("Electric")
vehicle3.setMaxPassanger(30)
vehicle3.move()
vehicle3.move()
vehicle3.move()
vehicle3.printData()

vehicle4 = Vehicle()
vehicle4.setFuelType("Nuclear")
vehicle4.setMaxPassanger(40)
vehicle4.move()
vehicle4.move()
vehicle4.move()
vehicle4.move()
vehicle4.printData()

vehicle5 = Vehicle()
vehicle5.setFuelType("Orginium")
vehicle5.setMaxPassanger(50)
vehicle5.move()
vehicle5.move()
vehicle5.move()
vehicle5.move()
vehicle5.move()
vehicle5.printData()

#Inisialisi kelas Ship dan pengisian data dummy
print(" ")
print("[Class: Ship]")
ship1 = Ship()
ship1.setFuelType("Pertamax")
ship1.setMaxPassanger(10)
ship1.move()
ship1.setAge(1)
ship1.setType("Submarine")
ship1.setCountryOfManufacture("Indonesia")
ship1.printData()

ship2 = Ship()
ship2.setFuelType("Solar")
ship2.setMaxPassanger(20)
ship2.move()
ship2.move()
ship2.setAge(2)
ship2.setType("Hovercraft")
ship2.setCountryOfManufacture("Germany")
ship2.printData()

ship3 = Ship()
ship3.setFuelType("Electric")
ship3.setMaxPassanger(30)
ship3.move()
ship3.move()
ship3.move()
ship3.setAge(3)
ship3.setType("Water Drone")
ship3.setCountryOfManufacture("USA")
ship3.printData()

ship4 = Ship()
ship4.setFuelType("Nuclear")
ship4.setMaxPassanger(40)
ship4.move()
ship4.move()
ship4.move()
ship4.move()
ship4.setAge(4)
ship4.setType("Warship")
ship4.setCountryOfManufacture("Russia")
ship4.printData()

ship5 = Ship()
ship5.setFuelType("Orginium")
ship5.setMaxPassanger(50)
ship5.move()
ship5.move()
ship5.move()
ship5.move()
ship5.move()
ship5.setAge(5)
ship5.setType("Landship")
ship5.setCountryOfManufacture("Rim Billiton")
ship5.printData()

#Inisialisi kelas Airplane dan pengisian data dummy
print(" ")
print("[Class: Airplane]")
airplane1 = Airplane()
airplane1.setFuelType("Pertamax")
airplane1.setMaxPassanger(10)
airplane1.move()
airplane1.setAge(1)
airplane1.setType("Piston Aircraft")
airplane1.setWingsLength(1)
airplane1.printData()

airplane2 = Airplane()
airplane2.setFuelType("Solar")
airplane2.setMaxPassanger(20)
airplane2.move()
airplane2.move()
airplane2.setAge(2)
airplane2.setType("jets")
airplane2.setWingsLength(2)
airplane2.printData()

airplane3 = Airplane()
airplane3.setFuelType("Electric")
airplane3.setMaxPassanger(30)
airplane3.move()
airplane3.move()
airplane3.move()
airplane3.setAge(3)
airplane3.setType("RC Airplane")
airplane3.setWingsLength(3)
airplane3.printData()

airplane4 = Airplane()
airplane4.setFuelType("Nuclear")
airplane4.setMaxPassanger(40)
airplane4.move()
airplane4.move()
airplane4.move()
airplane4.move()
airplane4.setAge(4)
airplane4.setType("Fighter")
airplane4.setWingsLength(4)
airplane4.printData()

airplane5 = Airplane()
airplane5.setFuelType("Orginium")
airplane5.setMaxPassanger(50)
airplane5.move()
airplane5.move()
airplane5.move()
airplane5.move()
airplane5.move()
airplane5.setAge(5)
airplane5.setType("Stealth")
airplane5.setWingsLength(5)
airplane5.printData()
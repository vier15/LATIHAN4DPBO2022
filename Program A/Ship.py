from Vehicle import Vehicle

class Ship(Vehicle):

    #private attributes
    __age = 0
    __type = "Type"
    __countryOfManufacture = "Country of Manufacture"

    #Constructor
    def __init__(self, age = 0, type = "Type", countryOfManufacture = "Country of Manufacture"):
        self.__age = age
        self.__type = type
        self.__countryOfManufacture = countryOfManufacture
    
    #Setter dan Getter Age
    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    #Setter dan Getter Type
    def setType(self, type):
        self.__type = type

    def getType(self):
        return self.__type

    #Setter dan Getter Country of Manufacture
    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture

    def getCountryOfManufacture(self):
        return self.__countryOfManufacture

    #Method print
    def printData(self):
        print("_______________________________________")
        print("Fuel Type : " + str(self.getFuelType()))
        print("Max Passangers : " + str(self.getMaxPassanger()))
        print("Traveled Distance : " + str(self.getTravelDistance()) + "km")
        print("")
        print("Age : " + str(self.getAge()) + " years")
        print("Type : " + str(self.getType()))
        print("Country of Manufacturer : " + str(self.getCountryOfManufacture()))
        print("")
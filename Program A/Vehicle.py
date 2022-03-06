class Vehicle():

    #private attributes
    __fuelType = "Fuel Type"
    __maxPassangers = 0
    __travelDistance = 0

    #Constructor
    def __init__(self, fuelType = "Fuel Type", maxPassanger = 0, travelDistance = 0):
        self.__fuelType = fuelType
        self.__maxPassangers = maxPassanger
        self.__travelDistance = travelDistance

    #Setter dan Getter Fuel Type
    def setFuelType(self, fuelType):
        self.__fuelType = fuelType

    def getFuelType(self):
        return self.__fuelType

    #Setter dan Getter Max Passanger
    def setMaxPassanger(self, maxPassanger):
        self.__maxPassangers = maxPassanger

    def getMaxPassanger(self):
        return self.__maxPassangers
    
    #Setter dan Getter Traveled Distance
    def setTravelDistance(self, travelDistance):
        self.__travelDistance = travelDistance

    def getTravelDistance(self):
        return self.__travelDistance

    #Method Move untuk menggerakan Vehicle yang nantinya akan menambah Travel Distance
    def move(self):
        self.__travelDistance += 1

    #Method print
    def printData(self):
        print("_______________________________________")
        print("Fuel Type : " + str(self.getFuelType()))
        print("Max Passangers : " + str(self.getMaxPassanger()))
        print("Traveled Distance : " + str(self.getTravelDistance()) + "km")
        print("")

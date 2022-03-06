from Vehicle import Vehicle

class Airplane(Vehicle):

    #private attributes
    __age = 0
    __type = "Type"
    __wingsLength = 0

    #Constructor
    def __init__(self, age = 0, type = "Type", wingsLength = 0):
        self.__age = age
        self.__type = type
        self.__wingsLength = wingsLength
    
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

    #Setter dan Getter Wings Length
    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    def getWingsLength(self):
        return self.__wingsLength

    #Method print
    def printData(self):
        print("_______________________________________")
        print("Fuel Type : " + str(self.getFuelType()))
        print("Max Passangers : " + str(self.getMaxPassanger()))
        print("Traveled Distance : " + str(self.getTravelDistance()) + "km")
        print("")
        print("Age : " + str(self.getAge()) + " years")
        print("Type : " + str(self.getType()))
        print("Wings Length : " + str(self.getWingsLength()) + "m")
        print("")
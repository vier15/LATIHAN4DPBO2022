from Person import Person
from Job import Job

class Driver(Person, Job):

    #private attributes
    __lisenceId = "Lisence ID"
    __activeUntil = "Active Until"
    __vehicleType = "Vehicle Type"

    #Constructor
    def __init__(self, lisenceId = "Lisence ID", activeUntil = "Active Until", vehicleType = "Vehicle Type"):
        self.__lisenceId = lisenceId
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    #Setter dan Getter Lisence ID
    def setLisenceId(self, lisenceId):
        self.__lisenceId = lisenceId

    def getLisenceId(self):
        return self.__lisenceId

    #Setter dan Getter Active Until
    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def getActiveUntil(self):
        return self.__activeUntil
    
    #Setter dan Getter Vehicle Type
    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    def getVehicleType(self):
        return self.__vehicleType

    #Method print
    def printData(self):
        print("__________________________________________________")
        print("NIK : " + str(self.getNik()))
        print("Name : " + str(self.getName()))
        print("Gender : " + str(self.getGender()))
        print("")
        print("NIP : " + str(self.getNip()))
        print("Company Name : " + str(self.getCompanyName()))
        print("Position : " + str(self.getPosition()))
        print("")
        print("Lisence ID : " + str(self.getLisenceId()))
        print("Active Until : " + str(self.getActiveUntil()))
        print("Vehicle Type : " + str(self.getVehicleType()))
        print("")
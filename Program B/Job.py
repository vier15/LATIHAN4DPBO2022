class Job():

    #private attributes
    __nip = "NIP"
    __companyName = "Company Name"
    __position = "Position"

    #Constructor
    def __init__(self, nip = "NIP", companyName = "Company Name", position = "Position"):
        self.__nip = nip
        self.__companyName = companyName
        self.__position = position

    #Setter dan Getter NIP
    def setNip(self, nip):
        self.__nip = nip

    def getNip(self):
        return self.__nip

    #Setter dan Getter Company Name
    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def getCompanyName(self):
        return self.__companyName
    
    #Setter dan Getter Position
    def setPosition(self, position):
        self.__position = position

    def getPosition(self):
        return self.__position

    #Method print
    def printData(self):
        print("__________________________________________________")
        print("NIP : " + str(self.getNip()))
        print("Company Name : " + str(self.getCompanyName()))
        print("Position : " + str(self.getPosition()))
        print("")
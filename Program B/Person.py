class Person():

    #private attributes
    __nik = "NIK"
    __name = "Name"
    __gender = "Gender"

    #Constructor
    def __init__(self, nik = "NIK", name = "Name", gender = "Gender"):
        self.__nik = nik
        self.__name = name
        self.__gender = gender

    #Setter dan Getter NIK
    def setNik(self, nik):
        self.__nik = nik

    def getNik(self):
        return self.__nik

    #Setter dan Getter Name
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name
    
    #Setter dan Getter Gender
    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    #Method Sleep agar orang ini tidur saat sudah malam
    def sleep(self):
        print("[sleep() called! This person will sleep at night~]")
        print("")

    #Method print
    def printData(self):
        print("__________________________________________________")
        print("NIK : " + str(self.getNik()))
        print("Name : " + str(self.getName()))
        print("Gender : " + str(self.getGender()))
        print("")
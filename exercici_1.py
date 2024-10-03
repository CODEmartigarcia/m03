class Pare():
    def __init__(self, firstName="García", lastName="Sabaté", Name="Enric"):
        self.cognom1pare = firstName
        self.cognom2pare = lastName
        self.nompare = Name

# self.__firstname...
    def getDadFirstName(self):
        return(self.cognom1pare)
    def getDadFullName(self):
        return(f'El nom complet del meu pare és {self.nompare} {self.cognom1pare} {self.cognom2pare}')
# jose = Pare()
# print(jose.getDadFullName())

class Mare():
    def __init__(self, firstName="Llambrich", lastName="Belvis", Name="Yolanda"):
        self.cognom1mare = firstName
        self.cognom2mare = lastName
        self.nommare = Name
    def getMomFirstName(self):
        return(self.cognom1mare)
    def getMomFullName(self):
        return(f'El nom complet de la meva mare és {self.nommare} {self.cognom1mare} {self.cognom2mare}')

class Fill(Pare, Mare):
    def __init__(self, name):
        Pare.__init__(self)
        Mare.__init__(self)
        self.name = name

    def getFullName(self):
        return(f'El meu nom complert és {self.name} {self.getDadFirstName()} {self.getMomFirstName()}')


# dad_first_name, dad_last_name, dad_name... mateix en mare

Marti = Fill("Marti")
print(Marti.getFullName())
print(Marti.getDadFullName())
print(Marti.getMomFullName())

# print(jose.nom)


# class Mare():

# class Fill():






































# class Pare():
#     def __init__(self, dadFirstName, dadLastName, dadName):
#         self.dadFirstName = dadFirstName
#         self.dadLastName = dadLastName
#         self.dadName = dadName
#     def getDadFirstName(self):
#         print(self.dadFirstName)
#     def getDadFullName(self):
#         print(f'{self.dadName} {self.dadFirstName} {self.dadLastName}')
# class Mare():
#     def __init__(self, momFirstName, momLastName, momName):
#         self.momFirstName = momFirstName
#         self.momLastName = momLastName
#         self.momName = momName
#     def getMomFirstName(self):
#         print(self.momFirstName)
#     def getMomFullName(self):
#         print(f'{self.momName} {self.momFirstName} {self.momLastName}')

# class Child(Pare, Mare):
#     def __init__(self, name, dadFirstName, dadLastName, momFirstName, momLastName):
#         Pare.__init__(self, dadFirstName, dadLastName, name)
#         Mare.__init__(self, momFirstName, momLastName, name)
#         self.name = name
#     def getFullName(self):
#         print(f'El meu nom és {self.name}')



# pare = Pare("Garcia", "Sabaté", "Enrique") 
# mare = Mare("Llambrich", "Belvis", "Yolanda") 
# fill = Child("Martí")
# print(fill.getFullName())
# print(pare.getDadFullName())
# print(mare.getMomFullName())

















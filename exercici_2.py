# Test Output:
# #Test Input
# c1 = Candidate('Manel', 'Cantells','male')
# c1.add_ability('JavaScript')
# c1.add_ability('Python')
# c2 = Candidate('Maria', 'Gironés','female')
# c2.add_ability('PHP')
# #Test Output
# He is Manel Cantells.
# ['JavaScript', 'Python']
# She is Maria Gironés.
# ['PHP']
# * * Observacions: El camp abilities és un array on s’han de poder afegir destreses de les
# persones.
# Noteu també que al crear un candidat s’especifica el gènere d’aquest de tal forma que al
# mostrar el seu nom (mètode info()) posa el pronom corresponen


class Person():
    def __init__(self, nom, cognom):
        self.nom = nom
        self.cognom = cognom
        self.abilities = []
    def add_ability(self, skill):
        self.abilities.append(skill)
        # print(self.abilities) 
    # def info(self):
    #     print(f'{gender}')
class Candidate(Person):
    def __init__(self, nom, cognom, gender):
        Person.__init__(self,nom, cognom)
        self.gender = gender
    def info(self):
        if self.gender == "male":
            print(f'He is {self.nom} {self.cognom}')
        else:
            print(f'She is {self.nom} {self.cognom}')
        return(self.abilities)

        



c1 = Candidate('Manel', 'Cantells','male')
c1.add_ability('JavaScript')
c1.add_ability('Python')
c2 = Candidate('Maria', 'Gironés','female')
c2.add_ability('PHP')

print(c1.info())
print(c2.info())

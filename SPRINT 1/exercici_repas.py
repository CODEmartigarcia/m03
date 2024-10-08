# Crear una classe del tipus "Animal" i dues més del tipus "Gat" i "Ós" 
# en fitxers python independents. 
# Declarar els atributs i les funcions generals de la classe "Animal". 
# Funcions com ara "menjar", "dormir", "caçar" i atributs com ara pes, edat, 
# si és amfibi i temps mitjà de vida.
# Partint de l'estructura anterior i aplicant el principi d'Herència en POO, 
# crear 1 objecte del tipus "Gat" i un altre de tipus "Ós" amb dades arbitràries, 
# inserir ambdós elements en una tupla, recórrer aquesta tupla i pintar 
# per pantalla els valors dels objectes esmentats.

class Animal():
    def __init__(self, pes, altura, anfibi, mortAproximada, salut, atac, potes ="4", ) :  # aixi practico deixar valors predefinits
        self.pes = pes
        self.altura = altura
        self.esAnfibi = bool(anfibi)
        self.quanMor = mortAproximada
        self.edat = 1
        self.potes = potes
        self.atac = atac
        self.salut = salut
        self.max_salut = salut
        self.honor = 0 

    def menjar(self):
        self.tiktak()
        print(f'Tens {self.edat} anys... Et queden {self.quanMor - self.edat} anys de vida')
        self.atac += 1.05
        return (f'He menjat! Atac +1')
    
    def dormir(self):
        self.tiktak()
        self.salut = self.max_salut
        if self.salut > self.max_salut:
            self.salut = self.max_salut
        print(f'He dormit')
        
    def caçar(self):
        self.tiktak()
        self.salut -= 20
        self.honor += self.atac
        print(f'Tens {self.honor} punts d\'honorable!')
        if(self.salut <= 0):
            print(f'Has mort! Has fet {self.honor} punts d\'honorable!')
            exit()
    def tiktak(self):
        print(f'Tens {self.edat} anys... Et queden {self.quanMor - self.edat} anys de vida')
        if self.pes > 0 and self.pes < 2000:
            self.edat += 1
        elif self.pes > 2000 and self.pes < 15000: 
            self.edat += 20
        else:
            self.edat += 1000
        if self.edat > self.quanMor:
            print('Has mort de vell')
            print(f'Has fet {self.honor} punts d\'honorable!')
            exit()
    def stats(self):
        print(f'Salut: {self.salut}/{self.max_salut}\n Atac: {self.atac}\n')
# Torete = Animal(30,150,20,False,40,50,10,)
# while True:
# print(Torete.caçar())   2
# print(Torete.caçar())   

# print(Torete.salut)   
class Gat(Animal):
    def __init__(self):
        Animal.__init__(self, pes=1200, altura=25, anfibi=False, mortAproximada=15, salut=100, atac=7, potes="4")
class Tortuga(Animal):
    def __init__(self):
        Animal.__init__(self, pes=10000, altura=15, anfibi=False, mortAproximada=400, salut=2000, atac=7, potes="4")
    def caçar(self):
        self.tiktak()
        self.salut -= 0 
        self.honor += self.atac / 3.41
        print(f'Tens {self.honor} punts d\'honorable!')
        if self.salut <= 0:
            print(f'Has mort! Has fet {self.honor} punts d\'honorable! Tukukutuko es resistent!')
            exit()
    def menjar(self):
        self.tiktak()
        print(f'Tens {self.edat} anys... Et queden {self.quanMor - self.edat} anys de vida')
        self.atac += 3
        return (f'He menjat! Atac +50')        
class Larix(Animal):
    def __init__(self):
        Animal.__init__(self, pes=243500, altura=352000, anfibi=False, mortAproximada=20300, salut=100, atac=1, potes="4")
    def caçar(self):
        self.tiktak()
        self.salut -= 10 
        self.honor += self.atac / 10
        print(f'Tens {self.honor} punts d\'honorable!')
        if self.salut <= 0:
            print(f'Has mort! Has fet {self.honor} punts d\'honorable! Però Larix és un gran guerrer!')
            exit()    
    def menjar(self):
        self.tiktak()
        print(f'Tens {self.edat} anys... Et queden {self.quanMor - self.edat} anys de vida')
        self.atac += 10
        return (f'He menjat! Atac +10') 
## EXERCICI BASE
kato = Gat()
tortuko = Tortuga()

tupla = (kato, tortuko)
for animal in tupla:
    print("Estadistiques:")
    print(f"Edat: {animal.edat}")
    print(f"Pes: {animal.pes}")
    print(f"Altura: {animal.altura}")
    print(f"Salut: {animal.salut}/{animal.max_salut}")
    print(f"Atac: {animal.atac}")
    print(f"Honor: {animal.honor}")
    print(f"Es Anfibi: {animal.esAnfibi}")
    print(f"Temps de vida aproximada: {animal.quanMor}")
    print("--------\n")

### JOC A PART
# TRIAR PJ!
print(" 1. Gat \n 2. Tortuga. \n 3. Larix")
character = input('Quin animal vols ser?')
match character:
    case "1":
        personatge_actual = Gat()
        name = 'Katow!'
        print('El gat és el personatge més agressiu, viu menys temps, però pot fer molts punts ràpidament.')
    case "2":
        personatge_actual = Tortuga()
        name = 'Tortoinso'
        print('La tortuga és el personatge bastant passiva, te marge de vida i quasi no ha de descansar.')

    case "3":
        personatge_actual = Larix()    
        name = 'Arboriko'
        print('Larix és un arbre mil·lenari, perd vida però té moltíssims anys de vida.')
print('El joc consisteix en fer 100 punts d\'honorable. \n Menjes per a ser més fort. Dorms per a curar-te. Caçes per guanyar punts.')
while True:
    print(" 1. Menjar \n 2. Dormir. \n 3. Caçar")
    accio = input(f'Hola {name}, Quina accio vols realitzar')    
    
    match accio:
        case "1":
            personatge_actual.menjar()
        case "2":
            personatge_actual.dormir()
        case "3":
            personatge_actual.caçar()
        case "0":
            print('Vull sortir del joc!')
            exit()
    personatge_actual.stats()



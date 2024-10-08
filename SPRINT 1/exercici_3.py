## PROGRAMA COMPTES BANC!
class Compte():
    def __init__(self, nom, telefon, mail, diners):
        self.client = nom
        self.telefon = telefon
        self.mail = mail
        self.diners = diners
    def dades(self):
        print(f'INFORMACIÓ DEL CLIENT 🧔 {self.client}\n Telèfon: {self.telefon}\n Correu electrònic: {self.mail}\n Quantitat de diners al banc: {self.diners}')
class Fixe(Compte):
    def __init__(self, nom, telefon, mail, diners, plaç, interes):
        Compte.__init__(self, nom, telefon, mail, diners)
        self.plaç = plaç
        self.interes = interes
    def import_interes(self):
        self.interestotal = (self.diners * self.interes) / 100
        self.total = self.interestotal + self.diners
    def info(self):
        print(f'{self.client}, {self.plaç}, {self.interes}, {self.total}')

class Estalvi(Compte):
    def __init__(self, nom, telefon, mail, diners):
        Compte.__init__(self, nom, telefon, mail, diners)
    def mostrarEstalvis(self):
        print(f'Tens {self.diners} estalviats')

clients = []
# ACCIONS A FER
def client_agregar():
    opcions = input(" 1 = Compte Fixe, \n 2 = Compte Estalvi")
    if opcions == "1":
        nom = input("Nom: ")
        while True:
            telefon = input("Telèfon: ")
            if len(telefon) == 9 and telefon.isdigit():
                telefon = int(telefon)  #posarlo 
                break
            else:
                print("El telèfon ha de ser de 9 dígits i solament s'accepten números.")
        
        mail = input("Mail: ")
        while True:
            try:
                diners = float(input("Diners: ")) 
                if diners >= 0:
                    break
                else:
                    print("El valor ha de ser major o igual a 0")
            except:
                print("El valor ha de ser un nombre amb o sense decimals.")
                
        while True:
            try:
                plaç = int(input("Plaç"))
                if plaç >= 0:
                    break
                else:
                    print("El plaç no pot ser negatiu")
            except:
                print("El valor ha de ser un int")
        while True:
            try:
                interes = float(input("Intères"))
                break
            except:
                print("El valor ha de ser un float")
        nou_client = Fixe(nom, telefon, mail, diners, plaç, interes)
        clients.append(nou_client)

    elif opcions == "2":
        nom = input("Nom")
        while True:
            telefon = input("Telèfon: ")
            if len(telefon) == 9 and telefon.isdigit():
                telefon = int(telefon)  #posarlo 
                break
            else:
                print("El telèfon ha de ser de 9 dígits i solament s'accepten números.")
        
        mail = input("Mail: ")
        while True:
            try:
                diners = float(input("Diners: ")) 
                if diners >= 0:
                    break
                else:
                    print("El valor ha de ser major o igual a 0")
            except:
                print("El valor ha de ser un nombre amb o sense decimals.")
        nou_client = Estalvi(nom, telefon, mail, diners)
        clients.append(nou_client)
    else:
        return   

def client_llistar():
    if not clients:
        print("No hi ha clients")
    else:
        for client in clients:
            client.dades()

def plaç_fix_estalviat(client):
        if isinstance(client, Estalvi):
          client.mostrarEstalvis()
        elif isinstance(client, Fixe):
          client.import_interes()
          client.info()
        else:
            return "Aquest client no té cap compte."
def buscar_client():
    busqueda = input("Pots donar-me el nom del client?").casefold()
    for client in clients:
        if client.client.casefold() == busqueda:
            return client
    else :
        return "Client no trobat."
def modificar_client():
    client_llistar()
    victima = input("Quin client vols modificar?").casefold()
    for client in clients:
        if client.client.casefold() == victima:
            client.client = input("Nom nou: ")
            
            while True:
                client.telefon = input("Telèfon nou: ")
                if len(client.telefon) == 9 and client.telefon.isdigit():
                    client.telefon = int(client.telefon) 
                    break
                else:
                    print("El telèfon ha de ser de 9 dígits i solament s'accepten números.")
        client.mail = input("Mail nou: ").casefold()
        while True:
            # try:
                diners = float(input("Diners nous: ")) 
                if diners >= 0 and diners != str:
                    client.diners = diners                    
                    break
                else:
                    print("El valor ha de ser major o igual a 0")           
        return
    else:
        print("Client no trobat.")

def eliminar_client():
    victima = input("Quin client vols eliminar?")
    for client in clients:
        if client.client == victima:
            clients.remove(client)
            print(f'El client {client.client} ha segut borrat correctament.')
            return
        else:
            print("Aquest client no existeix.")

# ELECCIÓ
while True:
    print(" 1. Agregar Client \n 2. Llistar els Clients. \n 3. Mostrar Fixe i Estalviat. \n 4. Buscar client. \n 5. Modificar client \n 6. Eliminar client. ")
    accio = input("Quina acció vols realitzar?")
    match accio:
        case "1":
            client_agregar()
        case "2":
            client_llistar()
        case "3":
            client = buscar_client()
            if isinstance(client, Compte):
                plaç_fix_estalviat(client)
            else:
                print(client)
        case "4":
            client = buscar_client()
            if isinstance(client, Compte):
                client.dades()
            else:
             print(client)
        case "5":
            modificar_client()
        case "6":
            eliminar_client()
        case "0":
            print("Sortint del programa.")
            break
        case _:
            print("Opció no vàlida, torna-ho a intentar.")     
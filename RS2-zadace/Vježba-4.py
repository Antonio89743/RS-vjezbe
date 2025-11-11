# Zadatak 1

from math import sqrt
from math import pi
from datetime import datetime

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraža):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraža = kilometraža

    def ispis(self):
        for atribut, vrijednost in self.__dict__.items():
                    print(f"  {atribut}: {vrijednost}")

    def starost(self):
        print(datetime.now().year - self.godina_proizvodnje)

a = Automobil("McLaren", "F1", 1996, 63125)
a.ispis()
a.starost()



# Zadatak 2

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b
    
    def oduzimanje(self):
        return self.a - self.b
    
    def mnozenje(self):
        return self.a * self.b
    
    def dijeljenje(self):
        return self.a / self.b
    
    def potenciranje(self):
        return self.a ** self.b

    def korijen(self, a):
        return sqrt(a)
    


# Zadatak 3

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene)

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = []

for student in studenti:
    objekt: Student = Student(student["ime"], student["prezime"], student["godine"], student["ocjene"])
    studenti_objekti.append(objekt)

najbolji_student: Student = max(studenti_objekti, key = lambda s: s.prosjek())



# Zadatak 4

class Krug:
    def __init__(self, r):
        self.r = r

    def povrsina(self):
        return pi * (self.r ** 2)

    def opseg(self):
        return 2 * pi * self.r
    
k: Krug = Krug(5)
print("Površina: ", k.povrsina())
print("Opseg: ", k.opseg())



# Zadatak 5

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department
    
    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")

    def give_raise(self, radnik: Radnik, povecanje: float):
        radnik.placa += povecanje

radnik: Radnik = Radnik("Ivan", "programer", 3000)
radnik.work()
print(radnik.placa)
manager: Manager = Manager("Ana", "voditelj projekta", 2500, "IT odjel")
manager.work()
manager.give_raise(radnik, 500)
print(radnik.placa)
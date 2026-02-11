"""Tambahkan Metode
Contoh
Tambahkan metode bernama welcomeke dalam Studentkelas:
"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2024)
x.welcome()

"""
Jika Anda menambahkan metode di kelas turunan dengan nama yang sama dengan fungsi di kelas induk, pewarisan metode induk akan ditimpa.
"""
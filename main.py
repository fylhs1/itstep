import random
class Human:
    def __init__(self,name="Human", job=None, home=None, car=None):
        self.name=name
        self.money=100
        self.gladness=50
        self.satienly=50
        self.job=job
        self.car=car
        self.home=home
    def get_home(self):
        pass
    def get_car(self):
        pass
    def get_job(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self, manage):
        pass
    def chill(self):
        pass
    def clean_home(self):
        pass
    def to_repair(self):
        pass
    def deys_indexes(self, dey):
        pass
    def is_alive(self):
        pass
    def live(self, dey):
class Auto:
    def __init__(self,brand):
        self.brand=brand
        self.passengers=[]
    def add_passengers(self,human):
        self.passengers.append(human)
    def print_passengers_names(self):
        if self.passengers!=[]:
            print(f"Names of{self.brand}passengers:")
            for passengers in self.passengers:
                print(passengers.name)
        else:
            print(f"There are passengers in {self.brand}")
anna=Human("Anna")
vika=Human("Vika")
car=Auto("Toyota")
car.add_passengers(anna)
car.add_passengers(vika)
car.print_passengers_names()
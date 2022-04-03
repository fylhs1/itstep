import random
class Student:
    def __init__(self, name):
        self.name = name
        self.money = 250
        self.gladness = 5.0
        self.progress = 0
        self.alive = True
    def to_stady(self):
        print("Time to stady")
        self.progress+=0.12
        self.gladness+=3
        self.money-=50
    def to_sleep(self):
        print("I will sleep")
        self.gladness+=3
        self.money-=30
    def to_chell(self):
        print("Rest time")
        self.gladness+=5
        self.progress-=0.1
        self.money-=100
    def to_work(self):
        print("go to work")
        self.gladness-=5
        self.money+=150
        self.progress-=0.2
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out....")
            self.alive = False
        elif self.gladness<=0:
            print("Depresion...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally..")
            self.alive = False
        elif self.money < 0:
            print("eat...")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness={self.gladness}")
        print(f"Progress={round(self.progress,2)}")
        print(f"money={round(self.money)}")
    def live(self, day):
        day = "Dey" + str(day) + "of" + self.name + "live"
        print(f"{day:=^50}")
        live_cybe= random.randint(1, 4)
        if live_cybe==1:
            self.to_stady()
        elif live_cybe==2:
            self.to_sleep()
        elif live_cybe==3:
            self.to_chell()
        elif live_cybe==4:
            self.to_work()
        self.end_of_day()
        self.is_alive()
nick=Student(name="Nick")
for day in range(365):
    if nick.alive==False:
        break
    nick.live(day)
class Person(object):
    def __init__(self, name, age, brain, legs):
        self.name = name
        self.age = age
        self.brain = brain
        self.legs = legs


    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job, uniform):
        self.name = name
        self.age = age
        self.job = job
        self.uniform = uniform


class Programmer(object):
    def __int__(self,name, age,)
        self.name = name
        self.age = age
        
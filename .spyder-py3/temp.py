# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Worker:
    def __init__(self,name,ID,salary):
        self.name = name
        self.ID = ID
        self.salary = salary

class Manager (Worker):
    def __init__ (self,name,ID,salary):
        Worker(name,ID,salary)
        self.workers = []
    def addWorker(self,worker):
        self.workers.append(worker)

ariel = Manager('Ariel','307863431',60000)
maayan = Worker ('Maayan','123',20000)
shoham = Worker ('Shoham','456',20000)

ariel.addWorker(maayan)
ariel.addWorker(shoham)

for worker in ariel.workers:
    print('Name:' + worker.name + ' ,ID:' + worker.ID + ' ,Salary:' + str(worker.salary))
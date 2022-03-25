from person import Person, Manager
import shelve

bob = Person('Bob Smith')
sue = Person('Sue Jones', 'dev', 100000)  # Автоматически выполняет__init__
tom = Manager('Tom Jones', 50000)
db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

import glob
print(glob.glob('person*'))
print(open('persondb.dir').read())
print(open('persondb.dat','rb').read ())

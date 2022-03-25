import shelve
# import person

db = shelve.open('persondb')
print('В базе', len(db), 'записи')
bob = db['Bob Smith']
print(bob.lastName())
for k in db:
    print(k, '=>', db[k])


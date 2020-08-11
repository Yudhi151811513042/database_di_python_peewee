from peewee import *
import random, datetime

sqlite_db = SqliteDatabase('pengguna.db')

class Pengguna(Model):
    username = CharField()
    point = IntegerField()
    join_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = sqlite_db

sqlite_db.connect()
sqlite_db.create_tables([Pengguna], safe=True)

#hitung jumlah data
#print(Pengguna.select().count())

users = Pengguna.select().paginate(2,2)

for user in users:
    print(user.username)

#users = Pengguna.select().order_by(Pengguna.point.desc())

#for user in users:
#    print(user.username) + ' ' + str(user.point)
"""
user = Pengguna.select().where(Pengguna.username == 'yudhi').get()
user.username = 'yudhirangga'
user.save()

user.update(point = 100).where(Pengguna.username == 'rangga').execute()
"""

'''
def get_rand():
    return random.randint(1,100)

data = [
    {'username': 'yudhi', 'point': get_rand()},
    {'username': 'rangga', 'point': get_rand()},
    {'username': 'boy', 'point': get_rand()},
    {'username': 'masta', 'point': get_rand()}
]

Pengguna.insert_many(data).execute()
'''
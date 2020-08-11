from peewee import *

sqlite_db = SqliteDatabase('user.db')

class User(Model):
    name = CharField()
    email = CharField()

    class Meta:
        database = sqlite_db

sqlite_db.connect()
sqlite_db.create_tables([User], safe=True)

#insert data
#User.create(name='test', email='test@test.test')

#user = User(name='test2', email='test2@test.test')
#user.save()

#print(User.insert(name='test3', email='test3@test.test').execute())

'''data_source =[
    {'name':'test4', 'email':'test4@test.test'},
    {'name':'test5', 'email':'test5@test.test'}
]

print(User.insert_many(data_source).execute()) '''
'''
data = [
    {'test6','test6@test.test'},
    {'test7','test7@test.test'}
]
fields = [User.name, User.email]

User.insert_many(data, validate_fields=Field).execute()

'''
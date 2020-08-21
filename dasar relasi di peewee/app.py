import datetime
from peewee import *

sqlite_db = SqliteDatabase('tweet.db')

class BaseModel(Model):
    class Meta:
        database = sqlite_db

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    message = TextField()
    create_date = DateTimeField(default=datetime.datetime.now)
    user = ForeignKeyField(User, backref='tweets')

'''query = Tweet.select().join(User)
for tweet in query:
    print(tweet.message)'''

yudhitweet = User.get(User.username=='yudhi')
for tweet in yudhitweet.tweets:
    print(tweet.message)


'''sqlite_db.create_tables([User, Tweet])

data = (
    ('yudhi', ('halo tweet', 'ini tweet kedua saya')),
    ('rangga', ('apa kabar dunia', 'selamat makan')),
    ('boy', ('hatiku hancur', 'aku tak berdaya'))
)

for username, tweets in data:
    user = User.create(username = username)
    for tweet in tweets:
        Tweet.create(user=user, message=tweet)'''
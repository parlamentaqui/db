import os
from mongoengine import *
from dotenv import load_dotenv
from random import randrange
from datetime import timedelta
from datetime import datetime

def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('1/1/2019 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2021 4:50 AM', '%m/%d/%Y %I:%M %p')

load_dotenv()

DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

connect(DB_NAME, host=f'mongodb://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?authSource=admin')

####### Models #######

class Deputy(Document):
    id = IntField(primary_key=True)
    name = StringField(required=True)
    photo_url = StringField()
    initial_legislature_id = IntField(required=True)
    final_legislature_id = IntField()
    initial_legislature_year = IntField(required=True)
    final_legislature_year = IntField()
    last_activity_date = DateTimeField()
    full_name = StringField()
    sex = StringField()
    email = StringField()
    birth_date = DateTimeField()
    death_date = DateTimeField()
    federative_unity = StringField()
    party = StringField()
    instagram_username = StringField()
    twitter_username = StringField()
    facebook_username = StringField()

class News(Document):
    id = IntField(primary_key=True)
    deputy_id = IntField()
    link = StringField()
    photo = StringField()
    title = StringField()
    abstract = StringField()
    deputy_name = StringField()
    update_date = DateTimeField()
    source = StringField()

class Tweet(Document):
    tweet_id = IntField(primary_key=True)
    deputy_id = IntField()
    name = StringField()
    twitter_username = StringField()
    date = DateTimeField()

####### Populate #######


populate_deputy_1 = Deputy(
    id=1, 
    name="Fepas do LoL",
    photo_url= "https://avatars.githubusercontent.com/u/29442029?v=4",
    initial_legislature_id=1,
    final_legislature_id=1,
    initial_legislature_year=2021,
    final_legislature_year=2021,
    last_activity_date=random_date(d1, d2),
    full_name="Felipe Campos",
    sex="M",
    email= "fepas@parlamentaqui.com",
    birth_date=random_date(d1, d2),
    death_date=random_date(d1, d2),
    federative_unity="GO",
    party="LOL",
    instagram_username="instafepasdolol",
    twitter_username="twitterfepasdolol",
    facebook_username="facefepasdolol"
).save() 

populate_deputy_2 = Deputy(
    id=2,
    name="Lyra dos Video Juegos",
    photo_url= "https://avatars.githubusercontent.com/u/38503082?v=4",
    initial_legislature_id=1,
    final_legislature_id=1,
    initial_legislature_year=2021,
    final_legislature_year=2021,
    last_activity_date=random_date(d1, d2),
    full_name="João Pedro Lyra",
    sex="M",
    email= "lyra@parlamentaqui.com",
    birth_date=random_date(d1, d2),
    death_date=random_date(d1, d2),
    federative_unity="DF",
    party="GAMES",
    instagram_username="instalyravideojuegos",
    twitter_username="twitterlyravideojuegos",
    facebook_username="facelyravideojuegos"
).save() 

populate_deputy_3 = Deputy(
    id=3, 
    name="Cici do Ifood",
    photo_url= "https://avatars.githubusercontent.com/u/58526599?v=4",
    initial_legislature_id=1,
    final_legislature_id=1,
    initial_legislature_year=2021,
    final_legislature_year=2021,
    last_activity_date=random_date(d1, d2),
    full_name="Cibele Goudinho",
    sex="F",
    email= "cibele@parlamentaqui.com",
    birth_date=random_date(d1, d2),
    death_date=random_date(d1, d2),
    federative_unity="DF",
    party="IFOOD",
    instagram_username="instacicidoifood",
    twitter_username="twittercicidoifood",
    facebook_username="facecicidoifood",
).save()

populate_tweet_1 = Tweet(
    tweet_id=1,
    deputy_id=1,
    name="Fepas do LoL",
    twitter_username="twitterfepasdolol",
    date=random_date(d1, d2)).save()

populate_tweet_2 = Tweet(
    tweet_id=2,
    deputy_id=2,
    name="Fepas do LoL",
    twitter_username="twitterfepasdolol",
    date=random_date(d1, d2)).save()

populate_tweet_3 = Tweet(
    tweet_id=3,
    deputy_id=3,
    name="Fepas do LoL",
    twitter_username="twitterfepasdolol",
    date=random_date(d1, d2)).save()

populate_tweet_4 = Tweet(
    tweet_id=4,
    deputy_id=4,
    name="Fepas do LoL",
    twitter_username="twitterfepasdolol",
    date=random_date(d1, d2)).save()

populate_tweet_5 = Tweet(
    tweet_id=5,
    deputy_id=5,
    name="Cici do Ifood",
    twitter_username="twittercicidoifood",
    date=random_date(d1, d2))

populate_tweet_6 = Tweet(
    tweet_id=6,
    deputy_id=6,
    name="Cici do Ifood",
    twitter_username="twittercicidoifood",
    date=random_date(d1, d2)).save()

populate_tweet_7 = Tweet(
    tweet_id=7,
    deputy_id=7,
    name="Lyra dos Video Juegos",
    twitter_username="twitterlyradosvideojuegos",
    date=random_date(d1, d2)).save()


populate_news_1 = News(
    id=1,
    deputy_id=3,
    link="https://g1.globo.com/planeta-bizarro/noticia/2019/09/04/cici-do-ifood-aparece-no-casamento-da-irma-fantasiada-de-tiranossauro-nos-eua.ghtml",
    photo="https://avatars.githubusercontent.com/u/58526599?v=4",
    title="Cici do Ifood aparece no casamento da irmã fantasiada de tiranossauro nos eua",
    abstract="eh isso mesmo q vc leu otaria",
    deputy_name="Cici do Ifood",
    update_date=random_date(d1, d2),
    source="g1.globo.com"
).save()

populate_news_2 = News(
    id=2,
    deputy_id=3,
    link="https://g1.globo.com/planeta-bizarro/noticia/2019/09/04/gato-de-cici-do-ifood-e-preso-suspeito-de-furto-nos-eua.ghtml",
    photo="https://avatars.githubusercontent.com/u/58526599?v=4",
    title="Gato de cici do ifood é preso suspeito de furto nos eua",
    abstract="eh isso mesmo q vc leu otaria 2",
    deputy_name="Cici do Ifood",
    update_date=random_date(d1, d2),
    source="g1.globo.com"
).save()

populate_news_3 = News(
    id=3,
    deputy_id=3,
    link="https://g1.globo.com/planeta-bizarro/noticia/2019/06/10/cici-do-ifood-e-multada-por-excesso-de-velocidade-no-canada-e-culpa-frango-empanado.ghtml",
    photo="https://avatars.githubusercontent.com/u/58526599?v=4",
    title="Cici do ifood é multada por excesso de velocidade no canada e culpa frango empanado",
    abstract="KKKKKKKKKKKKKKK ai eh foda bixo",
    deputy_name="Cici do Ifood",
    update_date=random_date(d1, d2),
    source="g1.globo.com"
).save()

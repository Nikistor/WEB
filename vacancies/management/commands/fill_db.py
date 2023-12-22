import random

from django.core import management
from django.core.management.base import BaseCommand
from vacancies.models import *
from .utils import random_date, random_timedelta


def add_cities():
    City(
        name="Москва",
        description="Москва — столица и крупнейший город России. Сюда ведут многие пути и человеческие судьбы, с этим городом связано множество роковых и знаменательных событий истории, людских радостей и надежд, несчастий и разочарований, разумеется, легенд, мифов и преданий. Москва — блистательный город, во всех отношениях достойный называться столицей. Здесь великолепные памятники архитектуры и живописные парки, самые лучшие магазины и высокие небоскребы, длинное метро и заполненные вокзалы. Москва никогда не спит, здесь трудятся с утра до поздней ночи, а затем веселятся до утра.",
        status=1,
        foundation_date=1147,
        grp=13.1,
        climate=255,
        square=2561
    ).save()

    City(
        name="Санкт-Петербург",
        description="Санкт-Петербург – один из красивейших мегаполисов мира, посмотреть на который приезжают путешественники из разных уголков планеты. Раскинувшийся на побережье Финского залива, в устье реки Невы, Санкт-Петербург является вторым по величине городом России (в статусе самостоятельного субъекта федерации) и одновременно административным центром Ленинградской области и Северо-Западного федерального округа.",
        status=1,
        foundation_date=1147,
        grp=13.1,
        climate=255,
        square=2561
    ).save()

    City(
        name="Екатеринбург",
        description="Екатеринбург – административный центр Свердловской области, четвёртый по численности город России. Город расположен на Среднем Урале, на восточном склоне Уральских гор. Рядом проходит условная граница Европы и Азии. Благодаря тому, что Уральские горы в этом месте представляют собой холмы были проложены дороги из Центральной России в Сибирь. Здесь проходят железные дороги, крупные автодороги, действует международный аэропорт «Кольцово».",
        status=1,
        foundation_date=1147,
        grp=13.1,
        climate=255,
        square=2561
    ).save()

    City(
        name="Киров",
        description="Киров – город и областной центр на реке Вятке, известный как родина традиционного народного промысла – дымковской игрушки, вкусного вятского кваса, легкого кукарского кружева и самобытного праздника «Свистопляска». Киров находится в Предуралье, 896 км к северо-востоку от Москвы. Город вошел в историю в роли места ссылок, где издавна отбывали заключение бунтари, не угодные власти. В середине XIX века в вятской ссылке провел семь лет знаменитый русский писатель М. Е. Салтыков-Щедрин.",
        status=1,
        foundation_date=1147,
        grp=13.1,
        climate=255,
        square=2561
    ).save()

    City(
        name="Волгоград",
        description="Волгоград - город, один из крупнейших на Юге страны. Его называют портом пяти морей, Волго-Донской канал соединяет теплые южные моря – Черное, Азовское, Каспийское – с холодными Балтийским и Северным. Благодаря этому в городе интенсивно развивается торговля и кипит деловая жизнь. В городе-герое Волгограде находится множество памятников, посвященных героям Великой Отечественной войны.",
        status=1,
        foundation_date=1147,
        grp=13.1,
        climate=255,
        square=2561
    ).save()

    print("Услуги добавлены")


def add_vacancies():
    users = CustomUser.objects.filter(is_moderator=False)
    moderators = CustomUser.objects.filter(is_superuser=True)

    if len(users) == 0:
        print("Заявки не могут быть добавлены. Сначала добавьте пользователей с помощью команды add_users")
        return

    cities = City.objects.all()

    for _ in range(10):
        vacancy = Vacancy.objects.create()
        vacancy.name = "Вакансия №" + str(vacancy.pk)
        vacancy.status = random.randint(2, 5)

        # if vacancy.status in [3, 4]:
        #     vacancy.date_complete = random_date()
        #     vacancy.date_of_formation = vacancy.date_complete - random_timedelta()
        #     vacancy.date_created = vacancy.date_of_formation - random_timedelta()
        #     vacancy.moderator = random.choice(moderators)
        # else:
        #     vacancy.date_of_formation = random_date()
        #     vacancy.date_created = vacancy.date_of_formation - random_timedelta()

        if vacancy.status in [3, 4]:
            if vacancy.status == 3:
                vacancy.date_complete = None
            else:
                vacancy.date_complete = random_date()

            if vacancy.date_complete:
                vacancy.date_of_formation = vacancy.date_complete - random_timedelta()
            else:
                vacancy.date_of_formation = random_date()

            vacancy.date_created = vacancy.date_of_formation - random_timedelta()
            vacancy.moderator = random.choice(moderators)
        else:
            vacancy.date_of_formation = random_date()
            vacancy.date_created = vacancy.date_of_formation - random_timedelta()

        vacancy.employer = random.choice(users)

        for i in range(random.randint(1, 5)):
            vacancy.cities.add(random.choice(cities))

        vacancy.save()

    print("Заявки добавлены")

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # management.call_command("clean_db")

        add_cities()
        add_vacancies()










from data.text_box_data import Person
from faker import Faker
import random


faker_uk = Faker('uk_UA')
Faker.seed()


def generate_person():
    yield Person(
        full_name=faker_uk.name(),
        email=faker_uk.email(),
        current_address=faker_uk.address(),
        permanent_address=faker_uk.address(),
        firstname=faker_uk.first_name(),
        lastname=faker_uk.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(10000, 100000),
        department=faker_uk.job(),
        mobile=faker_uk.msisdn(),
    )
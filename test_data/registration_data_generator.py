from faker import Faker
import random


class RegistrationDataGenerator:
    def __init__(self):
        self.GENDER = random.choice()
        self.fake = Faker("pl_PL")
        # if self.GENDER == Gender.FEMALE:
        #     self.FIRST_NAME = self.fake.first_name_female()
        # else:
        #     self.FIRST_NAME = self.fake.first_name_male()
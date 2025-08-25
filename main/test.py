#My biography

import re
from enum import Enum
from datetime import date
from typing import List, Optional


class Gender(Enum):
    MALE = 'Мужской'
    FEMALE = 'Женский'


class EducationLevel(Enum):
    SECONDARY = 'Общее стреднее'
    SECONDARY_VOCATIONAL = 'Средне-техническое'
    HIGHER = 'Высшее'
    COURSES = 'Курсы'


class MaritalStatus(Enum):
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'


class Education:
    def __init__(self, level: EducationLevel, end_year: int, institution: str,
                 speciality: str, success: str = ''):
        self.level = level
        self.end_year = end_year
        self.institution = institution
        self.speciality = speciality
        self.success = success


class Contact:
    def __init__(self):
        self.phone = ''
        self.email = ''
        self.telegram = ''


class Person:
    def __init__(self, birthday: date, gender: Gender):
        self._birthday = birthday
        self._gender = gender
        self._surname = ''
        self._name = ''
        self._patronymic = ''
        self._education_list: List[Education] = []
        self._marital_status = MaritalStatus.SINGLE
        self._children: List[Person] = []
        self._city = ''
        self._contact = Contact()

    @property
    def birthday(self) -> date:
        return self._birthday

    @property
    def gender(self) -> Gender:
        return self._gender

    @property
    def surname(self) -> str:
        return self._surname

    @surname.setter
    def surname(self, value: str):
        self._surname = value

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def patronymic(self) -> str:
        return self._patronymic

    @patronymic.setter
    def patronymic(self, value: str):
        self._patronymic = value

    @property
    def age(self) -> int:
        today = date.today()
        return today.year - self._birthday.year - ((
            today.month, today.day) < (
                self._birthday.month, self._birthday.day))

    @property
    def marital_status(self) -> MaritalStatus:
        return self._marital_status

    @marital_status.setter
    def marital_status(self, value: MaritalStatus):
        self._marital_status = value

    @property
    def child_count(self) -> int:
        return len(self._children)

    @property
    def have_child(self) -> bool:
        return len(self._children) > 0

    @property
    def city(self) -> str:
        return self._city

    @city.setter
    def city(self, value: str):
        self._city = value

    @property
    def contact(self) -> Contact:
        return self._contact

    def get_education(self, index: int) -> Optional[Education]:
        if index < len(self._education_list):
            return self._education_list[index]
        return None

    def add_education(self, education: Education) -> None:
        self._education_list.append(education)

    def add_education_params(self, level: EducationLevel, end_year: int,
                             institution: str, speciality: str,
                             success: str = '') -> None:
        education = Education(level, end_year, institution, speciality,
                              success)
        self.add_education(education)

    def add_child(self, child) -> None:
        self._children.append(child)

    def change_phone(self, value: str) -> bool:
        norm_phone = ''.join(c for c in value if c.isdigit())
        phone_regex = re.compile(r"^[78]\d{10}$")
        is_match = phone_regex.fullmatch(norm_phone)
        if is_match:
            self._contact.phone = norm_phone
        return is_match

    def change_email(self, value: str) -> bool:
        email_regex = re.compile(
            (r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"))
        is_match = email_regex.fullmatch(value)
        if is_match:
            self._contact.email = value
        return is_match

    def change_telegram(self, value: str) -> bool:
        telegram_regex = re.compile(r"^@[a-zA-Z0-9_]{5,32}$")
        is_match = telegram_regex.fullmatch(value)
        if is_match:
            self._contact.telegram = value
        return is_match

    def __str__(self):
        return (
            f"ФИО: {self.surname} {self.name} {self.patronymic}\n"
            f"Дата рождения: {self.birthday}\n"
            f"Возраст: {self.age}\n"
            f"Пол: {self.gender.value}\n"
            f"Город: {self.city}\n"
            f"Семейное положение: {self.marital_status.value}\n"
            f"Телефон: {self.contact.phone}\n"
            f"Email: {self.contact.email}\n"
            f"Telegram: {self.contact.telegram}\n"
            f"Дети: {'Есть' if self.have_child else 'Нет'} "
            F"({self.child_count})\n"
            f"Образование:\n" + "\n".join(
                f"- {edu.level.value} ({edu.end_year}): {edu.institution}, "
                f"{edu.speciality}"
                for edu in self._education_list
            )
        )


# Create me
if __name__ == "__main__":
    me = Person(date(1980, 6, 19), Gender.MALE)
    me.surname = "Шагинян"
    me.name = "Сергей"
    me.patronymic = "Валерьевич"

    me.add_education_params(
        EducationLevel.HIGHER,
        2022,
        "Новочеркасский Военный Инстиут Связи",
        "Управление частями и подразделениями с электропроводными"
        + "средствами связи""",
        "Диплом с отличием, золотая медаль."
    )

    me.add_education_params(
        EducationLevel.COURSES,
        2023,
        "ScillFactory",
        "Ful-stack разработчик на Python"
    )

    Sasha = Person(date(2014, 5, 13), Gender.MALE)
    Sasha.name = "Александр"
    me.add_child(Sasha)

    me.marital_status = MaritalStatus.MARRIED
    me.city = "Краснодар"

    me.change_phone("+7(918)184-94-25")
    me.change_email("shagi80@mail.com")
    me.change_telegram("@shagi80")

    print(me)

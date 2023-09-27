from datetime import date, datetime
from dateutil.relativedelta import relativedelta

class Person():
    def __init__(self, birthday: date, name: str) -> None:
        self._name: str = name
        self._birthday: date = birthday

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value:str):
        if value != self._name:
            self._name = value

    @property
    def birthday(self) -> date:
        return self._birthday
    @birthday.setter
    def birthday(self, value:date):
        if value != self._birthday:
            self._birthday = value

    def GetAge(self) -> int:
        now = datetime.now()
        difference = relativedelta(now, self._birthday)
        return difference.years


mydate = date.fromisoformat('2009-11-05')
myPerson = Person(mydate, 'Mike')
myAge = myPerson.GetAge()
print(f'{myPerson.name} is {myAge} years old')

mydate = date.fromisoformat('2009-10-02')
myPerson = Person(mydate, 'Felicity')
myAge = myPerson.GetAge()
print(f'{myPerson.name} is {myAge} years old')

mydate = date.fromisoformat('2007-12-31')
myPerson = Person(mydate, 'Mary')
myAge = myPerson.GetAge()
print(f'{myPerson.name} is {myAge} years old')

mydate = date.fromisoformat('1976-05-04')
myPerson = Person(mydate, 'Daniel')
myAge = myPerson.GetAge()
print(f'{myPerson.name} is {myAge} years old')
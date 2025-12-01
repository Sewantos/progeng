import abc
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    def info(self):
        return  f"ФИО: {self.name}, возраст: {self.age}"
    
class Scholarship(abc.ABC):
    @abc.abstractmethod
    def count_scholarship(self) -> int:
        pass
    
    @abc.abstractmethod
    def __lt__(self, other: 'Scholarship') -> bool:
        pass

    @abc.abstractmethod
    def __gt__(self, other: 'Scholarship') -> bool:
        pass

    @abc.abstractmethod
    def __eq__(self, other: 'Scholarship') -> bool:
        pass

class Student(Person, Scholarship):
    def __init__(self, name: str, age: int, group: str, grades: float):
        super().__init__(name, age)
        self.group = group
        self.grades = grades

    def rate_scholarship(self) -> dict[str, int]:
        return{"highest": 6000, "medium": 4000, "none": 0}

    def count_scholarship(self) -> int:
        money = self.rate_scholarship()
        if self.grades == 5:
            return money["highest"]
        elif self.grades >= 4:
            return money["medium"]
        else:
            return money["none"]
        
    def __gt__(self, other: Scholarship) -> bool:
        return self.count_scholarship() > other.count_scholarship()
    
    def __lt__(self, other: Scholarship) -> bool:
        return self.count_scholarship() < other.count_scholarship()

    def __eq__(self, other: Scholarship) -> bool:
        return self.count_scholarship() == other.count_scholarship()

class Graduate(Student):
    def __init__(self, name: str, 
            age: int, group: str, 
            grades: float, paper: str):
        super().__init__(name, age, group, grades)
        self.paper = paper
    
    def rate_scholarship(self) -> dict[str, int]:
        return{"highest": 8000, "medium": 6000, "none": 0}
    
student = Student("Тарковский Андрей Арсеньевич", 21, "О-217", 5)
graduate = Graduate(
    "Михалков Никита Сергеевич", 25, "О-237", 
    3.9, "Неоконченная пьеса для механического пианино"
)

print(student.info())
print("Стипендия:", student.count_scholarship(), "р")

print(graduate.info())
print("Стипендия:", graduate.count_scholarship(), "р")

print(
    "Стипендия студента", student.name, 
    "больше стипендии аспиранта", graduate.name,
    ":", student.__gt__(graduate)
)
print("Стипендия студента", student.name, 
    "меньше стипендии аспиранта", graduate.name,
    ":", student.__lt__(graduate)
)
print(
    "Стипендия студента", student.name, 
    "равна стипендии аспиранта", graduate.name, 
    ":", student.__eq__(graduate)
)
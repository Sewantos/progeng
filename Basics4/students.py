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
    def compare_scholarship(self, other: 'Scholarship') -> str:
        pass

class Student(Person, Scholarship):
    def __init__(self, name: str, age: int, group: str, grades: float):
        super().__init__(name, age)
        self.group = group
        self.grades = grades

    def grades2money(self) -> dict[str, int]:
        return{"highest": 6000, "medium": 4000, "none": 0}

    def count_scholarship(self) -> int:
        money = self.grades2money()
        if self.grades == 5:
            return money["highest"]
        elif self.grades < 5:
            return money["medium"]
        else:
            return money["none"]
    
    def compare_scholarship(self, other: 'Scholarship') -> str:
        self_sch = self.count_scholarship()
        other_sch = other.count_scholarship()
        if self_sch > other_sch:
            return "больше"
        elif self_sch < other_sch:
            return "меньше"
        return "равна"

class Graduate(Student):
    def __init__(self, name: str, age: int, group: str, grades: float, paper: str):
        super().__init__(name, age, group, grades)
        self.paper = paper
    
    def grades2money(self) -> dict[str, int]:
        return{"highest": 8000, "medium": 6000, "none": 0}
    
student = Student("Тарковский Андрей Арсеньевич", 21, "О-217", 5)
graduate = Graduate("Михалков Никита Сергеевич", 25, "О-237", 3.9, "Неоконченная пьеса для механического пианино")

print(student.info())

print("Стипендия:", student.count_scholarship(), "р")

print(graduate.info())
print("Стипендия:", graduate.count_scholarship(), "р")

print("Cтипендия", graduate.name, graduate.compare_scholarship(student), "стипендии", student.name)
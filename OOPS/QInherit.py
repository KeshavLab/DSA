class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def show_person_info(self):
        print(f"Name : {self.name}, Age: {self.age}")


class Employee(Person):
    def __init__(self,name,age,emp_id,salary):
        super().__init__(name,age)

        self.emp_id=emp_id
        self.salary= salary

    def show_emp_info(self):
        print(f"emp_id : {self.emp_id},Salary :{self.salary}")

emp1=Employee("John",30,101,50000)
emp1.show_person_info()

emp1.show_emp_info()
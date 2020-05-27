import abc

class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(abc.ABC): # Para não ser acessada diretamente ela precisa ser abstrata
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.workload = 8 # Carga horaria fixa para todos os funcionarios


    @abc.abstractmethod #  Obrigatorio a implementação do metodo
    def calc_bonus(self):
        pass

    @abc.abstractmethod #  Obrigatorio a implementação do metodo
    def get_hours(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department('managers', 1) # Proteção do atributo

    def get_department(self): # Acessa o atributo protegido
        return self.__department.name

    def set_department(self, name_department):
        self.__department.name = name_department
        return self.__department.name

    def calc_bonus(self):
        return self.salary * 0.15

    def get_hours(self):
        return self.workload


class Seller(Manager): # Vendedor
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self.__department = Department('sellers', 2)
        self.__sales = 0 # Proteção do atributo

    def get_sales(self): # Acessa o atributo protegido
    	return self.__sales

    def put_sales(self, sales): # Adiciona valores ao atributo protegido
    	self.__sales += sales
    	return self.__sales

    def get_department(self): # Retorna o nome do departamento
        return self.__department.name

    def set_department(self, name_department): # Modifica o nome do departamento
        self.__department.name = name_department
        return self.__department.name

    def calc_bonus(self):
        self.__sales = self.__sales * 0.15 # Total das vendas * 0.15
        return self.__sales

    def get_hours(self):
        return self.workload

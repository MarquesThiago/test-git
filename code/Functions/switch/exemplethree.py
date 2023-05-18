from collections import namedtuple


def create_type(name, calculate):
    GenericType = namedtuple(
        'GenericType', ['name', 'calculate']
    )
    return GenericType(name, calculate)


def type_hourly_pay():

    def calculate(value):
        pass

    return create_type('hourly', calculate)


def type_salarie_pay(value):

    def calculate(value):
        pass

    return create_type('salarie', calculate)


def type_commissioned_pay(value):

    def calculate(value):
        pass

    return create_type('commissioned', calculate)


def employee(name, type, week_hours, salarie, job):
    Employee = namedtuple(
        'Employee',
        [
            'name',
            'type',
            'week_hours',
            'base_salarie',
            'job_function',
            'calculate'
        ]
    )

    return Employee(name, type.name, week_hours, salarie, job, type.calculate)


def create_type_employee(type):

    type_employee = {
        "COMMISSIONED": type_commissioned_pay(),
        "SALARIED": type_salarie_pay(),
        "HOURLY": type_hourly_pay()
    }

    if type not in type_employee:
        raise ValueError('Invalid employee type')

    return type_employee[type]


def FactoryEmployee(name, type, week_hours, salarie, job):
    return employee(name, create_type_employee(type), week_hours, salarie, job)

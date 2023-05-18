from collections import namedtuple


def calculate_hourly_pay(value):
    pass


def calculate_salarie_pay(value):
    pass


def calculate_commissioned_pay(value):
    pass


def create_employee(name, type, week_hours, salarie, job):

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

    if type == "COMMISSIONED":
        return Employee(
            name, type, week_hours, salarie, job, calculate_commissioned_pay
        )
    elif type == "SALARIED":
        return Employee(
            name, type, week_hours, salarie, job, calculate_salarie_pay
        )
    elif type == "HOURLY":
        return Employee(
            name, type, week_hours, salarie, job, calculate_hourly_pay
        )
    else:
        raise TypeError('alue not expected')


def FactoryEmployee(name, type, week_hours, salarie, job):
    return create_employee(name, type, week_hours, salarie, job)

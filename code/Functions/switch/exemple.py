def calculate_hourly_pay(object):
    pass


def calculate_salarie_pay(object):
    pass


def calculate_commissioned_pay(object):
    pass


def money_pay(employee):

    if employee.type == 'COMMISSIONED':
        return calculate_commissioned_pay(employee)
    elif employee.type == 'HOURLY':
        return calculate_hourly_pay(employee)
    elif employee.type == 'SALARIED':
        return calculate_salarie_pay(employee)
    else:
        raise TypeError('Value not excepted')

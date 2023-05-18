import re


class People:

    def __init__(self, cpf) -> None:
        self.register_number_document = cpf


def verify_cpf(person: People) -> bool:

    cpf = str(person.register_number_document)
    only_number_cpf = re.sub(r"\D*", '', cpf)
    TOTAL_NUMBER_CPF = 11

    if len(only_number_cpf) != TOTAL_NUMBER_CPF:
        return False
    elif re.match(
        f"{only_number_cpf[0]}{{{TOTAL_NUMBER_CPF}}}",
        only_number_cpf
    ):
        return False
    else:
        return True

import re


def verify_cpf(register_number_document: str) -> bool:

    cpf = str(register_number_document)
    regex_not_digit = r"\D*"

    only_number_cpf = re.sub(regex_not_digit, '', cpf)

    TOTAL_NUMBER_CPF = 11
    regex_number_repeated_all = f"{only_number_cpf[0]}{{{TOTAL_NUMBER_CPF}}}"

    if not len(only_number_cpf) is TOTAL_NUMBER_CPF:
        return False
    elif re.match(
        regex_number_repeated_all,
        only_number_cpf
    ):
        return False
    else:
        return True

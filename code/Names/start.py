import re


def verify(p):

    number = str(p.number)
    d = re(r"\D*", '', number)

    if len(d) != 11:
        return False
    elif re.match(f"{d[0]}{'{11}'}", str(d)):
        return False
    else:
        return True

from typing import Union

number_four = 4
number_five = 5


def number_square(number: Union[int, float, complex]):
    return number**2


def number_cube(number: Union[int, float, complex]):
    return number**3


def is_odd_even_response(number):
    return number_square(number) if number % 2 == 0 else number_cube(number)


def ruler_number_cube_square(number: Union[int, float]):
    try:
        return is_odd_even_response(number)
    except TypeError:
        raise TypeError(
            (
                "Argument is not a number of type int or float, " +
                f"type from argument is {type(number)}"
            )
        )


ruler_number_cube_square(number_four)
ruler_number_cube_square(number_five)

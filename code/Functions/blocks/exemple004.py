from typing import Callable, Any, Union

number_four = 4
number_five = 5

RealNumber = Union[int, float]
Number = Union[int, float, complex]


def number_square(number: Number) -> Number:
    return number**2


def number_cube(number: Number) -> Number:
    return number**3


def is_odd_even_response(
    number: RealNumber,
    res_even: Callable[[Number], Any],
    res_odd: Callable[[Number], Any]
) -> Any:
    return res_even(number) if (number % 2) == 0 else res_odd(number)


def ruler_number_cube_square(number: RealNumber) -> RealNumber:
    try:
        return is_odd_even_response(number, number_square, number_cube)
    except TypeError:
        raise TypeError(
            (
                "Argument is not a number of type int or float, " +
                f"type from argument is {type(number)}"
            )
        )


ruler_number_cube_square(number_four)
ruler_number_cube_square(number_five)

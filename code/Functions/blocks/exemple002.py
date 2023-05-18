number_four = 4
number_five = 5


def is_odd_even_response(number):
    return number**2 if number % 2 == 0 else number**3


def ruler_number_cube_square(number):
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

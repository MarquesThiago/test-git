number_four = 4
number_five = 5


def ruler_number_cube_square(number):
    try:
        if number % 2 == 0:
            return number**2
        else:
            return number**3
    except TypeError:
        raise TypeError(
            (
                "argument is not a number of type int or float, " +
                f"type from argument {type(number)}"
            )
        )


ruler_number_cube_square(number_four)
ruler_number_cube_square(number_five)

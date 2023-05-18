from re import match
from pandas import DataFrame
from typing import Union
from forex_python.converter import CurrencyRates


def treat_remove_space(
    dataframe: DataFrame,
    column: str
) -> DataFrame:

    dataframe[column] = dataframe[column].apply(
        lambda cell: cell.strip()
    )

    return dataframe


def extract_name_coin(
    dataframe: DataFrame,
    column: str,
    name_new_column: str,
    regexp: str = '^[A-Z]{3}'
) -> DataFrame:
    dataframe[name_new_column] = dataframe[column].apply(
        lambda cell: match(cell, regexp)
    )
    return dataframe


def treatment_dataframe(dataframe: DataFrame) -> DataFrame:

    dataframe = treat_remove_space(dataframe, 'descriptorTransaction')
    dataframe = extract_name_coin(
        dataframe,
        'descriptorTransaction',
        'coin'
    )
    return dataframe


def convert_coin_to_real(
    dataframe: DataFrame,
    column_value: str,
    column_coin: str,
    name_column: str
):

    def convertor():
        c = CurrencyRates()
        return c.get_rate('USD', 'BRL')

    def calculate_value_real(value: Union[int, float]) -> float:
        return convertor() * value

    def check_is_coin_real(
        value: Union[int, float],
        coin: str
    ) -> Union[int, float]:
        return value if coin == 'BRL' else calculate_value_real(value)

    def convert(
        dataframe: DataFrame,
        column_coin: str,
        column_value: str,
        name_new_column: str
    ) -> DataFrame:
        dataframe[name_new_column] = dataframe.apply(
            lambda row: check_is_coin_real(
                row[column_value],
                row[column_coin]
            ),
            axis=1
        )

        return dataframe

    return convert(dataframe, column_coin, column_value, name_column)


def implementing_convert_coin(dataframe: DataFrame):
    return convert_coin_to_real(
        dataframe,
        'valueTransaction',
        'coin',
        "valueReal"
    )


def process_data(dataframe: DataFrame):
    dataframe = treatment_dataframe(dataframe)
    dataframe = implementing_convert_coin(dataframe)
    return dataframe

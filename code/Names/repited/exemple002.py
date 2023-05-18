from pyspark import DataFrame


def rename_columns(
    dataframe: DataFrame,
    list_columns_name: list
) -> DataFrame:

    TOTAL_COLUMNS = len(list_columns_name)
    dataframe_columns = dataframe.columns

    for index in range(TOTAL_COLUMNS):

        new_name_column = list_columns_name[index]
        old_name_column = dataframe_columns[index]

        dataframe = dataframe.withColumnRename(
            old_name_column, new_name_column
        )

    return dataframe

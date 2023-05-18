from pyspark import DataFrame


def rename_columns(
    dataframe: DataFrame,
    list_columns_name: list
) -> DataFrame:

    TOTAL_COLUMNS = len(list_columns_name)
    dataframe_columns = dataframe.columns

    for index in range(TOTAL_COLUMNS):

        new_name = list_columns_name[index]
        old_name = dataframe_columns[index]

        dataframe = dataframe.withColumnRename(
            old_name, new_name
        )

    return dataframe

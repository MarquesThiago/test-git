from pyspark import DataFrame


def rename_columns(
    dataframe: DataFrame,
    columns: list
):

    TOTAL_COLUMNS = len(columns)
    dataframe_columns = dataframe.columns

    for index in range(TOTAL_COLUMNS):

        column = columns[index]
        dataframe_column = dataframe_columns[index]

        dataframe = dataframe.WithColumnRename(
            dataframe_column, column
        )

    return dataframe

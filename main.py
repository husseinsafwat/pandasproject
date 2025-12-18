import dataframe
import file_handler
from file_handler import read_dtype, read_csv_file
from stats import get_col_mean, get_col_median, get_col_max, get_col_min, get_col_mode


def main():


    #TODO: Read data

    data = dataframe.Dataframe.create_frame('data/titanic.csv' , 'data/titanic_dtype.csv')
    # TODO: Fill missing values
    # Numeric columns → mean
    # Categorical columns → mod
    print(data.count_nulls())
    print(data.describe())
    data.fillna('median')
    print(data.count_nulls())
    print(data.describe())
    # TODO:Generate statistics file



    # TODO:Write cleaned data to CSV
    data.to_csv('data/new_titanic.csv')




if __name__ == "__main__":
    main()

import pandas as pd
import numpy as numpy

# =====Series=====

s = pd.Series([2, 4, 6, 8])

# print(s)

another_series = pd.Series([2, 4, 6, 8, 5], index=["f", "a", "c", "e", "a"])

# print(another_series)

# retrieve n number of values that have a given key
# print(another_series["a"])

# retrieve multiple values via passing in multiple keys
# NOTE:  this handles a "bad" index x, the value of which is NaN
# print(another_series[["a", "x"]])

# retrieve multiple values based on a boolean expression
# NOTE:  since the expression is inside the [] then the resuls are returned in a list; not raw booleans
# print(another_series[another_series > 4])

# retrieves the boolean result of the (boolean) expression
# print(another_series > 4)

# retrieves the result of the expression -- in this case multiply each member by 2
# print(another_series * 2)

dictionary_data = {"b": 100, "c": 150, "e": 200}

# similar behavior using data from a dict instead of a list
dictionary_data_series = pd.Series(dictionary_data, list("abcde"))

# print(dictionary_data_series * 2)

# =====DataFrame=====

pop_data = {"state": ["PA", "NY", "TX", "FL"], "year": [
    2010, 2011, 2012, 2013], "pop": [18.2, 12.2, 9.2, 9.7]}

addl_pop_data = pop_data

addl_pop_data["other"] = [20, 30, 10, 25]

# print(addl_pop_data)

pop_data_frame = pd.DataFrame(pop_data)

# describe provide common stats for the data in data frame
# print(pop_data_frame.describe())

# print(pop_data_frame)

# print(pop_data_frame["state"])

pop_data_dict_of_dict = {"PA": {"2010": 18.2,
                                "2011": 12.2}, "FL": {"2008": 9.2, "2010": 9.7}}

another_df = pd.DataFrame(pop_data_dict_of_dict)

# print(another_df)

# a DataFrame exposes index, columns, and values as properties -- providing easy access to those sets of values

grouping_data_frame = pd.DataFrame({
    "A": ["foo", "bar", "baz"],
    "B": ["one", "two", "three"],
    "C": numpy.random.randn(3),
    "D": numpy.random.randn(3)})

# print(grouping_data_frame)

# print(grouping_data_frame.groupby("A").sum())


def example3():
    df = pd.read_csv('weather.txt')
    print(df.head())    # top 5 lines
    print(df.tail(3))   # bottom 3 lines


def example6():
    df = pd.read_csv('weather.txt')
    print(df.sort_values('average_precipitation', ascending=False))


def example7():
    df = pd.read_csv('weather.txt')
    print(df.avg_low)
    print(df['avg_low'])
    print(df[2:4])  # rows 2 to 4
    print(df[['avg_low', 'avg_high']])
    # multiple columns: df.loc[from_row:to_row,['column1','column2']]
    print(df.loc[:, ['avg_low', 'avg_high']])
    # slicing scalar; outputs the avg_precipitation of row 9
    print(df.loc[9, ['average_precipitation']])
    print(df)
    # print(df.iloc[2:4,[0,3]])       #indexes 2-3, columns 0-3
    print(df.iloc[2:4])


def example8():
    df = pd.read_csv('weather.txt')
    higherThan70 = df[(df.avg_high > 70)]
    print(higherThan70)
    print()
    print(higherThan70[['month', 'avg_low', 'avg_high']])
    print()
    avg_low = higherThan70.avg_low
    print('max(avg_low)', max(avg_low))


# example3()
example8()

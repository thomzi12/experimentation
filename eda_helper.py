import pandas as pd

'''
eda_helper.py

A file with data analysis functions I often use to do the initial exploration of data

TODO:
- have if/else for columns that act as table key >> no need to print off value counts
'''


def _value_count_percentages(df_col):
    '''
    INPUT: dataframe column
    OUTPUT: dataframe with two columns: value counts and percentage of each distinct value
    '''
    value_counts_df = pd.DataFrame(df_col.value_counts())
    value_counts_df.columns = ['value_counts']
    value_counts_df['distribution'] = value_counts_df[
        'value_counts'] * 100 / sum(value_counts_df.value_counts)
    return value_counts_df


def _null_explorer(df_col):
    '''
    INPUT: dataframe column
    OUTPUT: string with two values: number of null values and null values as a percent of total rows
    '''
    null_values = df_col.isnull().sum()
    null_percent = df_col.isnull().sum() * 100 / df_col.shape[0]
    return 'Number of null values: {} ({:.1f}%)'.format(null_values, null_percent)


def column_inspector(df, col):
    '''
    INPUT: Dataframe, column of interest
    OUTPUT: Print outs of various descriptive statistics
    '''
    print('column name: {}'.format(col))
    print(df[col].describe())
    print('------------------')
    print('number of unique values: {}'.format(df[col].nunique()))
    print('------------------')
    print(_null_explorer(df[col]))
    print('------------------')
    value_counts = _value_count_percentages(df[col])
    if value_counts.shape[0] >= 10:
        print('10 most common values:')
        print(value_counts.iloc[:10, ])
        print('10 least common values:')
        print(value_counts.iloc[-10:, ])
    else:
        print(value_counts)
    print('******************')
    print('')
    return None


def _null_col_inspector(df):
    '''
    INPUT: Pandas dataframe
    OUTPUT: list of columns with at least one null value in them
    '''
    col_lst = []

    for col in df.columns:
        if df[col].isnull().sum() > 0:
            col_lst.append(col)
    return col_lst


def df_inspector(df):
    '''
    INPUT: Dataframe
    OUTPUT: column_inspector() called upon each columns
    '''
    null_cols = _null_col_inspector(df)
    if null_cols:
        print('Columns with at least one null value:')
        print(null_cols)
        print('')
    for col in df.columns:
        column_inspector(df, col)
    return None

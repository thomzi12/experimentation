import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import numpy as np

'''
regression_helper.py

A file with regression functions I often use for linear/logistic regression
'''

def logistic_regression(df, y_col, x_col, dummy_cols = None):
    '''
    INPUT: Dataframe, string of column of response variable, list of explanatory variables,
                    list of categorical variables to transform into dummy variable columns
    OUTPUT: Fitted logistic regression object
    '''

    print('Be sure to remove highly correlated variables!')

    y = df[y_col]
    x = df[x_col]

    if dummy_cols:
        for column in dummy_cols:
            dummy_columns = pd.get_dummies(x[column], prefix = column)
            x = x.join(dummy_columns.iloc[:,1:])
            print('excluded column: {}'.format(dummy_columns.columns[0]))
            x = x.drop(column, axis=1)

    # add a constant
    x['const'] = 1

    # Fit and summarize OLS model
    mod = sm.Logit(y,x.astype(float))
    res = mod.fit()

    return res


def linear_regression(df, y_col, x_col, dummy_cols = None):
    '''
    INPUT: Dataframe, string of column of response variable, list of explanatory variables,
                    list of categorical variables to transform into dummy variable columns
    OUTPUT: Fitted linear regression object
    '''
    # TODO: add correlation plot
    print('Be sure to remove highly correlated variables!')

    y = df[y_col]
    x = df[x_col]

    if dummy_cols:
        for column in dummy_cols:
            dummy_columns = pd.get_dummies(x[column], prefix = column)
            x = x.join(dummy_columns.iloc[:,1:])
            print('excluded column: {}'.format(dummy_columns.columns[0]))
            x = x.drop(column, axis=1)



    # add a constant
    x['const'] = 1

    # Fit and summarize OLS model
    mod = sm.OLS(y,x.astype(float))
    res = mod.fit()

    return res

def fitted_residual_plot(res, y):
    # Hmm, get a way to put this into side by side plots
    # Get fitted residual plot
    preds = res.fittedvalues.copy()
    actual = y.values.copy()
    residuals = actual-preds

    plt.figure(figsize=(6,2.5))
    plt.scatter(residuals, preds)
    plt.title('Fitted-Residual Plot to test Linearity & Equal Variance')
    return None

def q_q_plot(res, y):
    # Get Q-Q plot
    preds = res.fittedvalues.copy()
    actual = y.values.copy()
    residuals = actual-preds

    fig, ax = plt.subplots(figsize=(6,2.5))
    sp.stats.probplot(residuals, plot = ax, fit=True)
    plt.title('QQ Plot to test Normality')
    return None

def sns_correlation_plot(df, cols):
    mask = np.zeros_like(df[cols].corr())
    mask[np.triu_indices_from(mask)] = True
    sns.heatmap(df[cols].corr(), mask=mask)
    return None

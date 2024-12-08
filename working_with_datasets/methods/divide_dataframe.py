import pandas as pd
from .variables.small_variables import *
from .variables.datetime_cols import datetime_cols
from .variables.cols_continuous_variables import cols_continuous_variables
from .variables.cols_categorical_variables import cols_categorical_variables
from .variables.cols_to_drop import cols_to_drop

def divide_dataframe(df_bki:pd.DataFrame):
    usd_loan_idx = df_bki.loc[(df_bki['account_amt_currency_code'] == 'USD') | (df_bki['account_amt_currency_code'] == 'USD')].index
    df_bki.drop(usd_loan_idx, inplace=True)
    df_bki.drop(columns=cols_to_drop, inplace=True, index=1)
    df_dates = df_bki[datetime_cols]
    df_continuous = df_bki[cols_continuous_variables]
    df_categorical = df_bki[cols_categorical_variables]
    df_application_id = df_bki[[acc_uid, application_id]]
    return df_dates, df_continuous, df_categorical, df_application_id
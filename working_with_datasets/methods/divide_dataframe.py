import pandas as pd
from .variables.small_variables import *
from .variables.datetime_cols import datetime_cols
from .variables.cols_continuous_variables import cols_continuous_variables
from .variables.cols_categorical_variables import cols_categorical_variables
from .variables.cols_to_drop import cols_to_drop
from .df_categorical_compressed_and_indicatored import df_categorical_compressed
from .df_continuous_compressed import df_continuous_compressed

def divide_dataframe(df_bki:pd.DataFrame):
    usd_loan_idx = df_bki.loc[(df_bki['account_amt_currency_code'] == 'USD') | (df_bki['account_amt_currency_code'] == 'USD')].index
    df_bki.drop(usd_loan_idx, inplace=True)

    df_bki.drop(columns=cols_to_drop, inplace=True, index=1)

    df_dates = df_bki[datetime_cols]

    df_continuous = df_continuous_compressed(df_bki[cols_continuous_variables])

    df_categorical = df_categorical_compressed(df_bki[cols_categorical_variables]).groupby(['application_id'], as_index=False).sum()

    df_application_id = df_bki[[acc_uid, application_id]].groupby(['application_id'], as_index=False).agg(
        application_count=(acc_uid, 'count')
    )

    return df_dates, df_continuous, df_categorical, df_application_id
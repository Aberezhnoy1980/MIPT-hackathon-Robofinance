import pandas as pd
from .variables.small_variables import *
from .variables.datetime_cols import datetime_cols
from .variables.cols_continuous_variables import cols_continuous_variables
from .variables.cols_categorical_variables import cols_categorical_variables
from .variables.cols_to_drop import cols_to_drop
from .df_categorical_compressed_and_indicatored import df_categorical_compressed
from .df_continuous_compressed import df_continuous_compressed
from .cols_to_datetime import cols_to_datetime
from .account_credit_limit import account_credit_limit
from .df_attr_values import df_attr_values


def divide_dataframe(df_bki:pd.DataFrame, target_df=None) -> pd.DataFrame:

    usd_loan_idx = df_bki.loc[(df_bki['account_amt_currency_code'] == 'USD') | (df_bki['account_amt_currency_code'] == 'USD')].index

    df_bki.drop(usd_loan_idx, inplace=True)

    df_bki.drop(columns=cols_to_drop, inplace=True)

    df_dates = cols_to_datetime(df_bki[datetime_cols])

    df_continuous = df_continuous_compressed(df_bki[cols_continuous_variables])

    df_categorical = df_categorical_compressed(df_bki[cols_categorical_variables])

    df_application_id = df_bki[[acc_uid, application_id]].groupby(['application_id'], as_index=False).agg(
        application_count=(acc_uid, 'count')
    )

    df_pivot_account_credit_limit = account_credit_limit(df_bki[['application_id', 'account_amt_credit_limit', 'trade_loan_kind_code']])

    df_attr_val = df_attr_values(df_bki[['application_id', 'attr_value']])

    intermediate_df = pd.merge(df_dates, df_continuous, left_on='application_id', right_on='application_id')
    intermediate_df1 = pd.merge(df_categorical, df_application_id, left_on='application_id', right_on='application_id')

    intermediate_df2 = pd.merge(intermediate_df, intermediate_df1, left_on='application_id', right_on='application_id')

    intermediate_df2.fillna(0.0, inplace=True)

    intermediate_df3 = pd.merge(intermediate_df2, df_pivot_account_credit_limit, left_on='application_id', right_on='application_id')

    intermediate_df4 = pd.merge(intermediate_df3, df_attr_val, left_on='application_id', right_on='application_id')

    if(target_df is not None):
        final_df = pd.merge(intermediate_df4, target_df, left_on='application_id', right_on='application_id')

    else: final_df = intermediate_df4

    final_df.set_index(['reporting_dt'], inplace=True)
    final_df.sort_index(ascending=True, inplace=True)

    if('client_id' in final_df.columns):
        final_df.drop(columns=['client_id'], inplace=True)

    return final_df
import pandas as pd
# from datetime import datetime
# import numpy as np

def negative_scoring(df_dates:pd.DataFrame) -> int:    
    negative_score = 0
    if(
        pd.notnull(df_dates['legal_items_court_act_dt'])
    ):
        negative_score += 1

    if(
        pd.notnull(df_dates['due_arrear_start_dt'])
    ):
        negative_score += 1

    if(
        pd.notnull(df_dates['past_due_dt'])
    ):
        negative_score += 1
    
    if(
        pd.notnull(df_dates['past_due_principal_missed_date'])
    ):
        negative_score += 1
        
    if(
        pd.notnull(df_dates['past_due_int_missed_date'])
    ):
        negative_score += 1
        
    return negative_score

def negative_score_to_categorical(df_dates:pd.DataFrame) -> str:
    if (
        df_dates['negative_score'] == 0
    ):
        return 'no_overdue'
    elif(
        (df_dates['negative_score'] > 0)
        and
        (df_dates['negative_score'] <= 2)
    ):
        return 'mild_overdue'
    elif(
        (df_dates['negative_score'] > 2)
        and
        (df_dates['negative_score'] <= 3)
    ):
        return 'moderate_overdue'
    elif(
        df_dates['negative_score'] > 3
    ):
        return 'severe_overdue'

def amount_of_opened_credits(df_dates:pd.DataFrame) -> int:
    if(
        pd.notnull(df_dates['trade_opened_dt'])
    ):
        return 1
    else: return 0

def amount_of_closed_credits(df_dates:pd.DataFrame) -> int:
    if(
        pd.notnull(df_dates['trade_close_dt'])
    ):
        return 1
    else: return 0

def year_of_credit_open(df_dates:pd.DataFrame):
    return df_dates['trade_opened_dt'].year

def opened_credits_per_year(df_dates:pd.DataFrame):
    if (
        df_dates['year_of_credit_open'] < 2015
    ):
        return 'before 2015'
    elif(
        (df_dates['year_of_credit_open'] >= 2015)
        and
        (df_dates['year_of_credit_open'] < 2018)
    ):
        return 'between 2015 and 2018'
    elif(
        (df_dates['year_of_credit_open'] >= 2018)
        and
        (df_dates['year_of_credit_open'] < 2021)
    ):
        return 'between 2018 and 2021'
    elif(
        df_dates['year_of_credit_open'] >= 2021
    ):
        return 'after 2021'

def cols_to_datetime(df_dates:pd.DataFrame) -> pd.DataFrame:
    cols_for_datetime_format = [x for x in df_dates.columns if x != 'application_id']
    cols_for_final_removal = [x for x in cols_for_datetime_format if x != 'reporting_dt']

    df_dates[cols_for_datetime_format] = df_dates[cols_for_datetime_format].apply(pd.to_datetime)

    df_dates['credit_duration'] = (df_dates['trade_close_dt'] - df_dates['trade_opened_dt']).dt.days
    # df_dates['insurance_duration'] = (df_dates['collat_insured_insur_end_dt'] - df_dates['collat_insured_insur_start_dt']).dt.days
    # df_dates['debt_repaid_duration'] = (df_dates['collat_repay_dt'] - df_dates['trade_opened_dt']).dt.days
    df_dates['negative_score'] = df_dates.apply(negative_scoring, axis=1)
    df_dates['negative_score_to_categorical'] = df_dates.apply(negative_score_to_categorical, axis=1)
    df_dates['credit_opened'] = df_dates.apply(amount_of_opened_credits, axis=1)
    df_dates['credit_closed'] = df_dates.apply(amount_of_closed_credits, axis=1)
    df_dates['year_of_credit_open'] = df_dates.apply(year_of_credit_open, axis=1)
    df_dates['opened_credits_per_year'] = df_dates.apply(opened_credits_per_year, axis=1)

    cols_for_final_removal.append('negative_score')
    cols_for_final_removal.append('year_of_credit_open')

    df_dates.drop(columns=cols_for_final_removal, inplace=True)

    df_dates = pd.get_dummies(df_dates, columns=['negative_score_to_categorical', 'opened_credits_per_year'], dtype=int, dummy_na=False)

    df_dates_groupped = df_dates.groupby(['application_id'], as_index=False).agg(
        credit_duration_mean = ('credit_duration', 'mean'),
        credit_duration_sum = ('credit_duration', 'sum'),
        credit_duration_min = ('credit_duration', 'min'),
        credit_duration_max = ('credit_duration', 'max'),
        amount_of_opened_credits = ('credit_opened', 'sum'),
        amount_of_closed_credits = ('credit_closed', 'sum'),

        reporting_dt = ('reporting_dt', 'first'),
        negative_score_to_categorical_no_overdue = ('negative_score_to_categorical_no_overdue', 'sum'),
        negative_score_to_categorical_mild_overdue = ('negative_score_to_categorical_mild_overdue', 'sum'),
        negative_score_to_categorical_moderate_overdue = ('negative_score_to_categorical_moderate_overdue', 'sum'),
        negative_score_to_categorical_severe_overdue = ('negative_score_to_categorical_severe_overdue', 'sum')
    )

    df_dates_groupped['opened_to_closed_credit_ratio'] = df_dates_groupped['amount_of_closed_credits'] / df_dates_groupped['amount_of_opened_credits']

    return df_dates_groupped
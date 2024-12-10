import pandas as pd

def number_of_overdues_per_credit(df_bki:pd.DataFrame) -> int:
    total_no_of_overdues = 0
    list_of_overdues = [
        '1',
        '2'
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        'A',
        'B'
    ]
    for item in df_bki['attr_value']:
        if item in list_of_overdues:
            total_no_of_overdues += 1
    return total_no_of_overdues

def risky_status(df_bki:pd.DataFrame) -> int:
    total_no_of_overdues = 0
    list_of_overdues = [
        '1',
        '2'
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        'A',
        'B',
        'S',
        'R',
        'W',
        'U',
        'T',
    ]
    for item in df_bki['attr_value']:
        if item in list_of_overdues:
            total_no_of_overdues += 1
    return total_no_of_overdues

def number_of_hard_overdues_per_credit(df_bki:pd.DataFrame) -> int:
    total_no_of_overdues = 0
    list_of_overdues = [
        '5',
        '6',
        '7',
        '8',
        '9',
        'A',
        'B'
    ]
    for item in df_bki['attr_value']:
        if item in list_of_overdues:
            total_no_of_overdues += 1
    return total_no_of_overdues

def number_of_hopeless_debts(df_bki:pd.DataFrame) -> int:
    total_no_of_overdues = 0
    hopeless_debt = 'B'
    bankrupt = 'T'
    for item in df_bki['attr_value']:
        if ((item == hopeless_debt) or (item == bankrupt)):
            total_no_of_overdues += 1
    return total_no_of_overdues

def df_attr_values(df_bki:pd.DataFrame) -> pd.DataFrame:
    df_bki['number_of_overdues_per_credit'] = df_bki.apply(number_of_overdues_per_credit, axis=1)
    df_bki['number_of_hard_overdues_per_credit'] = df_bki.apply(number_of_hard_overdues_per_credit, axis=1)
    df_bki['number_of_hopeless_debts'] = df_bki.apply(number_of_hopeless_debts, axis=1)
    df_bki['risky_status'] = df_bki.apply(risky_status, axis=1)

    df_bki.drop(columns=['attr_value'], axis=1, inplace=True)

    return df_bki.groupby(['application_id'], as_index=False).agg(
        total_number_of_overdues_sum = ('number_of_overdues_per_credit', 'sum'),
        total_number_of_overdues_min = ('number_of_overdues_per_credit', 'min'),
        total_number_of_overdues_max = ('number_of_overdues_per_credit', 'max'),
        total_number_of_overdues_mean = ('number_of_overdues_per_credit', 'mean'),

        number_of_hard_overdues_sum = ('number_of_hard_overdues_per_credit', 'sum'),
        number_of_hard_overdues_min = ('number_of_hard_overdues_per_credit', 'min'),
        number_of_hard_overdues_max = ('number_of_hard_overdues_per_credit', 'max'),
        number_of_hard_overdues_mean = ('number_of_hard_overdues_per_credit', 'mean'),

        number_of_hopeless_debts_sum = ('number_of_hopeless_debts', 'sum'),
        number_of_hopeless_debts_min = ('number_of_hopeless_debts', 'min'),
        number_of_hopeless_debts_max = ('number_of_hopeless_debts', 'max'),
        number_of_hopeless_debts_mean = ('number_of_hopeless_debts', 'mean'),

        risky_statust_sum = ('risky_status', 'sum'),
        risky_statust_min = ('risky_status', 'min'),
        risky_statust_max = ('risky_status', 'max'),
        risky_statust_mean = ('risky_status', 'mean'),
        
        )

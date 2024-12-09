import pandas as pd


def df_continuous_compressed(df_continuous:pd.DataFrame) -> pd.DataFrame:
    return df_continuous.groupby(['application_id'], as_index=False).agg(
        account_amt_credit_limit_sum = ('account_amt_credit_limit', 'sum'),
        account_amt_credit_limit_min = ('account_amt_credit_limit', 'min'),
        account_amt_credit_limit_max = ('account_amt_credit_limit', 'max'),
        account_amt_credit_limit_mean = ('account_amt_credit_limit', 'mean'),

        account_amt_ensured_amt_sum = ('account_amt_ensured_amt', 'sum'),
        account_amt_ensured_amt_min = ('account_amt_ensured_amt', 'min'),
        account_amt_ensured_amt_max = ('account_amt_ensured_amt', 'max'),
        account_amt_ensured_amt_mean = ('account_amt_ensured_amt', 'mean'),

        coborrower_solidary_num_sum = ('coborrower_solidary_num', 'sum'),
        coborrower_solidary_num_min = ('coborrower_solidary_num', 'min'),
        coborrower_solidary_num_max = ('coborrower_solidary_num', 'max'),
        coborrower_solidary_num_mean = ('coborrower_solidary_num', 'mean'),

        paymnt_condition_principal_terms_amt_sum = ('paymnt_condition_principal_terms_amt', 'sum'),
        paymnt_condition_principal_terms_amt_min = ('paymnt_condition_principal_terms_amt', 'min'),
        paymnt_condition_principal_terms_amt_max = ('paymnt_condition_principal_terms_amt', 'max'),
        paymnt_condition_principal_terms_amt_mean = ('paymnt_condition_principal_terms_amt', 'mean'),

        paymnt_condition_interest_terms_amt_sum = ('paymnt_condition_interest_terms_amt', 'sum'),
        paymnt_condition_interest_terms_amt_min = ('paymnt_condition_interest_terms_amt', 'min'),
        paymnt_condition_interest_terms_amt_max = ('paymnt_condition_interest_terms_amt', 'max'),
        paymnt_condition_interest_terms_amt_mean = ('paymnt_condition_interest_terms_amt', 'mean'),

        paymnt_condition_min_paymt_sum = ('paymnt_condition_min_paymt', 'sum'),
        paymnt_condition_min_paymt_min = ('paymnt_condition_min_paymt', 'min'),
        paymnt_condition_min_paymt_max = ('paymnt_condition_min_paymt', 'max'),
        paymnt_condition_min_paymt_mean = ('paymnt_condition_min_paymt', 'mean'),

        overall_val_credit_total_amt_sum = ('overall_val_credit_total_amt', 'sum'),
        overall_val_credit_total_amt_min = ('overall_val_credit_total_amt', 'min'),
        overall_val_credit_total_amt_max = ('overall_val_credit_total_amt', 'max'),
        overall_val_credit_total_amt_mean = ('overall_val_credit_total_amt', 'mean'),

        overall_val_credit_total_monetary_amt_sum = ('overall_val_credit_total_monetary_amt', 'sum'),
        overall_val_credit_total_monetary_amt_min = ('overall_val_credit_total_monetary_amt', 'min'),
        overall_val_credit_total_monetary_amt_max = ('overall_val_credit_total_monetary_amt', 'max'),
        overall_val_credit_total_monetary_amt_mean = ('overall_val_credit_total_monetary_amt', 'mean'),

        month_aver_paymt_aver_paymt_amt_sum = ('month_aver_paymt_aver_paymt_amt', 'sum'),
        month_aver_paymt_aver_paymt_amt_min = ('month_aver_paymt_aver_paymt_amt', 'min'),
        month_aver_paymt_aver_paymt_amt_max = ('month_aver_paymt_aver_paymt_amt', 'max'),
        month_aver_paymt_aver_paymt_amt_mean = ('month_aver_paymt_aver_paymt_amt', 'mean'),

        collat_insured_insur_limit_sum = ('collat_insured_insur_limit', 'sum'),
        collat_insured_insur_limit_min = ('collat_insured_insur_limit', 'min'),
        collat_insured_insur_limit_max = ('collat_insured_insur_limit', 'max'),
        collat_insured_insur_limit_mean = ('collat_insured_insur_limit', 'mean'),

        collat_repay_amt_sum = ('collat_repay_amt', 'sum'),
        collat_repay_amt_min = ('collat_repay_amt', 'min'),
        collat_repay_amt_max = ('collat_repay_amt', 'max'),
        collat_repay_amt_mean = ('collat_repay_amt', 'mean'),

        arrear_start_amt_outstanding_sum = ('arrear_start_amt_outstanding', 'sum'),
        arrear_start_amt_outstanding_min = ('arrear_start_amt_outstanding', 'min'),
        arrear_start_amt_outstanding_max = ('arrear_start_amt_outstanding', 'max'),
        arrear_start_amt_outstanding_mean = ('arrear_start_amt_outstanding', 'mean'),

        arrear_amt_outstanding_sum = ('arrear_amt_outstanding', 'sum'),
        arrear_amt_outstanding_min = ('arrear_amt_outstanding', 'min'),
        arrear_amt_outstanding_max = ('arrear_amt_outstanding', 'max'),
        arrear_amt_outstanding_mean = ('arrear_amt_outstanding', 'mean'),

        arrear_principal_outstanding_sum = ('arrear_principal_outstanding', 'sum'),
        arrear_principal_outstanding_min = ('arrear_principal_outstanding', 'min'),
        arrear_principal_outstanding_max = ('arrear_principal_outstanding', 'max'),
        arrear_principal_outstanding_mean = ('arrear_principal_outstanding', 'mean'),

        arrear_int_outstanding_sum = ('arrear_int_outstanding', 'sum'),
        arrear_int_outstanding_min = ('arrear_int_outstanding', 'min'),
        arrear_int_outstanding_max = ('arrear_int_outstanding', 'max'),
        arrear_int_outstanding_mean = ('arrear_int_outstanding', 'mean'),

        arrear_other_amt_outstanding_sum = ('arrear_other_amt_outstanding', 'sum'),
        arrear_other_amt_outstanding_min = ('arrear_other_amt_outstanding', 'min'),
        arrear_other_amt_outstanding_max = ('arrear_other_amt_outstanding', 'max'),
        arrear_other_amt_outstanding_mean = ('arrear_other_amt_outstanding', 'mean'),

        due_arrear_amt_outstanding_sum = ('due_arrear_amt_outstanding', 'sum'),
        due_arrear_amt_outstanding_min = ('due_arrear_amt_outstanding', 'min'),
        due_arrear_amt_outstanding_max = ('due_arrear_amt_outstanding', 'max'),
        due_arrear_amt_outstanding_mean = ('due_arrear_amt_outstanding', 'mean'),

        due_arrear_principal_outstanding_sum = ('due_arrear_principal_outstanding', 'sum'),
        due_arrear_principal_outstanding_min = ('due_arrear_principal_outstanding', 'min'),
        due_arrear_principal_outstanding_max = ('due_arrear_principal_outstanding', 'max'),
        due_arrear_principal_outstanding_mean = ('due_arrear_principal_outstanding', 'mean'),

        due_arrear_int_outstanding_sum = ('due_arrear_int_outstanding', 'sum'),
        due_arrear_int_outstanding_min = ('due_arrear_int_outstanding', 'min'),
        due_arrear_int_outstanding_max = ('due_arrear_int_outstanding', 'max'),
        due_arrear_int_outstanding_mean = ('due_arrear_int_outstanding', 'mean'),

        due_arrear_other_amtoutstanding_sum = ('due_arrear_other_amtoutstanding', 'sum'),
        due_arrear_other_amtoutstanding_min = ('due_arrear_other_amtoutstanding', 'min'),
        due_arrear_other_amtoutstanding_max = ('due_arrear_other_amtoutstanding', 'max'),
        due_arrear_other_amtoutstanding_mean = ('due_arrear_other_amtoutstanding', 'mean'),

        past_due_amt_past_due_sum = ('past_due_amt_past_due', 'sum'),
        past_due_amt_past_due_min = ('past_due_amt_past_due', 'min'),
        past_due_amt_past_due_max = ('past_due_amt_past_due', 'max'),
        past_due_amt_past_due_mean = ('past_due_amt_past_due', 'mean'),

        past_due_principal_amt_past_due_sum = ('past_due_principal_amt_past_due', 'sum'),
        past_due_principal_amt_past_due_min = ('past_due_principal_amt_past_due', 'min'),
        past_due_principal_amt_past_due_max = ('past_due_principal_amt_past_due', 'max'),
        past_due_principal_amt_past_due_mean = ('past_due_principal_amt_past_due', 'mean'),

        past_due_int_amt_past_due_sum = ('past_due_int_amt_past_due', 'sum'),
        past_due_int_amt_past_due_min = ('past_due_int_amt_past_due', 'min'),
        past_due_int_amt_past_due_max = ('past_due_int_amt_past_due', 'max'),
        past_due_int_amt_past_due_mean = ('past_due_int_amt_past_due', 'mean'),

        past_due_other_amt_past_due_sum = ('past_due_other_amt_past_due', 'sum'),
        past_due_other_amt_past_due_min = ('past_due_other_amt_past_due', 'min'),
        past_due_other_amt_past_due_max = ('past_due_other_amt_past_due', 'max'),
        past_due_other_amt_past_due_mean = ('past_due_other_amt_past_due', 'mean'),

        delay5_sum = ('delay5', 'sum'),
        delay5_min = ('delay5', 'min'),
        delay5_max = ('delay5', 'max'),
        delay5_mean = ('delay5', 'mean'),

        delay30_sum = ('delay30', 'sum'),
        delay30_min = ('delay30', 'min'),
        delay30_max = ('delay30', 'max'),
        delay30_mean = ('delay30', 'mean'),

        delay60_sum = ('delay60', 'sum'),
        delay60_min = ('delay60', 'min'),
        delay60_max = ('delay60', 'max'),
        delay60_mean = ('delay60', 'mean'),

        delay90_sum = ('delay90', 'sum'),
        delay90_min = ('delay90', 'min'),
        delay90_max = ('delay90', 'max'),
        delay90_mean = ('delay90', 'mean'),

        delay_more_sum = ('delay_more', 'sum'),
        delay_more_min = ('delay_more', 'min'),
        delay_more_max = ('delay_more', 'max'),
        delay_more_mean = ('delay_more', 'mean'),

        cred_max_overdue_sum = ('cred_max_overdue', 'sum'),
        cred_max_overdue_min = ('cred_max_overdue', 'min'),
        cred_max_overdue_max = ('cred_max_overdue', 'max'),
        cred_max_overdue_mean = ('cred_max_overdue', 'mean'),
    )
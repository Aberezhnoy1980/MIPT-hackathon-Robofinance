from .small_variables import *

datetime_cols = [
'reporting_dt',
'fund_date', 
'trade_opened_dt',
'trade_close_dt', 
'paymnt_condition_principal_terms_amt_dt',
'paymnt_condition_interest_terms_amt_dt',       
'paymnt_condition_grace_start_dt', 
'paymnt_condition_grace_end_dt',
'paymnt_condition_interest_payment_due_date',       
# 'overall_val_credit_total_amt_date', # Дата расчета полной стоимости кредита (займа) - возможно от данного столбца можно избавиться, т.к. сама по себе дата расчета показателя ни на что не должна влиять
# 'month_aver_paymt_calc_date', # тоже можно избавиться по тем же причинам
'collat_insured_insur_start_dt',
'collat_insured_insur_end_dt', 
'collat_insured_insur_fact_end_dt',       
'collat_repay_dt', 
'loan_indicator_dt', 
'legal_items_court_act_dt', 
'hold_dt', 
'file_since_dt', 
'last_updated_dt',
'last_uploaded_dt', 
'arrear_calc_date',
'due_arrear_start_dt',
# 'due_arrear_calc_date', # тоже можно избавиться по тем же причинам
'past_due_dt', 
'past_due_calc_date', 
'past_due_principal_missed_date',
'past_due_int_missed_date']

datetime_cols.append(acc_uid)
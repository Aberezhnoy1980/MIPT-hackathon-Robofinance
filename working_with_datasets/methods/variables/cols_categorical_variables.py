from .small_variables import *

cols_categorical_variables = [
'trade_owner_indic',
'trade_trade_type_code',
'trade_loan_kind_code',
'trade_acct_type1',
'trade_has_card',
'trade_is_novation',
'trade_is_money_source',
'coborrower_has_solidary',
'coborrower_solidary_num',	
'paymnt_condition_terms_frequency',
'has_collaterals',
'has_guarantees',
'has_indie_guarantees',
'collat_insured_insur_sign',
'collat_insured_has_franchise',
'collat_insured_insur_end_reason',
'colat_repaid',
'collat_repay_code',
'loan_indicator',
'legal_items_has_legal_dispute',
'legal_items_court_act_effect_code',
'hold_code',
'arrear_sign',
'arrear_last_payment_due_code',
'arrear_unconfirm_grace',
'due_arrear_last_payment_due_code',
'past_due_last_payment_due_code'
]


cols_categorical_variables.append(application_id)